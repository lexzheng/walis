#!/usr/bin/env python2
# coding=utf8

from __future__ import absolute_import, division, print_function
from webargs import Arg
from walis.utils.http import args_parser
from walis.service.misc import amended_poi


def get():
    return amended_poi.gets()


def save():
    args = _get_args()
    return amended_poi.save(args)


def update():
    args = _get_args(allow_missing=True)
    _id = args.get('id')
    return amended_poi.update(_id, args)


def _get_args(allow_missing=False):
    args_spec = {
        'id': Arg(int, allow_missing=not allow_missing),
        'name': Arg(allow_missing=allow_missing),
        'city_id': Arg(int, allow_missing=allow_missing),
        'longitude': Arg(float, allow_missing=allow_missing),
        'latitude': Arg(float, allow_missing=allow_missing),
        'extra_tag': Arg(allow_missing=allow_missing),
        'address': Arg(allow_missing=allow_missing),
    }
    return args_parser.parse(args_spec)

