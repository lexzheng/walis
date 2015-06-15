#!/usr/bin/env python2
# coding=utf8

from __future__ import absolute_import, division, print_function

import inspect
from functools import wraps
import time
import sys
from werkzeug.routing import parse_rule
from flask import request
import re
from .ctx import ApiCtx
from walis.exception import (
    UserExc,
    SysExc,
)
from .response import (
    make_res,
    make_exc_res,
)
from .signal import (
    sig_call_ok,
    sig_call_done,
    sig_call_user_exc,
    sig_call_sys_exc,
    sig_call_unexcepted_exc,
)

from walis.exception.util import raise_dev_exc
from walis.exception.error_code import DEV_CLASS_EXTENDS_ERR, DEV_METHOD_VALID

buildin_methods = ["get", "gets", "post", "put", "patch", "upload", "delete"]


def api(rule='/', **options):
    """ API decorator for walis api
    """
    api_ctx = ApiCtx()

    def _wrapper(func):
        _cache_api(func, rule, options)

        @wraps(func)
        def wrapper(*args, **kwargs):
            api_ctx.func = func
            api_ctx.req = request
            api_ctx.started_at = time.time()
            module_name = func.func_globals['__name__']
            api_ctx.module = module_name[module_name.rindex('.')+1:]

            try:
                rv = func(*args, **kwargs)
            except UserExc as exc:
                api_ctx.exc = exc
                api_ctx.response = make_exc_res(exc)
                sig_call_user_exc.send(api_ctx)
            except SysExc as exc:
                api_ctx.exc = exc
                api_ctx.response = make_exc_res(exc)
                sig_call_sys_exc.send(api_ctx)
            except:
                api_ctx.exc = sys.exc_info()[1]
                api_ctx.response = make_exc_res(api_ctx.exc)
                sig_call_unexcepted_exc.send(api_ctx)
            else:
                api_ctx.response = make_res(rv)
                sig_call_ok.send(api_ctx)
            sig_call_done.send(api_ctx)
            return api_ctx.response

        return wrapper

    return _wrapper


def _cache_api(func, rule, options):
    if rule is not None:
        if options.get('methods') is None:
            if func.__name__ in buildin_methods:
                options.update(methods=[func.__name__.upper()])
            else:
                options.update(methods=['GET'])
        if not hasattr(func, 'api_cache') or func.api_cache is None:
            func.api_cache = {func.__name__: [(rule, options)]}
        elif not func.__name__ in func.api_cache:
            func.api_cache[func.__name__] = [(rule, options)]
        else:
            func.api_cache[func.__name__].append((rule, options))


class WalisView(object):

    decorators = []
    route_base = None
    route_prefix = None
    trailing_slash = True

    @classmethod
    def register(cls, app, route_base=None, subdomain=None, route_prefix=None,
                 trailing_slash=None):

        if cls is WalisView:
            raise_dev_exc(DEV_CLASS_EXTENDS_ERR, class_name='WalisApi')

        if route_base:
            cls.orig_route_base = cls.route_base
            cls.route_base = route_base

        if route_prefix:
            cls.orig_route_prefix = cls.route_prefix
            cls.route_prefix = route_prefix

        if not subdomain:
            if hasattr(app, "subdomain") and app.subdomain is not None:
                subdomain = app.subdomain
            elif hasattr(cls, "subdomain"):
                subdomain = cls.subdomain

        if trailing_slash is not None:
            cls.orig_trailing_slash = cls.trailing_slash
            cls.trailing_slash = trailing_slash

        members = get_interesting_members(WalisView, cls)

        for name, value in members:
            view_func = getattr(cls(), name)
            route_name = cls._build_endpoint(name)

            if hasattr(value, "api_cache") and name in value.api_cache:
                for idx, cached_rule in enumerate(value.api_cache[name]):
                    rule, options = cached_rule
                    rule = cls._build_rule(rule)
                    sub, ep, options = cls.parse_options(options)

                    if not subdomain and sub:
                        subdomain = sub

                    if ep:
                        endpoint = ep
                    elif len(value.api_cache[name]) == 1:
                        endpoint = route_name
                    else:
                        endpoint = "%s_%d" % (route_name, idx,)

                    trailing_slash = options.pop('trailing_slash', True)
                    if not trailing_slash:
                        rule = rule.rstrip("/")

                    view_func = cls._make_deco_func(view_func)
                    app.add_url_rule(rule, endpoint, view_func,
                                     subdomain=subdomain, **options)
            elif name in buildin_methods:
                view_func = api(rule=None)(view_func)
                view_func = cls._make_deco_func(view_func)

                if name in ["gets"]:
                    methods = ["GET"]
                else:
                    methods = [name.upper()]

                rule = cls._build_rule("/", value)
                if not cls.trailing_slash:
                    rule = rule.rstrip("/")

                app.add_url_rule(rule, route_name, view_func, methods=methods,
                                 subdomain=subdomain)
            else:
                # TODO
                raise_dev_exc(DEV_METHOD_VALID, msg=u'函数必须是<WalisApi>支持的内建函数或者由@api修饰')

        if hasattr(cls, "orig_route_base"):
            cls.route_base = cls.orig_route_base
            del cls.orig_route_base

        if hasattr(cls, "orig_route_prefix"):
            cls.route_prefix = cls.orig_route_prefix
            del cls.orig_route_prefix

        if hasattr(cls, "orig_trailing_slash"):
            cls.trailing_slash = cls.orig_trailing_slash
            del cls.orig_trailing_slash

    @classmethod
    def parse_options(cls, options):
        """Extracts subdomain and endpoint values from the options dict and returns
           them along with a new dict without those values.
        """
        options = options.copy()
        subdomain = options.pop('subdomain', None)
        endpoint = options.pop('endpoint', None)
        return subdomain, endpoint, options,

    @classmethod
    def _build_rule(cls, rule, method=None):
        """Creates a routing rule based on either the class name (minus the
        'View' suffix) or the defined `route_base` attribute of the class

        :param rule: the path portion that should be appended to the
                     route base

        :param method: if a method's arguments should be considered when
                       constructing the rule, provide a reference to the
                       method here. arguments named "self" will be ignored
        """

        rule_parts = []

        if cls.route_prefix:
            rule_parts.append(cls.route_prefix)

        route_base = cls._get_route_base()
        if route_base:
            rule_parts.append(route_base)

        rule_parts.append(rule)
        ignored_rule_args = ['self']
        if hasattr(cls, 'base_args'):
            ignored_rule_args += cls.base_args

        if method:
            args = get_true_argspec(method, method.__name__)[0]
            for arg in args:
                if arg not in ignored_rule_args:
                    rule_parts.append("<%s>" % arg)

        result = "/%s" % "/".join(rule_parts)
        return re.sub(r'(/)\1+', r'\1', result)


    @classmethod
    def _get_route_base(cls):
        """Returns the route base to use for the current class."""

        if cls.route_base is not None:
            route_base = cls.route_base
            base_rule = parse_rule(route_base)
            cls.base_args = [r[2] for r in base_rule]
        else:
            if cls.__name__.endswith("View"):
                route_base = cls.__name__[:-4].lower()
            elif cls.__name__.endswith("Api"):
                route_base = cls.__name__[:-3].lower()
            else:
                route_base = cls.__name__.lower()

        return route_base.strip("/")

    @classmethod
    def _build_endpoint(cls, method_name):
        return cls.__name__ + ":%s" % method_name

    @classmethod
    def _make_deco_func(cls, view_func):
        if cls.decorators:
            for decorator in cls.decorators:
                view_func = decorator(view_func)
        return view_func


def get_interesting_members(base_class, cls):
    """Returns a list of methods that can be routed to"""

    base_members = dir(base_class)
    all_members = inspect.getmembers(cls, predicate=inspect.ismethod)
    return [member for member in all_members
            if not member[0] in base_members
            and (hasattr(member[1], "__self__")
                 and not member[1].__self__ in inspect.getmro(cls))
            and not member[0].startswith("_")
            and not member[0].startswith("before_")
            and not member[0].startswith("after_")]


def get_true_argspec(method, raw_method_name=None):
    """
    Drills through layers of decorators attempting to
    locate the actual argspec for the method.
    """

    argspec = inspect.getargspec(method)
    args = argspec[0]
    if args and args[0] == 'self':
        return argspec
    if hasattr(method, '__func__'):
        method = method.__func__
    if not hasattr(method, '__closure__') or method.__closure__ is None:
        if method.__name__ != raw_method_name:
            return []

    closure = method.__closure__
    for cell in closure:
        inner_method = cell.cell_contents
        if inner_method is method:
            continue
        if not inspect.isfunction(inner_method) \
                and not inspect.ismethod(inner_method):
            continue
        true_argspec = get_true_argspec(inner_method, raw_method_name)
        if true_argspec:
            return true_argspec
