#!/usr/bin/env python2
# -*- coding: utf8 -*-

from __future__ import absolute_import, division, print_function

from walis.thirdparty import thirdparty_svc, thrift_client
from walis.utils.misc import any_to_dic, always_list

def get(pk_or_pks):
    with thrift_client('ers') as ers:
        if isinstance(pk_or_pks,(tuple,list)):
            result = ers.mget_entry(pk_or_pks)
        else:
            result = ers.get_entry(pk_or_pks)
    return result


def post_or_put(pk=None,tobj=None):
    with thrift_client('ers') as ers:
        result = ers.save_entry(pk,tobj)
    return result


def set_is_valid(pk_or_pks, is_valid):
    pks = always_list(pk_or_pks)
    for pk in pks:
        entry = thirdparty_svc.ers.TEntry()
        entry.is_valid = is_valid
        entry = any_to_dic(entry)
        post_or_put(pk,entry)
