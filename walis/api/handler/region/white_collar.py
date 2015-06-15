#! /usr/bin/env python2
# -*- coding:utf-8 -*-

from __future__ import division, print_function, absolute_import

from walis.utils.http import Arg, args_parser
from walis.service.region import white_collar as white_collar_base


def get_building_list_by_area():
    arg_spec = {
        '_area': Arg(list)
    }
    args = args_parser.parse(arg_spec)
    points = args['_area']
    buildings = white_collar_base.query_building_by_points(points)
    building_list = []
    total_population = 0
    for building in buildings:
        building_list.append(building_to_dict(building))
        total_population += int(building.population) if building.population is not None else 0
    return {
        'total_population': total_population,
        'building_list': building_list}


def building_to_dict(building):
    return {
        'building_id': int(building.building_id),
        'building_name': building.building_name,
        'population': int(building.population) if building.population is not None else 0,
        'region_id': int(building.region_id) if building.region_id is not None else None,
        'latitude': float(building.latitude),
        'longitude': float(building.longitude)
        }