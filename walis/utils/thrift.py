#!/usr/bin/env python2
# -*- coding: utf8 -*-

from __future__ import absolute_import, division, print_function

class ThriftEnum(object):
    #todo enum 是一个类型,应该写成元类的方式-.-...
    # 现在这种写法无法进行类型判断-.-...
    def __init__(self, enum, excluded=None):
        self.enum = enum
        if excluded is None:
            excluded = []
        _dict = {}
        for k, v in enum._NAMES_TO_VALUES.iteritems():
            if k not in excluded:
                setattr(self, k, v)
                _dict[k] = v
        self._n2v = _dict
        self._v2n = {v: k for k, v in _dict.iteritems()}


def dict2ttype(maps, ttype, keys=None):
    if keys is None:
        keys = maps.keys()
    keys_set = set(keys)

    for key, value in maps.items():
        if key in keys_set:
            setattr(ttype, key, value)
    return ttype


def ttype2dict(ttype, keys=None):
    keys_set = []
    maps = {}
    if keys:
        keys_set = set(keys)

    for key, value in ttype.__dict__.items():
        if keys_set and key not in keys_set:
            continue
        maps[key] = value
    return maps
