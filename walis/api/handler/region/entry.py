#!/usr/bin/env python2
# -*- coding: utf8 -*-

from __future__ import print_function, division, absolute_import

from walis.service.region import entry as entry_base
from walis.utils.http import args_to_tobj, Arg, args_parser

from walis.thirdparty import thirdparty_svc

    
def post():
    entry = args_to_tobj(thirdparty_svc.ers.TEntry)
    entry_base.post_or_put(None,entry)
    return ''


def get(pk):
    pk = int(pk)
    result = entry_base.get(pk)
    return result


def put(pk):
    pk = int(pk)
    entry = args_to_tobj(thirdparty_svc.ers.TEntry)
    entry_base.post_or_put(pk,entry)
    return ''


def set_is_valid():
    args_spec = {
        'entry_id':Arg(int),
        'entry_ids':Arg(default=[]),
        'is_valid':Arg(bool),
    }
    args = args_parser.parse(args_spec)
    entry_id = args['entry_id']
    entry_ids = args['entry_ids']
    if entry_id:
        entry_ids.append(entry_id)
    entry_base.set_is_valid(entry_ids,args['is_valid'])
    return ''
