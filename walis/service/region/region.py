#!/usr/bin/env python2
# -*- coding: utf8 -*-

from __future__ import absolute_import, division, print_function

import json

from collections import defaultdict

from flask.ext.login import current_user

from walis.utils.misc import any_to_dic, dic_to_tobj, any_to_raw
from walis.thirdparty import thirdparty_svc, thrift_client

from walis.service.region import inner

loop_size = 100

REGION_TYPE_CBD = 1
REGION_TYPE_SCHOOL = 2


def get_all():
    query = thirdparty_svc.ers.TRegionQuery()
    with thrift_client('ers') as ers:
        regions = ers.query_region(query)

    return regions


def mget(region_ids, return_map=False):
    with thrift_client('ers') as ers:
        region_map = ers.mget_region(region_ids)

    if return_map:
        return region_map
    return region_map.values()


def get_region_group_region_map(region_ids):

    region_group_map = get_region_region_group_map(region_ids)

    index = 0
    region_id_map = {}
    while True:
        cur_ids = region_group_map.keys()[index*loop_size: (index+1)*loop_size]
        if not cur_ids:
            break
        with thrift_client('ers') as ers:
            region_id_map.update(ers.mget_region(cur_ids))
        index += 1

    region_group_region_map = defaultdict(list)
    for region_id, region_group_id in region_group_map.items():
        region_group_region_map[region_group_id].append(
            region_id_map[region_id])

    return region_group_region_map


def get_region_region_group_map(region_ids):
    index = 0
    result = {}
    while True:
        cur_region_ids = region_ids[index*loop_size: (index+1)*loop_size]
        if not cur_region_ids:
            break
        with thrift_client('ers') as ers:
            result.update(ers.get_region_region_group_map(cur_region_ids))
        index += 1

    return result


def get(pk):
    with thrift_client('ers') as ers:
        result = ers.get_region(pk)
        result = any_to_dic(result)
    result = any_to_dic(result)
    return result


def post(pk=None, dic=None):
    tobj = dic_to_tobj(dic, thirdparty_svc.ers.TRegion, True)
    with thrift_client('ers') as ers:
        result = ers.save_region(pk, tobj)
    return result


def put(pk, dic=None):
    tobj = dic_to_tobj(dic, thirdparty_svc.ers.TRegion, True)
    with thrift_client('ers') as ers:
        result = ers.save_region(pk, tobj)
    return result


def delete(pk, **kwargs):
    uid = kwargs.get('uid', None) or current_user.id
    with thrift_client('ers') as ers:
        result = ers.remove_region(pk, uid)
        return result


def get_regions_by_city_id(city_id, type_code=None, show_all=None):
    with thrift_client('ers') as ers:
        region_query = thirdparty_svc.ers.TRegionQuery()
        region_query.city_ids = [city_id,]

        if type_code is not None:
            region_query.type_codes = [type_code]

        if show_all is not None:
            region_query.show_all = show_all

        result = ers.query_region(region_query)
        result = any_to_raw(result)
    result = any_to_dic(result)
    return result


def get_region_by_rst(rst_id):
    with thrift_client('ers') as ers:
        try:
            region = ers.get_region_by_restaurant(rst_id)
        except thirdparty_svc.ers.ERSUserException:
            region = None
    return region


def get_region_map_by_rst(rst_ids):
    with thrift_client('ers') as ers:
        region_map = ers.get_restaurant_region_map(rst_ids)
    return region_map


def get_regions_by_cityid(city_id):
    return inner.query_regions(city_ids=[city_id])


def _format_region_area(area):
    if not area:
        return []
    try:
        area_json = json.loads(area)
    except ValueError:
        return []
    area_json = area_json[0]
    points = area_json['point']
    _area = []
    for point in points:
        lat, lng = [float(_) for _ in point.split(',')]
        _area.append({'lat': lat, 'lng': lng})
    return _area