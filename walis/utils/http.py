#!/usr/bin/env python2
# coding=utf8

from __future__ import absolute_import, division, print_function

import json

import jsonpickle
from flask import request
import webargs.core
from webargs.flaskparser import FlaskParser
from webargs.core import Parser
from webargs import Arg

from .format import to_int

# TODO 整理这个文件 ***************************


def get_real_remote_addr():
    # todo 当前未考虑负载均衡-.-
    # 写的时候请参考nginx的配置-.-...
    """
    当前未考虑负载均衡
    """
    # for x in request.access_route:
    # print(x)
    return request.remote_addr


def jsonpickle_dumps(obj, **kwargs):
    kwargs.setdefault('unpicklable', False)
    return jsonpickle.encode(obj, **kwargs)


def jsonpickle_loads(string, **kwargs):
    return jsonpickle.decode(string, **kwargs)


args_parser = None


class ArgsParser(FlaskParser):
    def all_args_spec(self, req=None, *args, **kwargs):
        # todo 这里有bug肯定的-.-temp fix
        req = req or request
        targets = kwargs.get('targets', []) or self.targets
        spec = {}
        for target in targets:
            if target == 'json':
                json_dict = req.get_json(silent=True)
                if json_dict:
                    [spec.__setitem__(k, Arg()) for k in json_dict.keys()]
            elif target == 'querystring':
                [spec.__setitem__(k, Arg()) for k in req.args.keys()]
            elif target == 'form':
                [spec.__setitem__(k, Arg()) for k in req.form.keys()]
            elif target == 'headers':
                [spec.__setitem__(k, Arg()) for k in req.headers.keys()]
            elif target == 'cookies':
                [spec.__setitem__(k, Arg()) for k in req.cookies.keys()]
            elif target == 'files':
                [spec.__setitem__(k, Arg()) for k in req.files.keys()]
            elif target == '_data':
                _data = request.args.get('_data', None)
                try:
                    json_data = json.loads(_data, )
                except Exception:
                    json_data = None
                if json_data:
                    [spec.__setitem__(k, Arg()) for k in json_data.keys()]
            else:
                pass
        return spec

    def parse_all(self, req=None, *args, **kwargs):
        args_spec = self.all_args_spec(req, *args, **kwargs)
        return self.parse(args_spec, req, *args, **kwargs)


def _auto_init():
    global args_parser
    default_targets = Parser.DEFAULT_TARGETS
    position = 'first'
    if position == 'first':
        targets = ('_data',) + default_targets
    elif position == 'last':
        targets = default_targets + ('_data',)
    else:
        targets = default_targets
    args_parser = ArgsParser(targets=targets)


def get_single_arg(arg_name, arg_type, allow_missing=False):
    arg_spec = {
        arg_name: webargs.Arg(arg_type, allow_missing=allow_missing),
    }
    arg = args_parser.parse(arg_spec)
    return arg.get(arg_name)


_auto_init()


@args_parser.target_handler('_data')
def parse_data(request, name, arg):
    _data = request.args.get('_data', None)
    try:
        json_data = json.loads(_data, )
    except Exception:
        json_data = None
    if json_data:
        return webargs.core.get_value(json_data, name, arg.multiple)
    else:
        return None


@args_parser.error_handler
def handle_error(error):
    raise error


def args_to_tobj(tobj_or_ttype):
    # todo test here-.-
    tobj = tobj_or_ttype
    args = args_parser.parse_all()
    for k, v in args.iteritems():
        setattr(tobj, k, v)
    return tobj


def format_int(args, key):
    args.__setitem__(key, to_int(args.get(key)))
