#!/usr/bin/env python2
# -*- coding: utf8 -*-

from __future__ import print_function, division, absolute_import

import json

from walis.thirdparty import thrift_client, thirdparty_svc
from walis.exception.util import raise_zeus_exc
from walis.exception.error_code import ZEUS_DATABASE_ERROR


def search_restaurants(restaurant_ids=None, is_valid=None,
                       city_ids=None, region_group_ids=None,
                       region_ids=None, is_premium=None,
                       order_mode=None, offset=None, limit=None):
    query = thirdparty_svc.ers.TRestaurantSearchFilterQuery()
    query.city_ids = city_ids
    query.region_group_ids = region_group_ids
    query.region_ids = region_ids
    query.is_valid = is_valid
    query.is_premium = is_premium
    query.order_mode = order_mode
    query.offset = offset
    query.size = limit
    query.order_by_id = 'desc'

    if restaurant_ids is not None:
        query.restaurant_ids = restaurant_ids

    with thrift_client('ers') as ers:
        restaurant_json = ers.search_filter_restaurant(query)

    if not restaurant_json:
        raise_zeus_exc(ZEUS_DATABASE_ERROR)

    restaurant_info = json.loads(restaurant_json)
    total_num = restaurant_info['total']
    if total_num == 0:
        return [], 0

    restaurants = [rest['_source'] for rest in restaurant_info['hits']]
    return restaurants, total_num


def query_restaurant_director(restaurant_ids=None, director_ids=None,
                              notice_enabled=None, in_charge=None,
                              offset=None, limit=None):
    query = thirdparty_svc.ers.TRestaurantDirectorQuery()
    query.restaurant_ids = restaurant_ids
    query.director_ids = director_ids
    query.notice_enabled = notice_enabled
    query.in_charge = in_charge
    query.offset = offset
    query.limit = limit
    with thrift_client('ers') as ers:
        return ers.query_restaurant_director(query)


def set_restaurant_director(director_id, restaurant_ids,
                            notice_enabled, in_charge):
    with thrift_client('ers') as ers:
        return ers.set_restaurant_director(
            director_id, restaurant_ids, notice_enabled, in_charge)


def rm_restaurant_director(director_id, restaurant_ids):
    with thrift_client('ers') as ers:
        return ers.rm_restaurant_director(director_id, restaurant_ids)
