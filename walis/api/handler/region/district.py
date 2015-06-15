#!/usr/bin/env python2
# -*- coding: utf8 -*-

from __future__ import division, print_function, absolute_import

from walis.service.region import district as district_base

from walis.utils.http import args_to_tobj, Arg, args_parser
from walis.thirdparty import thirdparty_svc

    
def post():
    district = args_to_tobj(thirdparty_svc.ers.TDistrict)
    district_base.post_or_put(None,district)
    return ''


def get(pk):
    pk = int(pk)
    result = district_base.get(pk)
    return result


def put(pk):
    pk = int(pk)
    district = args_to_tobj(thirdparty_svc.ers.TDistrict)
    district_base.post_or_put(pk,district)
    return ''


def set_is_valid():
    args_spec = {
        'district_id':Arg(int),
        'district_ids':Arg(default=[]),
        'is_valid':Arg(bool),
    }
    args = args_parser.parse(args_spec)
    district_id = args['district_id']
    district_ids = args['district_ids']
    if district_id:
        district_ids.append(district_id)
    district_base.set_is_valid(district_ids,is_valid=args['is_valid'])
    return ''
