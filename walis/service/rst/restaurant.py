#!/usr/bin/env python2
# -*- coding: utf8 -*-

from __future__ import absolute_import, print_function, division

import json
import logging

from walis.thirdparty import (
    thrift_client,
    thirdparty_svc,
)

from walis.utils.misc import ttype2dict
from walis.utils.misc import getresult_to_raw
from walis.service.rst import inner

log = logging.getLogger('all.restaurant-app')


def get_restaurants(ids):
    ids = list(set(ids))
    restaurants = inner.get_restaurants(ids)
    return [ttype2dict(rst) for rst in restaurants]


def get_restaurants_map(ids):
    restaurants = get_restaurants(ids)
    return {rst['id']: rst for rst in restaurants}


def get(id_or_ids):
    with thrift_client('ers') as ers:
        if isinstance(id_or_ids, (tuple, list)):
            result = ers.mget(id_or_ids)
        else:
            result = ers.get(id_or_ids)
    result = getresult_to_raw(result)
    return result


mget = get


def get_by_mobile(mobile):
    """
    :param mobile <string>
    :return Restaurant
    """
    with thrift_client('ers') as ers:
        try:
            rst = ers.get_by_mobile(mobile)
        except Exception:
            rst = None

    return rst


def get_map(restaurant_ids):
    with thrift_client('ers') as ers:
        restaurants = ers.mget(restaurant_ids)
    return {r.id: r for r in restaurants}


def get_admin_id(restaurant_id):
    with thrift_client('eus') as eus:
        return eus.get_restaurant_admin(restaurant_id).user_id


def get_olpay_records(user_id, begin_date, end_date, type=None):
    with thrift_client('eus') as eus:
        records = eus.account_get_stats(user_id, begin_date, end_date)

    if type is None:
        records = [r for r in records if r.type in (0, 1)]
    else:
        records = [r for r in records if r.type == type]
    return records


def get_olpay_detail(user_id, begin_date, end_date,
                     offset, limit, status=None):
    query = _create_olpay_records_query(user_id, begin_date, end_date,
                                        offset, limit, status)

    with thrift_client('eus') as eus:
        records = eus.query_trade_record(query)
        total_num = eus.count_trade_record(query)

    return records, total_num


def _create_olpay_records_query(user_id, begin_date, end_date,
                                offset, limit, status=None):
    query = thirdparty_svc.eus.TTradeRecordQuery()
    query.user_id = user_id
    query.from_datetime = begin_date
    query.to_datetime = end_date
    query.categories = [
        thirdparty_svc.eus.BalanceChangeConst.TRADE_TYPE_PRODUCE, ]
    query.offset = offset
    query.limit = limit
    if status is not None:
        query.statuses = [status, ]
    return query


def get_withdraw_records(restaurant_id, status, begin_date, end_date,
                         offset, limit):
    query = _create_withdraw_records(
        restaurant_id, status, begin_date, end_date, offset, limit)

    with thrift_client('eus') as eus:
        records = eus.walle_query_withdraw_apply(query)
        total_num = eus.walle_count_withdraw_apply(query)

    return records, total_num


def _create_withdraw_records(restaurant_id, status, begin_date, end_date,
                             offset, limit):
    query = thirdparty_svc.eus.TWalleWithdrawApplyQuery()
    query.restaurant_id = restaurant_id
    query.from_created_at = begin_date
    query.to_created_at = end_date
    query.offset = offset
    query.limit = limit
    query.statuses = status

    return query


def get_balance_change(user_id, trade_type, begin_date, end_date,
                       offset, limit):
    query = _create_balance_change(user_id, trade_type,
                                   begin_date, end_date,
                                   offset, limit)
    with thrift_client('eus') as eus:
        records = eus.walle_query_balance_change(query)
        total_num = eus.walle_count_balance_change(query)

    return records, total_num


def _create_balance_change(user_id, trade_type, begin_date, end_date,
                           offset, limit):
    query = thirdparty_svc.eus.TWalleBalanceChangeQuery()
    query.user_id = user_id
    query.from_datetime = begin_date
    query.to_datetime = end_date
    query.offset = offset
    query.limit = limit
    query.trade_types = trade_type
    query.pay_methods = trade_type

    return query


def query_restaurant(city_ids=None, region_ids=None, is_premium=False, is_valid=True, offset=None, limit=None):
    query = _create_restaurant_query(city_ids, region_ids, is_premium,
                                     is_valid, offset, limit)
    with thrift_client('ers') as ers:
        result = ers.search_filter_restaurant(query)
        rst_list = json.loads(result)['hits']
    return rst_list


def _create_restaurant_query(city_ids=None, region_ids=None,
                             is_premium=False, is_valid=True, offset=None, limit=None):
    query = thirdparty_svc.ers.TRestaurantSearchFilterQuery()
    query.city_ids = city_ids
    query.region_ids = region_ids
    query.is_premium = is_premium
    query.is_valid = is_valid
    query.offset = offset
    query.size = limit

    return query


def mget_restaurant_in_region(region_ids):
    with thrift_client('ers') as ers:
        restaurant_ids = ers.mget_restaurant_in_region(region_ids, True)
    return restaurant_ids


def get_restaurant_region_map(rst_ids):
    with thrift_client('ers') as ers:
        region_map = ers.get_restaurant_region_map(rst_ids)
    return region_map


def update_restaurant(rst_id, user_id, **rst_struct):
    rst = thirdparty_svc.ers.TRestaurant()
    for k, v in rst_struct.iteritems():
        if hasattr(rst, k):
            setattr(rst, k, v)
    with thrift_client('ers') as ers:
        ers.update_restaurant(rst_id, user_id, rst)


def search_filter_restaurant(restaurant_ids=None, city_ids=None, region_group_ids=None, region_ids=None, offset=0, size=100):
    query = thirdparty_svc.ers.TRestaurantSearchFilterQuery()
    query.restaurant_ids = restaurant_ids
    query.city_ids = city_ids
    query.region_group_ids = region_group_ids
    query.region_ids = region_ids
    query.offset = offset
    query.size = size
    with thrift_client('ers') as ers:
        result = ers.search_filter_restaurant(query)
        result = json.loads(result)
    return result['hits']


def query_rst_by_area(area, is_valid=1, is_premium=0):
    return inner.query_rst_by_area(area, is_valid, is_premium)
