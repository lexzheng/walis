#!/usr/bin/env python2
# -*- coding: utf8 -*-

from __future__ import absolute_import, division, print_function

from walis.utils.http import args_parser, Arg
from walis.utils.paging import get_paging_params
from walis.service.coupon import (
    coupon as coupon_base,
    rst_coupon_batch,
    batch as coupon_batch_base
)
from walis.exception.util import raise_user_exc
from walis.exception.error_code import (
    COUPON_SN_REQUIRED,
    COUPON_SN_INVALID,
    COUPON_COUNT_REQUIRED,
    COUPON_COUNT_INVALID
)

GENERIC_COUPON = 1
ONETIME_COUPON = 2
COUPON_TYPE = (GENERIC_COUPON, ONETIME_COUPON)

GENERAL_COUPON_DEFAULT_REMAIN = 99999999


def get(coupon_id):
    coupon = coupon_base.get(coupon_id)
    # add associated restaurant-ids
    coupon['rst_ids'] = rst_coupon_batch.get_rst_ids(coupon['batch_sn'])
    # add batch type if it can be confirmed, else it's -1 (unknow)
    coupon_batch = coupon_batch_base.get_by_batch_sn(coupon['batch_sn'])
    if coupon_batch is not None:
        coupon['batch_type'] = coupon_batch.batch_type
    else:
        coupon['batch_type'] = -1

    return coupon


def query():
    args_spec = {
        'sn': Arg(str),
        'batch_sn': Arg(str),
    }
    args = args_parser.parse(args_spec)
    page_no, page_size = get_paging_params()
    offset = (page_no - 1) * page_size
    limit = page_size

    return coupon_base.query(
        sn=args['sn'],
        batch_sn=args['batch_sn'],
        offset=offset,
        limit=limit
    )


def save():
    args_spec = {
        'coupon_type': Arg(int, required=True, validate=lambda t: t in COUPON_TYPE, error='Invalid coupon type'),
        'batch_sn': Arg(str, required=True),
        'deadline': Arg(str, required=True),
        'sn': Arg(str),
        'remain': Arg(int),
        'count': Arg(int),
    }
    args = args_parser.parse(args_spec)

    if args['coupon_type'] == GENERIC_COUPON:
        if args.get('sn') is None:
            raise_user_exc(COUPON_SN_REQUIRED)

        if not _check_sn_length(args['sn']):
            raise_user_exc(COUPON_SN_INVALID)

        remain = args.get('remain') or GENERAL_COUPON_DEFAULT_REMAIN

        result = coupon_base.save_generic_coupon(
            batch_sn=args['batch_sn'],
            deadline=args['deadline'],
            sn=args['sn'],
            remain=remain
        )
        result = [result.get('sn'), ]
    else:
        if args.get('count') is None:
            raise_user_exc(COUPON_COUNT_REQUIRED)

        if int(args.get('count')) > 500:
            raise_user_exc(COUPON_COUNT_INVALID)

        result = coupon_base.save_onetime_coupon(
            batch_sn=args['batch_sn'],
            remain=1,
            deadline=args['deadline'],
            remarks=u"后台生成",
            count=args['count']
        )

    return result


def update(coupon_id):
    args_spec = {
        'deadline': Arg(str, allow_missing=True),
        'remain': Arg(int, allow_missing=True),
    }
    args = args_parser.parse(args_spec)

    return coupon_base.update(
        coupon_id=coupon_id,
        deadline=args.get('deadline'),
        remain=args.get('remain', 0),
    )


def validate_sn(sn):
    valid = False
    if _check_sn_length(sn):
        coupon = coupon_base.mget_by_sn(sn)
        valid = False if coupon else True

    return {
        'is_valid': valid
    }


def _check_sn_length(sn):
    return len(str(sn)) <= 32
