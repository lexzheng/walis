#!/usr/bin/env python2
# -*- coding: utf8 -*-
from __future__ import absolute_import, division, print_function

from flask.ext.login import current_user
from pypinyin import lazy_pinyin, FIRST_LETTER

from walis.thirdparty import thrift_client, thirdparty_svc
from walis.utils.misc import dic_to_tobj, getresult_to_raw, always_list, ttype2dict
from .inner import city as city_base

loop_size = 100


def get_citys(ids):
    ids = list(set(ids))
    citys = city_base.get_citys(ids)
    return [ttype2dict(city) for city in citys]


def get_citys_map(ids):
    citys = get_citys(ids)
    return {city['id']: city for city in citys}


def get(pk_or_pks):
    with thrift_client('ers') as ers:
        if isinstance(pk_or_pks, (tuple, list)):
            pk_or_pks = list(set(pk_or_pks))
            result = ers.mget_city(pk_or_pks)
            # zeus大神在这mget return了个字典-.-你大爷的不一致
            result = result.values()
        else:
            pk_or_pks = int(pk_or_pks)
            result = ers.get_city(pk_or_pks)
    result = getresult_to_raw(result)
    return result


def mget(city_ids, return_map=False):
    with thrift_client('ers') as ers:
        city_map = ers.mget_city(city_ids)

    if return_map:
        return city_map

    return city_map.values()


def post_or_put(pk=None, dic=None):
    tobj = dic_to_tobj(dic, thirdparty_svc.ers.TCity, True)
    if not tobj.pinyin:
        tobj.pinyin = ''.join(lazy_pinyin(tobj.name, errors='ignore'))
    if not tobj.abbr:
        tobj.abbr = ''.join(
            lazy_pinyin(tobj.name, style=FIRST_LETTER, errors='ignore')).upper()
    if not tobj.sort:
        tobj.sort = 2000
    with thrift_client('ers') as ers:
        result = ers.save_city(pk, tobj)
    return result


def set_is_valid(pk_or_pks, is_valid):
    pks = always_list(pk_or_pks)
    for pk in pks:
        city = thirdparty_svc.ers.TCity()
        city.is_valid = is_valid
        post_or_put(pk, city)


def get_city_ids_by_user(user_id=None):
    """
     :return
        1.superadmin [all citiy ids]
        2.city_director [city_ids]
        3.others []
    """
    if user_id is None:
        user_id = current_user.id

    # if super admin
    if current_user.is_super_admin():
        return [city.id for city in get_all_cities()]

    with thrift_client('ers') as ers:
        user_struct = ers.get_direct_struct(user_id)

    # if city.admin
    if user_struct.city_ids:
        return user_struct.city_ids

    # do not have cities
    return []


def get_city_id_name_pairs_by_user():
    # if super admin
    if current_user.is_super_admin():
        return {city.id: city.name for city in get_all_cities()}

    with thrift_client('ers') as ers:
        user_struct = ers.get_direct_struct(current_user.id)

    # if city.admin
    if user_struct.city_ids:
        with thrift_client('ers') as ers:
            cities = ers.mget_city(user_struct.city_ids).values()
        return {city.id: city.name for city in cities}

    # do not have cities
    return []


def get_city_id_name_pairs(city_id_map):
    if not city_id_map:
        return {}

    city_ids = city_id_map.keys()
    index = 0
    cities = []
    while True:
        cur_ids = city_ids[index * loop_size: (index + 1) * loop_size]
        if not cur_ids:
            break
        with thrift_client('ers') as ers:
            cities.extend(ers.mget_city(cur_ids).values())
        index += 1

    return {city.id: city.name for city in cities}


def get_all_cities():
    city_query = thirdparty_svc.ers.TCityQuery()
    city_query.is_valid = True
    with thrift_client('ers') as ers_client:
        return ers_client.query_city(city_query)


def get_city_by_region_group(region_group_id):
    with thrift_client('ers') as ers:
        city = ers.get_city_by_region_group(region_group_id)
    return city


def get_city_by_region(region_id):
    with thrift_client('ers') as ers:
        city = ers.get_city_by_region(region_id)
    return city
