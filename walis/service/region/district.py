#!/usr/bin/env python2
# -*- coding: utf8 -*-

from __future__ import absolute_import, division, print_function

from walis.thirdparty import thrift_client, thirdparty_svc
from walis.utils.misc import always_list, any_to_dic, dic_to_tobj


def get(pk_or_pks):
    """
    神zues-.-这个接口开了get不开mget-.-
    """
    with thrift_client('ers') as ers:
        if isinstance(pk_or_pks,(tuple,list)):
            result = map(ers.get_district,[pk for pk in pk_or_pks])
        else:
            result = ers.get_district(pk_or_pks)
    result = any_to_dic(result)
    return result


def post_or_put(pk=None, dic=None):
    tobj = dic_to_tobj(dic,thirdparty_svc.ers.TDistrict,True)
    with thrift_client('ers') as ers:
        result = ers.save_district(pk,tobj)
    return result


def set_is_valid(pk_or_pks, is_valid):
    pks = always_list(pk_or_pks)
    for pk in pks:
        district = thirdparty_svc.ers.TDistrict()
        district.is_valid = is_valid
        district = any_to_dic(district)
        post_or_put(pk, district)


def zers_query_district(**kwargs):
    with thrift_client('ers') as ers:
        q = thirdparty_svc.ers.TDistrictQuery()
        for k,v in kwargs:
            if k in q.__dict__.keys():
                setattr(q,k,v)
        result = ers.query_district(q)
        return result
