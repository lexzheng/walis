#! /usr/bin/env python2
# -*- coding:utf-8 -*-

from __future__ import absolute_import, division, print_function

from walis.utils.http import Arg, args_parser
from walis.service.analytics import trs_query_config as trs_query_cfg_service
from walis.utils.paging import get_paging_params

from walis.utils.time import strptime_to_date


def gets():
    arg_spec = {
        'city_id': Arg(int, allow_missing=True)
    }
    args = args_parser.parse(arg_spec)

    offset, limit = get_paging_params(db_style=True)
    return trs_query_cfg_service.gets(city_id=args.get('city_id'), offset=offset, limit=limit)


def post():
    arg_spec = {
        'city_id': Arg(int, required=True),
        'date_from': Arg(str, required=True),
        'date_end': Arg(str, required=True),
    }
    args = args_parser.parse(arg_spec)
    return trs_query_cfg_service.add_or_update(args['city_id'],
                                               strptime_to_date(args['date_from']),
                                               strptime_to_date(args['date_end']))


def get(city_id):
    return trs_query_cfg_service.get_by_city(city_id)


def put(city_id):
    arg_spec = {
        'date_from': Arg(str, required=True),
        'date_end': Arg(str, required=True),
    }
    args = args_parser.parse(arg_spec)
    return trs_query_cfg_service.add_or_update(city_id,
                                               strptime_to_date(args['date_from']),
                                               strptime_to_date(args['date_end']))
