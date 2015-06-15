#!/usr/bin/env python2
# coding=utf8

from __future__ import absolute_import, division, print_function

from walis.service.rst import director as rst_dir_base


def get_restaurant_director_ids(restaurant_id):
    records = rst_dir_base.query_restaurant_director(
        restaurant_ids=[restaurant_id])

    return [r.director_id for r in records if r.in_charge == 1]


def change_director_region(user_id, old_region, new_region):
    city_diff = _diff(old_region.city_ids, new_region.city_ids)
    region_group_diff = _diff(old_region.region_group_ids,
                              new_region.region_group_ids)
    region_diff = _diff(old_region.region_ids, new_region.region_ids)

    query_dict = {}
    if city_diff:
        query_dict['city_ids'] = city_diff
    if region_group_diff:
        query_dict['region_group_ids'] = region_group_diff
    if region_diff:
        query_dict['region_ids'] = region_diff

    if not query_dict:
        return

    dir_records = rst_dir_base.query_restaurant_director(
        director_ids=[user_id],
        offset=0, limit=1000)
    dir_rst_ids = [d.restaurant_id for d in dir_records]
    query_dict['restaurant_ids'] = dir_rst_ids
    query_dict['offset'] = 0
    query_dict['limit'] = 1000

    restaurants = rst_dir_base.search_restaurants(**query_dict)
    rst_ids = [r['id'] for r in restaurants[0]]
    rst_dir_base.rm_restaurant_director(user_id, rst_ids)


def set_bd_restaurant_director(user_id, rst_ids, notice_enabled=True, in_charge=True):
    old_rst_dir = rst_dir_base\
        .query_restaurant_director(director_ids=[user_id,], offset=0, limit=1000)
    new_rst_dir = rst_dir_base\
        .query_restaurant_director(restaurant_ids=rst_ids, offset=0, limit=1000)

    old_rst_ids = [rst_dir.restaurant_id for rst_dir in old_rst_dir]
    new_rst_ids = [rst_dir.restaurant_id for rst_dir in new_rst_dir]
    rm_rst_ids = _diff(old_rst_ids, new_rst_ids)
    add_rst_ids = _diff(new_rst_ids, old_rst_ids)

    rst_dir_base.rm_restaurant_director(user_id, rm_rst_ids)
    rst_dir_base.set_restaurant_director(user_id, add_rst_ids, notice_enabled, in_charge)


def _diff(list1, list2):
    """ return stuff in list1 but not in list2
    """
    if not list1 or not list2:
        return list1

    return set(list1) - set(list2)
