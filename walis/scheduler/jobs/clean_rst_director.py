#!/usr/bin/env python2
# coding=utf8

from __future__ import absolute_import, division, print_function
import copy
import logging
from collections import defaultdict
from walis.scheduler.jobs import job_deco
from walis.service.rst import (
    director as rst_dir_base,
    restaurant as rst_base,
)
from walis.thirdparty import (
    thirdparty_svc,
    thrift_client,
)
from walis.service.user import user as user_base

log = logging.getLogger('scheduler.rst_director_cleaner')


@job_deco
def clean_rst_director():
    dir_rst_map = get_director_rst_map()

    for user_id, rst_ids in dir_rst_map.items():
        if user_base.is_superadmin(user_id):
            continue

        rst_to_clean = get_rst_not_in_charge(user_id, rst_ids)

        if rst_to_clean:
            log.info('clean {} \'s restaurant: [{}]'.format(
                user_id, rst_to_clean.__repr__()))
            rst_dir_base.rm_restaurant_director(user_id, rst_to_clean)


def get_director_rst_map():
    rv = defaultdict(list)
    offset = 0
    limit = thirdparty_svc.ers.MAX_LIST_SIZE
    while True:
        records = rst_dir_base.query_restaurant_director(
            offset=offset,
            limit=limit
        )
        for record in records:
            rv[record.director_id].append(record.restaurant_id)

        if len(records) < limit:
            break
        offset += limit

    return rv


def get_rst_not_in_charge(user_id, rst_ids):
    region_struct = get_direct_struct(user_id)
    city_ids = set(getattr(region_struct, 'city_ids', []))
    region_ids = set(getattr(region_struct, 'region_ids', []))
    rg_ids = set(getattr(region_struct, 'region_group_ids', []))

    rst_to_clean = copy.copy(rst_ids)

    if city_ids:
        rsts = rst_base.mget(rst_ids)
        rst_to_clean = [rst.id for rst in rsts if rst.city_id not in city_ids]

    if rg_ids:
        with thrift_client('ers') as ers:
            ex_regions = ers.get_regions_by_region_group_ids(rg_ids)
            ex_region_ids = set([r.id for r in ex_regions])
        if ex_region_ids:
            region_ids |= ex_region_ids

    if not region_ids:
        return rst_to_clean

    with thrift_client('ers') as ers:
        rst_region_map = ers.get_restaurant_region_map(rst_to_clean)

    for rst_id, region_id in rst_region_map.items():
        if region_id in region_ids:
            rst_to_clean.remove(rst_id)

    return rst_to_clean


def get_direct_struct(user_id):
    with thrift_client('ers') as ers:
        return ers.get_direct_struct(user_id)


if __name__ == '__main__':
    job()
