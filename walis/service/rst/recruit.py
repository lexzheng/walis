#!/usr/bin/env python2
# coding=utf8

from __future__ import absolute_import, division, print_function

from flask.ext.login import current_user
from sqlalchemy import func

from walis.model.walis import DBSession
from walis.model.walis.rst import RestaurantRecruitment
from walis.thirdparty import thrift_client
from walis.utils.model import MAX_QUERY_LIST_SIZE


attr_to_display = [
    'id',
    'restaurant_id',
    'headcount',
    'salary',
    'status',
    'created_at',
    'comment',
    'working_time_start',
    'working_time_end',
]


def get_by_uid(user_id, status=None, offset=None, limit=None):
    q = DBSession().query(RestaurantRecruitment).\
        filter(RestaurantRecruitment.restaurant_id > 0)

    if status is not None:
        q = q.filter(RestaurantRecruitment.status == status)

    if offset is not None:
        q = q.offset(offset)

    if limit is not None:
        q = q.limit(min(limit, MAX_QUERY_LIST_SIZE))

    # if super admin
    if current_user.is_super_admin():
        return q

    with thrift_client('ers') as ers:
        user_struct = ers.get_direct_struct(user_id)

    # if city.admin
    if user_struct.city_ids:
        return q.filter(
            RestaurantRecruitment.city_id.in_(user_struct.city_ids)).all()

    region_ids = []
    # if region_group.admin
    if user_struct.region_group_ids:
        with thrift_client('ers') as ers:
            regions = ers.get_regions_by_region_group_ids(
                user_struct.region_group_ids)
        region_ids = [region.id for region in regions]

    # if region.admin
    if user_struct.region_ids:
        region_ids.extend(user_struct.region_ids)
        region_ids = list(set(region_ids))

    with thrift_client('ers') as ers:
        restaurant_ids = ers.mget_restaurant_in_region(region_ids, True)

    return q.filter(RestaurantRecruitment.restaurant_id.in_(restaurant_ids))


def count_by_uid(user_id, status=None):
    q = DBSession().query(func.count(RestaurantRecruitment.id)).\
        filter(RestaurantRecruitment.restaurant_id > 0)

    if status is not None:
        q = q.filter(RestaurantRecruitment.status == status)

    # if super admin
    if current_user.is_super_admin():
        return q.scalar()

    with thrift_client('ers') as ers:
        user_struct = ers.get_direct_struct(user_id)

    # if city.admin
    if user_struct.city_ids:
        return q.filter(
            RestaurantRecruitment.city_id.in_(user_struct.city_ids)).all().scalar()

    region_ids = []
    # if region_group.admin
    if user_struct.region_group_ids:
        with thrift_client('ers') as ers:
            regions = ers.get_regions_by_region_group_ids(
                user_struct.region_group_ids)
        region_ids = [region.id for region in regions]

    # if region.admin
    if user_struct.region_ids:
        region_ids.extend(user_struct.region_ids)
        region_ids = list(set(region_ids))

    with thrift_client('ers') as ers:
        restaurant_ids = ers.mget_restaurant_in_region(region_ids, True)

    return q.filter(RestaurantRecruitment.restaurant_id.in_(restaurant_ids)).scalar()


def pack_recruits(recruits):
    recruits = [recruit for recruit in recruits if
                recruit.restaurant_id is not None]

    package = {'recruits': []}
    restaurant_ids = list(
        set([recruit.restaurant_id for recruit in recruits]))
    with thrift_client('ers') as ers:
        restaurants = ers.mget(restaurant_ids)

    restaurant_map = {}
    for r in restaurants:
        restaurant_map[r.id] = [r.name, r.phone]

    for index, recruit in enumerate(recruits):
        if recruit.restaurant_id < 0:
            continue
        recruit_map = {}
        for attr in attr_to_display:
            recruit_map[attr] = getattr(recruit, attr)
        recruit_map['name'] = restaurant_map.get(recruit.restaurant_id, ' ')[0]
        recruit_map['phone'] = restaurant_map.get(recruit.restaurant_id, ' ')[-1]
        recruit_map['salary'] = float(recruit_map['salary'])
        package['recruits'].append(recruit_map)

    return package['recruits']
