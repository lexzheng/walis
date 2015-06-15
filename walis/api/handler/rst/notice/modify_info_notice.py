#!/usr/bin/env python2
# -*- coding: utf8 -*-

from __future__ import print_function, absolute_import, division

from flask.ext.login import current_user

from walis.service.rst import director as director_base
from walis.service.region import city as city_base
from walis.utils.paging import get_paging_params
from walis.thirdparty import thrift_client
from walis.utils.http import Arg, args_parser

director_permission = [
    'region_director',
    'city_director',
    'entry_director'
]


def get_direct_struct():
    if current_user.is_super_admin():
        return None, None, None

    with thrift_client('ers') as ers:
        direct_struct = ers.get_direct_struct(current_user.id)

    city_ids = direct_struct.city_ids or None
    region_group_ids = direct_struct.region_group_ids or None
    region_ids = direct_struct.region_ids or None

    if city_ids is None and region_group_ids is None and region_ids is None:
        user_groups = current_user.user_groups
        if not user_groups:
            return [], [], []

        for group in user_groups:
            if group in director_permission:
                return [], [], []

    return city_ids, region_group_ids, region_ids


def get_notifications(args):
    city_ids, region_group_ids, region_ids = get_direct_struct()

    if city_ids == [] and region_ids == [] and region_ids == []:
        return [], 0

    rst_id = args.pop('restaurant_id', None)
    if rst_id is not None:
        args['restaurant_ids'] = [rst_id]

    page_no, page_size = get_paging_params()
    restaurants, total_num = director_base.search_restaurants(
        city_ids=city_ids, region_group_ids=region_group_ids,
        region_ids=region_ids, offset=(page_no - 1) * page_size,
        limit=page_size, **args)

    if not restaurants:
        return [], 0

    restaurant_ids = [r['id'] for r in restaurants]
    city_ids = list(set([r['city_id'] for r in restaurants]))
    notifications = director_base.query_restaurant_director(
        restaurant_ids, [current_user.id, ])
    notification_map = {n.restaurant_id: [n.notice_enabled, n.in_charge]
                        for n in notifications}

    result = []
    city_map = city_base.mget(city_ids, return_map=True)
    for restaurant in restaurants:
        if city_map.get(restaurant['city_id'], None) is None:
            continue

        with thrift_client('ers') as ers:
            try:
                region = ers.get_region_by_restaurant(restaurant['id'])
                region_name = region.name
            except Exception as e:
                region_name = ''
                region_group_name = ''
            else:
                try:
                    region_group_name = ers.get_region_group_by_region(
                        region.id).name
                except Exception as e:
                    region_group_name = ''

        result.append({
            'restaurant_id': restaurant['id'],
            'restaurant_name': restaurant['name'],
            'city_id': restaurant['city_id'],
            'city_name': city_map[restaurant['city_id']].name,
            'region_group_name': region_group_name,
            'region_name': region_name,
            'notice_enabled': notification_map.get(restaurant['id'], [0])[0],
            'in_charge': notification_map.get(restaurant['id'], [None, 0])[1]
        })

    return result, total_num


def set_notification(restaurant_ids, notice_enabled=None, in_charge=None):
    director_base.set_restaurant_director(current_user.id, restaurant_ids,
                                          notice_enabled, in_charge)


def get():
    args = args_parser.parse({
        'restaurant_id': Arg(int, allow_missing=True),
        'is_premium': Arg(int, allow_missing=True),
        'order_mode': Arg(int, allow_missing=True),
        'is_valid': Arg(int, allow_missing=True),
    })
    result, total_num = get_notifications(args)
    return {
        'notifications': result,
        'total_num': total_num
    }


def put():
    args = args_parser.parse({
        'restaurant_ids': Arg([], allow_missing=False),
        'notice_enabled': Arg(int, allow_missing=True),
        'in_charge': Arg(int, allow_missing=True),
    })
    args['restaurant_ids'] = [int(r) for r in args['restaurant_ids']]
    set_notification(**args)
    return ''
