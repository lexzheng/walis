#!/usr/bin/env python2
# -*- coding: utf8 -*-

from __future__ import division, print_function, absolute_import

from walis.service.region import zone as zone_base

from walis.utils.http import args_to_tobj, Arg, args_parser
from walis.thirdparty import thirdparty_svc


def post():
    zone = args_to_tobj(thirdparty_svc.ers.TZone)
    zone_base.post_or_put(None,zone)
    return ''


def get(pk):
    pk = int(pk)
    result = zone_base.get(pk)
    return result


def put(pk):
    pk = int(pk)
    zone = args_to_tobj(thirdparty_svc.ers.TZone)
    zone_base.post_or_put(pk,zone)
    return ''


def set_is_valid():
    args_spec = {
        'zone_id':Arg(int),
        'zone_ids':Arg(default=[]),
        'is_valid':Arg(bool),
    }
    args = args_parser.parse(args_spec)
    zone_id = args['zone_id']
    zone_ids = args['zone_ids']
    if zone_id:
        zone_ids.append(zone_id)
    zone_base.set_is_valid(zone_ids,args['is_valid'])
    return ''
