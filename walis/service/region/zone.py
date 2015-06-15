#!/usr/bin/env python2
# -*- coding: utf8 -*-

from __future__ import absolute_import, division, print_function

from walis.thirdparty import thirdparty_svc, thrift_client
from walis.utils.misc import always_list, any_to_dic, dic_to_tobj

def get(pk_or_pks):
    with thrift_client('ers') as ers:
        if isinstance(pk_or_pks,(tuple,list)):
            result = map(ers.get_zone,[pk for pk in pk_or_pks])
        else:
            result = ers.get_zone(pk_or_pks)
    result = any_to_dic(result)
    return result


def post_or_put(pk=None,dic=None):
    tobj = dic_to_tobj(dic,thirdparty_svc.ers.TZone)
    with thrift_client('ers') as ers:
        result = ers.save_zone(pk,tobj)
    return result


def set_is_valid(pk_or_pks, is_valid):
    pks = always_list(pk_or_pks)
    for pk in pks:
        zone = thirdparty_svc.ers.TZone()
        zone.is_valid = is_valid
        zone = any_to_dic(zone)
        post_or_put(pk,zone)
