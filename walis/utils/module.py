#!/usr/bin/env python2
# coding=utf8

from __future__ import absolute_import, division, print_function
from importlib import import_module

from walis.exception.util import raise_dev_exc
from walis.exception.error_code import (
    DEV_MODULE_ATTR_ERR,
    DEV_MODULE_PATH_ERR,
    DEV_MODULE_LOAD_ERR
)

def load_obj(path):
    """Load an object given its absolute object path, and return it.

    object can be a class, function, variable o instance.
    path ie: 'scrapy.contrib.downloadermiddelware.redirect.RedirectMiddleware'
    """

    try:
        dot = path.rindex('.')
    except ValueError:
        raise_dev_exc(DEV_MODULE_PATH_ERR, path=path)

    module, name = path[:dot], path[dot+1:]
    try:
        mod = import_module(module)
    except ImportError as e:
        raise_dev_exc(DEV_MODULE_LOAD_ERR, path=path, exc=e)

    try:
        obj = getattr(mod, name)
    except AttributeError:
        raise_dev_exc(DEV_MODULE_ATTR_ERR, module=module, name=name)

    return obj
