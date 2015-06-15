# coding=utf8

from __future__ import absolute_import, division, print_function
import json
from walis.thirdparty import (
    thrift_client,
    thirdparty_svc,
)
from walis.utils.data import query_all


def query_restaurants(restaurant_ids=None, is_valid=None, city_ids=None,
                      region_group_ids=None, region_ids=None, region_type=None,
                      is_premium=None, order_mode=None, saas_statuses=None,
                      has_dianping_id=None, offset=None, limit=None):
    query = thirdparty_svc.ers.TRestaurantSearchFilterQuery()
    query.city_ids = city_ids
    query.region_group_ids = region_group_ids
    query.region_ids = region_ids
    query.region_type = region_type
    query.is_valid = is_valid
    query.is_premium = is_premium
    query.order_mode = order_mode
    query.offset = offset
    query.size = limit
    query.order_by_id = 'desc'

    if restaurant_ids is not None:
        query.restaurant_ids = restaurant_ids

    if has_dianping_id is not None:
        query.has_dianping_id = has_dianping_id

    if saas_statuses is not None:
        query.saas_statuses = saas_statuses

    with thrift_client('ers') as ers:
        restaurant_json = ers.search_filter_restaurant(query)

    if not restaurant_json:
        return [], 0

    restaurant_info = json.loads(restaurant_json)
    total_num = restaurant_info['total']
    if total_num == 0:
        return [], 0

    restaurants = [rest['_source'] for rest in restaurant_info['hits']]
    return restaurants


def query_all_rsts(restaurant_ids=None, is_valid=None, city_ids=None,
                   region_group_ids=None, region_ids=None, region_type=None,
                   is_premium=None, order_mode=None, saas_statuses=None,
                   has_dianping_id=None,):
    return query_all(query_restaurants, restaurant_ids=restaurant_ids,
                     is_valid=is_valid, city_ids=city_ids,
                     region_group_ids=region_group_ids, region_ids=region_ids,
                     region_type=region_type, is_premium=is_premium,
                     order_mode=order_mode, saas_statuses=saas_statuses,
                     has_dianping_id=has_dianping_id)


def update_restaurant_region(rst_id, region_id):
    with thrift_client('ers') as ers:
        ers.update_restaurant_region(rst_id, region_id)


def query_rst_by_area(area, is_valid=1, is_premium=0):
    with thrift_client('ers') as ers:
        rst_ids = ers.query_by_area(is_valid, is_premium, area)
    return rst_ids


def query_zeus_bankcard_by_rst_ids(rst_ids):
    with thrift_client('eus') as eus:
        rst_bankcards = eus.mget_bankcard_by_restaurant(rst_ids)
    return rst_bankcards
