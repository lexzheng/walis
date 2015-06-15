#!/usr/bin/env python2
# -*- coding: utf8 -*-

from __future__ import absolute_import, division, print_function

import json

from flask.ext.login import current_user
from walis.exception.util import raise_auth_exc
from walis.exception.error_code import AUTH_FAILED_ERROR

from walis.utils.misc import dic_fields_process
from walis.api.handler.region import white_collar as white_collar_handler

from walis.utils.http import  args_parser, Arg
from walis.service.region import (
    region as region_base,
    white_collar as white_collar_base,
)

WHITE_COLLAR_TYPE_CODE = 1


def check_region_post(*args, **kwargs):
    if current_user.is_super_admin():
        return True
    args = args_parser.parse_all()
    city_ids = current_user.city_ids
    if args['city_id'] in city_ids:
        return True


def check_region(*args, **kwargs):
    if current_user.is_super_admin():
        return True
    region_id = int(kwargs['pk'])
    if region_id in current_user.region_ids:
        return True
    city_ids = current_user.city_ids
    if city_ids:
        region = region_base.get(region_id)
        if region['city_id'] in city_ids:
            return True


def check_get_regions_by_city_id(*args, **kwargs):
    return True

    
def post():
    dic = args_parser.parse_all()
    if not check_region_post():
        raise_auth_exc(AUTH_FAILED_ERROR)
    dic['area'] = front_area_to_back_area(dic['_area'])
    result = region_base.post(None, dic)
    if dic['type_code'] == WHITE_COLLAR_TYPE_CODE:
        white_collar_base.update_building_region(result, dic['_area'])
    return result


def get(pk):
    pk = int(pk)
    if not check_region(pk=pk):
        raise_auth_exc(AUTH_FAILED_ERROR)
    result = region_base.get(pk)
    dic_fields_process(result, excludes=['has_geohash', 'color'])
    result['_area'] = back_area_to_front_area(result['area'])
    if result['type_code'] == WHITE_COLLAR_TYPE_CODE:
        result['buildings'] = _get_building_by_region_id(result['id'])
    return result


def put(pk):
    pk = int(pk)
    if not check_region(pk=pk):
        raise_auth_exc(AUTH_FAILED_ERROR)
    dic = args_parser.parse_all()
    region = region_base.get(pk)
    dic['area'] = front_area_to_back_area(dic['_area'])
    result = region_base.put(pk, dic)
    if region['type_code'] == WHITE_COLLAR_TYPE_CODE and dic['type_code'] != WHITE_COLLAR_TYPE_CODE:
        white_collar_base.delete_by_region(result)
    if dic['type_code'] == WHITE_COLLAR_TYPE_CODE:
        white_collar_base.update_building_region(result, dic['_area'])
    return result


def delete(pk):
    pk = int(pk)
    if not check_region(pk=pk):
        raise_auth_exc(AUTH_FAILED_ERROR)
    region = region_base.get(pk)
    if region['type_code'] == WHITE_COLLAR_TYPE_CODE:
        white_collar_base.delete_by_region(pk)
    region_base.delete(pk)
    return ''


def get_regions_by_city_id():
    args_spec = {
        'city_id': Arg(int),
    }
    if not check_get_regions_by_city_id():
        raise_auth_exc(AUTH_FAILED_ERROR)
    args = args_parser.parse(args_spec)
    city_id = args['city_id']
    result = region_base.get_regions_by_city_id(city_id)
    for region in result:
        region['_area'] = back_area_to_front_area(region['area'])
        if region['type_code'] == WHITE_COLLAR_TYPE_CODE:
            region['buildings'] = _get_building_by_region_id(region['id'])
        dic_fields_process(region, excludes=['has_geohash', 'color'])
    return result


def back_area_to_front_area(area):
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


def front_area_to_back_area(_area):
    if not _area:
        return ''
    points = []
    for point_dic in _area:
        points.append('{lat},{lng}'.format(**point_dic))
    area_json = [{'point': points}]
    return json.dumps(area_json)


def _get_building_by_region_id(region_id):
    buildings = white_collar_base.get_building_by_region(region_id)
    total_population = 0
    building_list = []
    for building in buildings:
        total_population += int(building.population) if building.population else 0
        building_list.append(white_collar_handler.building_to_dict(building))

    buildings_dict = {
        'total_population': int(total_population),
        'building_list': building_list
    }
    return buildings_dict
