#!/usr/bin/env python2
# coding=utf8

from __future__ import absolute_import, division, print_function
from walis.thirdparty import (
    thrift_client,
    thirdparty_svc,
)


def get(id_or_ids):
    with thrift_client('ers') as ers:
        if isinstance(id_or_ids, (tuple, list)):
            result = ers.mget_food_activity(id_or_ids)
        else:
            result = ers.get_food_activity(id_or_ids)
    return result


mget = get


def get_amount(restaurant_id, activity_id):
    with thrift_client('ers') as ers:
        try:
            return ers.get_restaurant_activity_subsidy(
                restaurant_id,
                activity_id,
                thirdparty_svc.ers.SubsidyConst.CATEGORY_FOOD_ACTIVITY
            )
        except:
            return None


def query(city_ids=None, begin_date=None, end_date=None,
          is_valid=None):
    query = thirdparty_svc.ers.TFoodActivityQuery()
    if city_ids:
        query.city_ids = city_ids
    if begin_date:
        query.begin_date = begin_date
    if end_date:
        query.end_date = end_date
    if is_valid:
        query.is_valid = is_valid

    with thrift_client('ers') as ers:
        query.offset = 0
        query.limit = thirdparty_svc.ers.MAX_LIST_SIZE
        return ers.query_food_activity(query)
