#!/usr/bin/env python2
# -*- coding: utf8 -*-

from __future__ import print_function, division, absolute_import

from collections import Counter, OrderedDict

from flask import current_app

from walis.service.activity import food_activity as food_act_base
from walis.utils.http import Arg, args_parser
from walis.thirdparty import thrift_client

# todo temp use
def parse_args1():
    args_spec = {
            'restaurant_ids':Arg(default=[]),
            'restaurant_id':Arg(int,default=None),
            'category_ids':Arg(default=[]),
            'category_id':Arg(int,default=None),
            'food_ids':Arg(default=[]),
            'food_id':Arg(int,default=None),
    }
    args = args_parser.parse(args_spec)
    restaurant_ids = args.get('restaurant_ids', [])
    category_ids = args.get('category_ids', [])
    food_ids = args.get('food_ids', [])
    restaurant_id = args.get('restaurant_id', None)
    category_id = args.get('category_id', None)
    food_id = args.get('food_id', None)
    if restaurant_id:
        restaurant_ids.append(restaurant_id)
    if category_id:
        category_ids.append(category_id)
    if food_id:
        food_ids.append(food_id)
    return restaurant_ids, category_ids, food_ids, restaurant_id, category_id, food_id


def which_activity_id(activity_counter):
    if len(activity_counter) > 1:
        current_app.logger.error('more than one activity {}'.format(str(
            activity_counter)))
    most = activity_counter.most_common(1)
    if len(most) == 0:
        return None
    else:
        return most[0][0]


def get_activity_ids(foods):
    with thrift_client('ers') as ers:
        food_ids = list(set([food.id for food in foods]))
        _map = ers.get_weekday_food_activity_id_map_no_cache(food_ids, None)
        _day_activity_counter_map = OrderedDict({day:Counter() for day in
                                                    range(1,8)})
        days = []
        for food_id, day_activity_map in _map.iteritems():
            for day, activity_id in day_activity_map.iteritems():
                days.append(day)
                _day_activity_counter_map[day].update([activity_id])
        day_counter = Counter(days)
        for day,count in day_counter.iteritems():
            if count!=0 and count<len(foods):
                current_app.logger.info('{} not all foods has '
                                        'activity'.format(str(_map)))
        week_activity_ids = []
        for k,v in _day_activity_counter_map.items():
            week_activity_ids.append(which_activity_id(v))
        return week_activity_ids


def week_activity_ids_to_full(activity_ids):
    activities = []
    for _id in activity_ids:
        activity = food_act_base.get(_id)
        activities.append(activity)
    return activities