#!/usr/bin/env python2
# coding=utf8

from __future__ import absolute_import, division, print_function

from flask import request

from walis.thirdparty import thrift_client, thirdparty_svc
from walis.utils.paging import MAX_LIMIT_SIZE


def get(id_or_ids):
    with thrift_client('ers') as ers:
        if isinstance(id_or_ids, (tuple, list)):
            result = ers.mget_restaurant_activity(id_or_ids)
        else:
            result = ers.get_restaurant_activity(id_or_ids)
    return result


mget = get


def post_or_put(activity_id=None):
    if activity_id is not None:
        activity_id = int(activity_id)
    activity_json = request.json
    with thrift_client('ers') as ers_client:
        if activity_id:
            with thrift_client('ers') as ers:
                activity = ers.get_restaurant_activity(activity_id)
            activity = _restaurant_activity_json2ttype(activity_json, activity)
            ers_client.update_restaurant_activity(activity_id, activity)
        else:
            activity = _restaurant_activity_json2ttype(activity_json)
            ers_client.add_restaurant_activity(activity)
        return ''


def get_amount(restaurant_id, activity_id, ):
    with thrift_client('ers') as ers:
        try:
            amount = ers.get_restaurant_activity_subsidy(
                restaurant_id,
                activity_id,
                thirdparty_svc.ers.SubsidyConst.CATEGORY_RESTAURANT_ACTIVITY
            )
        except:
            amount = None


def query(city_ids=None, begin_date=None, end_date=None,
          is_valid=None):
    q = thirdparty_svc.ers.TRestaurantActivityQuery()
    if city_ids:
        q.city_ids = city_ids
    if begin_date:
        q.begin_date = begin_date
    if end_date:
        q.end_date = end_date
    if is_valid:
        q.is_valid = is_valid

    return _query_all_restaurant_activity(q)


def _query_all_restaurant_activity(q):
    result = []
    q.offset = 0
    q.limit = MAX_LIMIT_SIZE

    # while True:
    with thrift_client('ers') as ers:
        result.extend(ers.query_restaurant_activity_for_admin(q))

        # if len(result) < MAX_LIMIT_SIZE:
        # break
        # query.offset += MAX_LIMIT_SIZE

    return result


def _restaurant_activity_json2ttype(restaurant_activity_json,
                                    restaurant_activity=None):
    if not restaurant_activity:
        restaurant_activity = thirdparty_svc.ers.TRestaurantActivity()
    for k, v in restaurant_activity_json.iteritems():
        if k in ['description']:
            continue
        setattr(restaurant_activity, k, v)
    return restaurant_activity