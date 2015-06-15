#!/usr/bin/env python2
# -*- coding: utf8 -*-

from __future__ import print_function, division, absolute_import

from collections import defaultdict

from flask.ext.login import current_user

from walis.utils.misc import dic_fields_process
from walis.service.region import city as city_base
from walis.service.region import region as region_service

from walis.utils.http import args_to_tobj, Arg, args_parser
from walis.thirdparty import thrift_client, thirdparty_svc


def post():
    city = args_to_tobj(thirdparty_svc.ers.TCity)
    city_base.post_or_put(None, city)
    return ''


def get(pk):
    pk = int(pk)
    result = city_base.get(pk)
    return result


def put(pk):
    pk = int(pk)
    city = args_to_tobj(thirdparty_svc.ers.TCity)
    city_base.post_or_put(pk, city)
    return ''


def set_is_valid():
    args_spec = {
        'city_id': Arg(int),
        'city_ids': Arg(default=[]),
        'is_valid': Arg(bool)
    }
    args = args_parser.parse(args_spec)
    city_id = args['city_id']
    city_ids = args['city_ids']
    if city_id:
        city_ids.append(city_id)
    city_base.set_is_valid(city_ids, is_valid=args['is_valid'])
    return ''


def get_by_user():
    city_ids = city_base.get_city_id_name_pairs_by_user()
    return {'city_ids': city_ids}


def get_all_valid():
    with thrift_client('ers') as ers:
        q = thirdparty_svc.ers.TCityQuery()
        q.is_valid = True
        result = ers.query_city(q)
    return result


def get_all_by_user_with_alphabet():
    """
    [GET] get all the cities by current-user
    return: first alphabet with city_id and city_name
        e.g. : {b:{1:北京, 12:北宁}, s:{2:上海}, ...}
    """
    city_query = thirdparty_svc.ers.TCityQuery()
    city_query.is_valid = True
    with thrift_client('ers') as ers_client:
        city_list = ers_client.query_city(city_query)

    # if not activity manager, find out his cities.
    if not current_user.has_groups(['activity_manager'],
                                   is_strict=False):
        city_list = filter(lambda city: city.id in (current_user.all_city_ids or []),
                           city_list)

    city_map = defaultdict(list)
    for city in city_list:
        alphabet = city.abbr[0].upper()
        city_map[alphabet].append({city.id: city.name})

    return dict(city_map)


def get_regions_by_city_id(city_id):
    result = region_service.get_regions_by_cityid(city_id)
    for region in result:
        region['_area'] = region_service._format_region_area(region['area'])
        dic_fields_process(region, excludes=['has_geohash', 'created_at', 'color', 'city_id', 'area' ])
    return result
