#!/usr/bin/env python2
# -*- coding: utf8 -*-

from __future__ import print_function, division, absolute_import

from walis.thirdparty import thrift_client, thirdparty_svc
from walis.utils.time import timestamp2datetime

MAX_QUERY_LIMIT = 1000
DEFAULT_QUERY_LIMIT = 50


def save(batch_type, admin_id, admin_name, restaurant_ids=None):
    batch_info = thirdparty_svc.eos.TCouponBatchInfo()
    batch_info.batch_type = batch_type
    batch_info.admin_id = admin_id
    batch_info.admin_name = admin_name
    if restaurant_ids is not None:
        batch_info.restaurant_ids = restaurant_ids

    with thrift_client('eos') as eos:
        return eos.generate_coupon_batch(batch_info)


def get_by_batch_sn(batch_sn):
    condition = thirdparty_svc.eos.TCouponBatchQuery()
    condition.batch_sn = batch_sn

    with thrift_client('eos') as eos:
        batch_record_list = eos.query_coupon_batch_record(condition)

    try:
        return batch_record_list.pop()
    except IndexError:
        return None


def query(admin_id=None, offset=None, limit=DEFAULT_QUERY_LIMIT):
    condition = thirdparty_svc.eos.TCouponBatchQuery()

    if admin_id is not None:
        condition.admin_id = admin_id

    if offset is not None:
        condition.offset = offset

    if limit is not None:
        condition.limit = min(limit, MAX_QUERY_LIMIT)

    with thrift_client('eos') as eos:
        batch_record_list = eos.query_coupon_batch_record(condition)

    # make datetime readable
    for batch_record in batch_record_list:
        batch_record.created_at = timestamp2datetime(
            batch_record.created_at)
        batch_record.updated_at = timestamp2datetime(
            batch_record.updated_at)

    return batch_record_list
