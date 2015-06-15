#!/usr/bin/env python2
# -*- coding: utf8 -*-

from __future__ import absolute_import, division, print_function

from collections import defaultdict

from walis.thirdparty import thirdparty_svc, thrift_client


def get_all():
    region_groups = []

    query = thirdparty_svc.ers.TRegionGroupQuery()
    query.offset = 0
    query.limit = thirdparty_svc.ers.MAX_LIST_SIZE

    while True:
        with thrift_client('ers') as ers:
            result = ers.query_region_group(query)
        region_groups.extend(result)

        if len(result) < thirdparty_svc.ers.MAX_LIST_SIZE:
            break
        query.offset += thirdparty_svc.ers.MAX_LIST_SIZE

    return region_groups


def mget(region_group_ids, return_map=False):
    with thrift_client('ers') as ers:
        region_group_map = ers.mget_region_group(region_group_ids)

    if return_map:
        return region_group_map

    return region_group_map.values()


def get_city_region_group_map(city_ids):
    region_groups = []

    query = thirdparty_svc.ers.TRegionGroupQuery()
    query.city_ids = city_ids
    query.offset = 0
    query.limit = thirdparty_svc.ers.MAX_LIST_SIZE

    while True:
        with thrift_client('ers') as ers:
            result = ers.query_region_group(query)
        region_groups.extend(result)

        if len(result) < thirdparty_svc.ers.MAX_LIST_SIZE:
            break
        query.offset += thirdparty_svc.ers.MAX_LIST_SIZE

    city_region_group_map = defaultdict(list)
    for r_group in region_groups:
        city_region_group_map[r_group.city_id].append(r_group)

    return city_region_group_map


def get_city_region_group_map_by_rg(region_group_ids):
    city_region_group_map = defaultdict(list)
    for rg in mget(region_group_ids):
        city_region_group_map[rg.city_id].append(rg.id)

    return city_region_group_map

def get_region_group_by_region(region_id):
    with thrift_client('ers') as ers:
        try:
            region_group = ers.get_region_group_by_region(region_id)
        except thirdparty_svc.ers.ERSUserException:
            region_group = None
    return region_group

def get_region_group_map_by_region(region_ids):
    with thrift_client('ers') as ers:
        region_group_map = ers.get_region_region_group_map(region_ids)
    return region_group_map
