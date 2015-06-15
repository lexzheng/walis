#!/usr/bin/env python2
# -*- coding: utf8 -*-

from __future__ import division, print_function, absolute_import

from webargs import Arg

from walis.service.user import user as user_base, hongbao as hongbao_base
from walis.utils.http import args_parser
from walis.utils.paging import get_paging_params


def gets_hongbao():
    args = args_parser.parse({
        'user_id': Arg(int, allow_missing=True),
        'phone': Arg(str, allow_missing=True),
        'sn': Arg(str, allow_missing=True),
        'order_id': Arg(int, allow_missing=True),
        'status': Arg(int, allow_missing=True),
        'source': Arg(str, allow_missing=True),
        'from_datetime': Arg(str, allow_missing=True),
        'to_datetime': Arg(str, allow_missing=True),
    })
    page_no, page_size = get_paging_params()
    args.update(offset=(page_no-1) * page_size, limit=page_size)
    hongbao_list, total_num = hongbao_base.gets_hongbao(args)
    return {
        'hongbao_list': hongbao_list,
        'total_num': total_num
    }


def gets_hongbao_exchange():
    args = args_parser.parse({
        'phone': Arg(str, allow_missing=True),
        'sn': Arg(str,allow_missing=True),
        'status': Arg(int, allow_missing=True),
        'from_datetime': Arg(str, allow_missing=True),
        'to_datetime': Arg(str, allow_missing=True),
    })
    page_no, page_size = get_paging_params()
    args.update(offset=(page_no-1) * page_size, limit=page_size)
    hongbao_exchange_list, total_num = hongbao_base.gets_hongbao_exchange(args)
    return {
        'hongbao_exchange_list': hongbao_exchange_list,
        'total_num': total_num
    }


def gets_hongbao_share():
    args = args_parser.parse({
        'phone': Arg(str, allow_missing=True),
        'order_id': Arg(int, allow_missing=True),
        'status': Arg(int, allow_missing=True),
        'from_datetime': Arg(str, allow_missing=True),
        'to_datetime': Arg(str, allow_missing=True),
    })
    page_no, page_size = get_paging_params()
    args.update(offset=(page_no-1) * page_size, limit=page_size)
    hongbao_share_list, total_num = hongbao_base.gets_hongbao_share(args)
    return {
        'hongbao_share_list': hongbao_share_list,
        'total_num': total_num
    }


def gets_hongbao_grab():
    args = args_parser.parse({
        'phone': Arg(str, allow_missing=True),
        'status': Arg(int, allow_missing=True),
        'from_datetime': Arg(str, allow_missing=True),
        'to_datetime': Arg(str, allow_missing=True),
    })
    page_no, page_size = get_paging_params()
    args.update(offset=(page_no-1) * page_size, limit=page_size)
    hongbao_grab_list, total_num = hongbao_base.gets_hongbao_grab(args)
    return {
        'hongbao_grab_list': hongbao_grab_list,
        'total_num': total_num
    }


def gets_by_userid(user_id):
    results = hongbao_base.gets_by_userid(user_id)
    user = user_base.get_user(user_id)
    return {'hongbaos': results,'user_name': user.username}


def delete(hongbao_sn):
    hongbao_base.delete(hongbao_sn)
    return ''
