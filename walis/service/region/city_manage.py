#!/usr/bin/env python2
# -*- coding: utf8 -*-

from __future__ import print_function, division, absolute_import

import operator

from walis.thirdparty import thrift_client, thirdparty_svc
from walis.service.region import (
    city as city_base,
    district as district_base,
    zone as zone_base
)
from walis.utils.misc import any_to_raw
from walis.utils.misc import dic_fields_process

from walis.api.handler.region.city import get_all_valid
from walis.exception.error_code import (
    CITY_NAME_EXISTS, DIST_NAME_REDUNDANCE, ZONE_NAME_REDUNDANCE)
from walis.exception.util import (
    raise_user_exc,
)


def post_or_put(pk=None, dic=None):
    if pk is not None:
        pk = int(pk)
    # 处理新建与更新
    new_city = dic
    new_city['is_valid'] = True

    check_same(new_city)

    city_id = city_base.post_or_put(pk, new_city)
    new_city['id'] = city_id

    _districts = new_city.get('_districts', [])
    for _district in _districts:
        _district['is_valid'] = True
        _district['city_id'] = new_city['id']
        _district['id'] = district_base.post_or_put(_district['id'], _district)
        _zones = _district.get('_zones', [])
        for _zone in _zones:
            _zone['is_valid'] = True
            _zone['city_id'] = new_city['id']
            _zone['district_id'] = _district['id']
            _zone['id'] = zone_base.post_or_put(_zone['id'], _zone)
    # 处理删除
    if pk is not None:
        old_city = get(pk)
        old_districts = old_city.get('_districts', [])
        old_district_ids = set([district['id'] for district in old_districts])
        new_districts = new_city.get('_districts', [])
        new_district_ids = set([district['id'] for district in new_districts])
        delete_ids = list(old_district_ids - new_district_ids)

        district_base.set_is_valid(delete_ids, False)

        old_zones = reduce(
            operator.add, [_district.get('_zones', []) for _district in old_districts], [])
        old_zone_ids = set([zone['id'] for zone in old_zones])
        new_zones = reduce(
            operator.add, [_district.get('_zones', []) for _district in new_districts], [])
        new_zone_ids = set([zone['id'] for zone in new_zones])
        delete_ids = list(old_zone_ids - new_zone_ids)
        zone_base.set_is_valid(delete_ids, False)


def check_same(new_city):

    lcdist = new_city.get('_districts', [])
    if len(lcdist) == 0:  # no dist,no ploblem,over
        return 0

    distname = set([item.get('name', '') for item in lcdist])
    if len(distname) < len(lcdist):
        raise_user_exc(DIST_NAME_REDUNDANCE)

    for item in lcdist:
        zones = item.get('_zones', [])
        if len(zones) == 0:
            break
        else:
            zonename = set([item.get('name', '') for item in zones])
            if len(zonename) < len(zones):
                raise_user_exc(ZONE_NAME_REDUNDANCE)


def get(pk_or_pks):
    def sget(pk):
        city = city_base.get(pk)

        district_query = thirdparty_svc.ers.TDistrictQuery()
        district_query.city_id = city['id']
        district_query.is_valid = True
        with thrift_client('ers') as ers:
            districts = ers.query_district(district_query)
            districts = any_to_raw(districts)

        zone_query = thirdparty_svc.ers.TZoneQuery()
        zone_query.city_id = city['id']
        zone_query.is_valid = True
        with thrift_client('ers') as ers:
            zones = ers.query_zone(zone_query)
            zones = any_to_raw(zones)

        [_district.__setitem__('_zones', []) for _district in districts]
        districts_map = {district['id']: district for district in districts}
        for zone in zones:
            district = districts_map.get(zone['district_id'], None)
            if district:
                district['_zones'].append(zone)
        city['_districts'] = districts
        return city
    if isinstance(pk_or_pks, (tuple, list)):
        result = [sget(pk) for pk in pk_or_pks]
    else:
        result = sget(pk_or_pks)
    #result = any_to_dic(result)
    return result

mget = get


def city_filter(city):
    city_fields_include = ['id', 'name', 'sort', 'district_code', 'abbr',
                           'area_code', 'longitude', 'latitude', 'is_map', 'pinyin', '_districts']
    district_fields_include = ['id', 'name', '_zones']
    zone_fields_include = ['id', 'name', '_entries']
    districts = city.get('_districts', [])
    zones = reduce(
        operator.add, [district.get('_zones', []) for district in districts], [])
    dic_fields_process(city, city_fields_include)
    [dic_fields_process(district, district_fields_include)
     for district in districts]
    [dic_fields_process(zone, zone_fields_include) for zone in zones]
    return city


def _diff_process(objs, old_tobjs, base_cls):
    obj_map = {obj.id: obj for obj in objs}
    obj_ids = [obj.id for obj in objs]
    old_tobj_ids = [obj.id for obj in old_tobjs]
    create, update, delete = ids_diff(old_tobj_ids, obj_ids)
    for obj in objs:
        if obj.id is None:
            base_cls.post_or_put(None, obj)
    for _id in create:
        base_cls.post_or_put(None, obj_map[_id])
    for _id in update:
        base_cls.post_or_put(_id, obj_map[_id])
    for _id in delete:
        base_cls.set_is_valid(_id, False)


def ids_diff(old, new):
    old = set(old)
    new = set(new)
    create = new - old
    delete = old - new
    update = new & old
    create = [_id for _id in create if _id is not None]
    delete = [_id for _id in delete if _id is not None]
    update = [_id for _id in update if _id is not None]
    return create, update, delete
