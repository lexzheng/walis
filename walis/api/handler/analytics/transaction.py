#! /usr/bin/env python2
# -*- coding:utf-8 -*-

from __future__ import absolute_import, division, print_function

from walis.utils.http import Arg, args_parser
from walis.api.handler.region.region import front_area_to_back_area

from walis.service.analytics import transaction as transaction_svc


def query_by_area():
    arg_spec = {
        'city_id': Arg(int),
        '_area': Arg(list)
    }
    args = args_parser.parse(arg_spec)

    points = []
    for point_dic in args.get('_area', []):
        points.append('{lng},{lat}'.format(**point_dic))
    return transaction_svc.get_order_trs_by_area(args['city_id'], points)


def query_by_city(city_id):
    return transaction_svc.count_all_daily_trs_by_city(city_id)
