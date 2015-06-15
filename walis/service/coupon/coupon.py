#!/usr/bin/env python2
# -*- coding: utf8 -*-

from __future__ import print_function, division, absolute_import

from walis.thirdparty import thrift_client, thirdparty_svc
from walis.utils.misc import ttype2dict
from walis.utils.time import str2timestamp

MAX_QUERY_LIMIT = 1000
DEFAULT_QUERY_LIMIT = 50


def get(coupon_id):
    with thrift_client('eos') as eos:
        result = eos.get_coupon(int(coupon_id))
    return ttype2dict(result)


def query(sn=None, batch_sn=None, offset=None, limit=DEFAULT_QUERY_LIMIT):
    condition = thirdparty_svc.eos.TCouponQuery()
    if sn is not None:
        condition.coupon_sn = sn

    if batch_sn is not None:
        condition.batch_sn = batch_sn

    with thrift_client('eos') as eos:
        coupon_total = eos.walle_count_coupon(condition)

    if offset is not None:
        condition.offset = offset

    if limit is not None:
        condition.limit = min(limit, MAX_QUERY_LIMIT)

    with thrift_client('eos') as eos:
        coupon_list = eos.walle_query_coupon(condition)

    return {
        'list': coupon_list,
        'total': coupon_total
    }


def save_generic_coupon(batch_sn, deadline, sn, remain):
    with thrift_client('eos') as eos:
        coupon = eos.save_coupon(
            id=None,
            sn=sn,
            batch_sn=batch_sn,
            remain=remain,
            deadline=deadline
        )
        return ttype2dict(coupon)


def save_onetime_coupon(batch_sn, remain, deadline, remarks, count):
    with thrift_client('eos') as eos:
        return eos.batch_generate_coupon(
            batch_sn=batch_sn,
            remain=remain,
            deadline=str2timestamp(deadline),
            remarks=remarks,
            count=count,
            coupon_sn_length=10,
            use_alnum=False
        )


def update(coupon_id, deadline=None, remain=None):
    with thrift_client('eos') as eos:
        return eos.save_coupon(
            id=int(coupon_id),
            sn='',
            batch_sn='',
            remain=int(remain) if remain else 0,
            deadline=deadline if deadline else ''
        )


def mget_by_sn(sn):
    with thrift_client('eos') as eos:
        return eos.mget_coupon_by_sn([sn, ])
