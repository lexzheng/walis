#!/usr/bin/env python2
# -*- coding: utf8 -*-
from __future__ import absolute_import, division, print_function
import json
import datetime
from walis.thirdparty import thrift_client


def restaurant_activity_json2ttype(restaurant_activity_json,
                                   restaurant_activity=None):
    if not restaurant_activity:
        restaurant_activity = thrift_client('ers').TRestaurantActivity()
    for k, v in restaurant_activity_json.iteritems():
        if k in ['description']:
            continue
        setattr(restaurant_activity, k, v)
    return restaurant_activity


class RestaurantActivityMixin(object):
    TYPE_COUPON = 3
    TYPE_NEW_USER_DISCOUNT = 7
    TYPE_EXTRA_DISCOUNT = 100
    TYPE_OLPAYMENT_REDUCE = 101
    TYPE_ADVANCED_DISCOUNT = 102
    TYPE_NEW_USER_DISCOUNT_EXCLUSIVE = 103
    TYPE_ORDER_HONGBAO = 104
    TYPE_JINBAO = 105

    ACTIVITY_TYPE_NAME_MAP = {
        # 抵价券
        TYPE_COUPON: lambda attr: '抵价券{}元'.format(attr),

        # 新用户优惠
        TYPE_NEW_USER_DISCOUNT: lambda attr: '新用户立减{}元'.format(attr),

        # 满立减
        TYPE_EXTRA_DISCOUNT: lambda attr: ','.join(
            ['满{}元减{}元'.format(full, minus) for full, minus in attr.items()]),

        # 不与其他活动同享的新用户优惠
        TYPE_NEW_USER_DISCOUNT_EXCLUSIVE:
            lambda attr: '不与其他活动同享的新用户优惠{}元'.format(attr),

        # 满立减，在线支付再减
        TYPE_ADVANCED_DISCOUNT: lambda attr: ';'.join(
            ['满{}元减{}元，在线支付再减{}元'.format(
                full, minus['0'], minus['1']) for full, minus in
             sorted(attr.items(), lambda x, y: cmp(x[0], y[0]))]),

        # 满X元送红包
        TYPE_ORDER_HONGBAO: lambda attr: ','.join(
            ['满{}元送{}元红包'.format(full, give) for full, give in attr.items()])
        if isinstance(attr, dict) else u'最高抢{}元红包'.format(attr),

        TYPE_JINBAO: '个人专享红包',
    }

    @classmethod
    def get_name(cls, activity):
        if activity.type == RestaurantActivityMixin.TYPE_OLPAYMENT_REDUCE:
            # dirty hack
            return activity.description.split(u',')[0]
        elif activity.type == RestaurantActivityMixin.TYPE_JINBAO:
            return cls.ACTIVITY_TYPE_NAME_MAP[activity.type]
        else:
            attr = json.loads(activity.attribute)
            return cls.ACTIVITY_TYPE_NAME_MAP[activity.type](attr)


get_restaurant_activity_name = RestaurantActivityMixin.get_name


def strptime_to_date(date_str):
    return datetime.datetime.strptime(date_str, '%Y-%m-%d').date()


def get_marketman_relative_restaurant(uid):
    with thrift_client('ers') as ers:
        direct_struct = ers.get_direct_struct(uid)
        region_group_ids = direct_struct.region_group_ids
        _region_ids = []
        region_ids = direct_struct.region_ids
        _region_ids.extend(region_ids)
        if region_group_ids:
            sub_region_ids = ers.get_region_by_region_group_ids(
                region_group_ids)
            _region_ids.extend(sub_region_ids)
        restaurants = ers.walle_mget_restaurant_in_region(_region_ids)
        return restaurants


def get_marketman_relative_city_ids(uid):
    with thrift_client('ers') as ers:
        direct_struct = ers.get_direct_struct(uid)

    city_ids = direct_struct.city_ids
    region_group_ids = direct_struct.region_group_ids
    region_ids = direct_struct.region_ids

    if city_ids:
        city_ids = set(city_ids)
    else:
        city_ids = set()

    if region_group_ids:
        with thrift_client('ers') as ers:
            region_groups = ers.mget_region_group(region_group_ids).values()
        city_ids = city_ids.union([rg.city_id for rg in region_groups])

    if region_ids:
        with thrift_client('ers') as ers:
            regions = ers.mget_region(region_ids).values()
        city_ids = city_ids.union([r.city_id for r in regions])

    return list(city_ids)


def dict2ttype(maps, ttype, keys=None):
    if keys is None:
        keys = maps.keys()
    keys_set = set(keys)

    for key, value in maps.items():
        if key in keys_set:
            setattr(ttype, key, value)
    return ttype


def ttype2dict(ttype, keys=None):
    keys_set = []
    maps = {}
    if keys:
        keys_set = set(keys)

    for key, value in ttype.__dict__.items():
        if keys_set and key not in keys_set:
            continue
        maps[key] = value
    return maps
