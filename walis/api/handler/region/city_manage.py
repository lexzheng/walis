#!/usr/bin/env python2
# -*- coding: utf8 -*-

from __future__ import division, print_function, absolute_import

from walis.thirdparty import thrift_client, thirdparty_svc
from walis.utils.http import args_parser
from walis.utils.misc import any_to_raw
from walis.service.region import city_manage as city_manager_base


def post():
    args = args_parser.parse_all()
    city_manager_base.post_or_put(None, args)
    return ''


def get(id):
    return city_manager_base.city_filter(city_manager_base.get(id))


def gets():
    city_query = thirdparty_svc.ers.TCityQuery()
    city_query.is_valid = True
    with thrift_client('ers') as ers:
        cities = ers.query_city(city_query)
        cities = any_to_raw(cities)

    city_ids = [city['id'] for city in cities]
    return [city_manager_base.city_filter(city)
            for city in city_manager_base.mget(city_ids)]


def put(pk):
    args = args_parser.parse_all()
    city_manager_base.post_or_put(pk, args)
    return ''
