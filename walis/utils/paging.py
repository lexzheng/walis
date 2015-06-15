#!/usr/bin/env python2
# coding=utf8

from __future__ import absolute_import, division, print_function


#!/usr/bin/env python2
# coding=utf8

from __future__ import absolute_import, division, print_function
import functools

from flask import request
from webargs import Arg
from walis.utils.http import args_parser


FIRST_PAGE = 1
# DEFAULT_PAGE_SIZE = sys.maxint
DEFAULT_PAGE_SIZE = 10000

MAX_LIMIT_SIZE = 1000


def page_deco(paging_size=DEFAULT_PAGE_SIZE, allow_missing=True):
    """
    [deprecated] not so useful
    automatically parse <page_no> and <page_size>
    """

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            args_spec = {
                'page_no': Arg(int, allow_missing=allow_missing),
                'page_size': Arg(int, allow_missing=allow_missing),
            }
            argments = args_parser.parse(args_spec, request)
            page_no = argments.get('page_no', FIRST_PAGE)
            page_size = argments.get('page_size', paging_size)
            func.func_globals['page_no'] = page_no
            func.func_globals['page_size'] = page_size
            ret = func(*args, **kwargs)
            func.func_globals.pop('page_no')
            func.func_globals.pop('page_size')
            return ret

        return wrapper

    return decorator


def get_paging_params(paging_size=DEFAULT_PAGE_SIZE,
                      allow_missing=True,
                      db_style=False):
    args_spec = {
        'page_no': Arg(int, allow_missing=allow_missing),
        'page_size': Arg(int, allow_missing=allow_missing),
    }
    argments = args_parser.parse(args_spec, request)
    page_no = argments.get('page_no', FIRST_PAGE)
    page_size = argments.get('page_size', paging_size)

    if db_style:
        offset = (page_no-1) * page_size
        limit = page_size
        return offset, limit

    return page_no, page_size


def paging(collection):
    """
    You will need it when paging for collections.

    :param collection: list or tuple
    :return: partial collection after paging
    """
    if type(collection) not in (list, tuple):
        return []

    page_no, page_size = get_paging_params()

    return collection[(page_no - 1) * page_size: page_no * page_size]
