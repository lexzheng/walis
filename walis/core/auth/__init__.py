#!/usr/bin/env python2
# coding=utf8

from __future__ import absolute_import, division, print_function
import functools

from flask.ext.login import current_user

from walis import config
from walis.core.auth.map import (
    permission_map,
    AUTH_MAP,
    AUTH_MAP_HR,
)
from walis.core.response import make_no_permission_res

from walis.thirdparty.coffee import coffee

from pprint import pprint as pp

def auth_init(app):
    # TODO 考虑统一抽出deco view的规则
    endpoint_list = filter(
        lambda endpoint: endpoint in AUTH_MAP.keys(),
        app.view_functions.keys()
    )

    endpoint_list_hr = filter(
        lambda endpoint: endpoint in AUTH_MAP_HR.keys(),
        app.view_functions.keys()
    )

    # add login deco for each view_func
    for ep in endpoint_list:
        app.view_functions[ep] = auth(ep)(app.view_functions[ep])

    for ep in endpoint_list_hr:
        app.view_functions[ep] = auth_hr(ep)(app.view_functions[ep])


def auth(endpoint):
    """ auth deco.
    """

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            auth_groups = AUTH_MAP.get(endpoint)

            if config.LOGIN['enabled'] and \
                    not current_user.has_groups(auth_groups):
                # TODO rase exception here
                return no_permission()

            return func(*args, **kwargs)

        return wrapper

    return decorator


def auth_hr(endpoint):
    """ auth deco.
    """

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            permission_code = AUTH_MAP_HR.get(endpoint)
            if config.LOGIN['enabled'] and \
                    not coffee.hr_permission.isPermittedToThis(context=current_user.auth_context,
                                                               permission=permission_code):
                return no_permission()

            return func(*args, **kwargs)

        return wrapper

    return decorator


# TODO to be deprecated
def permission(permission_name=None):
    """
    permission decorator used in Api class functions
    Used in two ways:
        1. give certain permission_name and config it in permission/config.py
        2. use default permission key (api_class_name:func_name) and config it
            in permission/config.py
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            permission_key = permission_name
            if permission_name is None:
                permission_key = ':'.join(
                    [self.__class__.__name__, func.__name__])

            p_groups = permission_map.get(permission_key)

            is_permitted = False
            if 'superadmin' in p_groups and current_user.is_super_admin():
                is_permitted = True

            if not is_permitted:
                if p_groups is None:
                    return no_permission()

                if config.LOGIN['enabled'] and \
                        not current_user.has_groups(p_groups):
                    return no_permission()

            return func(self, *args, **kwargs)

        return wrapper

    return decorator


def no_permission():
    return make_no_permission_res()


