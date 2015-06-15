#!/usr/bin/env python2
# -*- coding: utf8 -*-
from __future__ import absolute_import, division, print_function
from datetime import date

from flask import request
from flask.ext.login import current_user
from webargs import Arg

from walis.service.activity import rst_activity
from walis.service.activity.utils import get_restaurant_activity_name
from walis.thirdparty import thrift_client, thirdparty_svc
from walis.thirdparty.coffee import coffee
from walis.utils.http import args_parser
from walis.utils.paging import paging
from walis.utils.time import strptime_to_date
from walis.core.auth.map import auth_map_admin


DEFAULT_PAGE_SIZE = 20


def add():
    return rst_activity.post_or_put()


def get(act_id):
    with thrift_client('ers') as ers:
        return ers.get_restaurant_activity(int(act_id))


def update():
    return rst_activity.post_or_put(request.json.get('id'))


def get_by_city_and_period():
    """ [GET] get restaurant-activities by city_ids and
        start-date and end-date """
    rest_activity_query = thirdparty_svc.ers.TRestaurantActivityQuery()
    args_spec = {
        'city_ids': Arg([], allow_missing=True),
        'begin_date': Arg(str, allow_missing=True),
        'end_date': Arg(str, allow_missing=True),
        'overdue': Arg(bool, allow_missing=True),
    }
    args = args_parser.parse(args_spec, request)

    city_ids = args.get('city_ids', [])

    if not coffee.hr_permission.isPermittedToThis(context=current_user.auth_context,
                                                  permission=auth_map_admin['ACT_RST_ADMIN']):
        user_city_ids = current_user.utp_city_ids
        if city_ids:
            city_ids = list(set(city_ids + user_city_ids))
        else:
            city_ids = user_city_ids

    rest_activity_query.city_ids = city_ids
    rest_activity_query.begin_date = args.get('begin_date', None)
    rest_activity_query.end_date = args.get('end_date', None)
    rest_activity_query.limit = 1000
    overdue = args.get('overdue', None)

    with thrift_client('ers') as ers_client:
        restaurant_activities = ers_client.query_restaurant_activity_for_admin(
            rest_activity_query)

    if overdue is not None:
        today = date.today()
        if overdue:
            restaurant_activities = [act for act in restaurant_activities if
                                     _overdue(act, today)]
        else:
            restaurant_activities = [act for act in restaurant_activities if
                                     not _overdue(act, today)]

    total_num = len(restaurant_activities)
    rest_activities_page = paging(restaurant_activities)
    for act in rest_activities_page:
        act.activity_name = get_restaurant_activity_name(act)

    return {
        'restaurant_activities': rest_activities_page,
        'total_num': total_num
    }


def query_restaurant_activity_for_admin(self):
    # todo 效验是否admin
    args_spec = {
        'city_ids': Arg(),
        'begin_date': Arg(str),
        'end_date': Arg(str),
        'offset': Arg(int),
        'limit': Arg(int),
    }
    args = args_parser.parse(args_spec)
    q = thirdparty_svc.ers.TRestaurantActivityQuery()
    for k, v in args.iteritems():
        setattr(q, k, v)
    with thrift_client('ers') as ers:
        result = ers.query_restaurant_activity_for_admin(q)
    return result


def _overdue(act, today):
    end_date = strptime_to_date(act.end_date)
    return today > end_date
