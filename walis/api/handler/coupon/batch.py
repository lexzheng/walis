#!/usr/bin/env python2
# -*- coding: utf8 -*-

from __future__ import absolute_import, division, print_function

from flask.ext.login import current_user

from walis.utils.http import args_parser, Arg
from walis.utils.paging import get_paging_params
from walis.service.coupon import batch as coupon_batch_base
from walis.exception.util import raise_user_exc
from walis.exception.error_code import RST_IDS_REQUIRED

BATCH_RST_GEN = 1
BATCH_RST_ONE = 2
BATCH_NORST_GEN = 3
BATCH_NORST_ONE = 4

BATCH_TYPE_LIST = [
    BATCH_RST_GEN,
    BATCH_RST_ONE,
    BATCH_NORST_GEN,
    BATCH_NORST_ONE
]
BATCH_TYPE_RST = [
    BATCH_RST_GEN,
    BATCH_RST_ONE
]


def save():
    args_spec = {
        'batch_type': Arg(int, required=True, validate=lambda t: t in BATCH_TYPE_LIST, error='Invalid batch type'),
        'rst_ids': Arg(str, allow_missing=True)
    }
    args = args_parser.parse(args_spec)

    # check restaurant ids when the batch bound with restaurant
    if args['batch_type'] in BATCH_TYPE_RST:
        if args.get('rst_ids') is None:
            raise_user_exc(RST_IDS_REQUIRED)

        args['rst_ids'] = [int(rst_id) for rst_id in args['rst_ids'].split()]

    batch_sn = coupon_batch_base.save(
        args['batch_type'], current_user.id, current_user.name,
        args.get('rst_ids', None)
    )

    return {
        'batch_sn': batch_sn
    }


def query():
    args_spec = {
        'admin_id': Arg(int, allow_missing=True)
    }
    args = args_parser.parse(args_spec)
    page_no, page_size = get_paging_params()
    offset = (page_no - 1) * page_size
    limit = page_size

    return coupon_batch_base.query(
        admin_id=args.get('admin_id', current_user.get_id()),
        offset=offset,
        limit=limit
    )
