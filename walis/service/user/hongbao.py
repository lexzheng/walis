#!/usr/bin/env python2
# -*- coding: utf8 -*-

from __future__ import division, absolute_import, print_function

from walis.utils.paging import get_paging_params
from walis.thirdparty import thrift_client, thirdparty_svc
from walis.utils.misc import ttype2dict
from walis.utils.time import get_timestamp_by_start_date,get_timestamp_by_end_date,timestamp2datetime


STATUS_UNUSED = 0
STATUS_USED = 1
STATUS_ORDER_CANCEL = 2
STATUS_INVALID = 3

def get_hongbao_query(args):
    query = thirdparty_svc.eus.TWalleHongbaoQuery()
    query.user_id = args.get('user_id', None)
    query.phone = args.get('phone', None)
    query.sn = args.get('sn', None)
    query.order_id = args.get('order_id', None)
    query.status = args.get('status', None)
    query.source = args.get('source', None)
    query.from_datetime = get_timestamp_by_start_date(args.get('from_datetime', None))
    query.to_datetime = get_timestamp_by_end_date(args.get('to_datetime', None))
    return query


def gets_hongbao(args):
    query = get_hongbao_query(args)
    with thrift_client('eus') as eus:
        count = eus.walle_count_user_hongbao(query)
        query.offset = args.get('offset', None)
        query.limit = args.get('limit', None)
        results = eus.walle_query_user_hongbao(query)
    hongbaos = []
    user_hongbao_keys = ['hongbao_sn','created_at','amount','sum_condition','begin_date','end_date','status','name','username','phone','order_id']
    for result in results:
        hongbao_dict = ttype2dict(result, keys=user_hongbao_keys)
        hongbao_dict['order_id'] = str(hongbao_dict['order_id'])
        hongbao_dict['created_at'] = timestamp2datetime(hongbao_dict['created_at'])
        hongbaos.append(hongbao_dict)
    return hongbaos,count


def gets_hongbao_exchange(args):
    query = get_hongbao_query(args)
    with thrift_client('eus') as eus:
        count = eus.walle_count_hongbao_exchange(query)
        query.offset = args.get('offset', None)
        query.limit = args.get('limit', None)
        results = eus.walle_query_hongbao_exchange(query)
    hongbao_exchanges = []
    hongbao_exchange_keys = ['exchange','amount','sum_condition','created_at','end_date','status','hongbao_sn','phone']
    for hongbao_exchange in results:
        hongbao_exchange_dict = ttype2dict(hongbao_exchange, keys=hongbao_exchange_keys)
        hongbao_exchange_dict['created_at'] = timestamp2datetime(hongbao_exchange_dict['created_at'])
        hongbao_exchanges.append(hongbao_exchange_dict)
    return hongbao_exchanges,count


def gets_hongbao_share(args):
    query = get_hongbao_query(args)
    with thrift_client('eus') as eus:
        count = eus.walle_count_hongbao_group(query)
        query.offset = args.get('offset', None)
        query.limit = args.get('limit', None)
        results = eus.walle_query_hongbao_group(query)
    hongbao_shares = []
    hongbao_share_keys = ['order_id','phone','total_count','used_count','status','source','updated_at']
    for hongbao_share in results:
        hongbao_share = ttype2dict(hongbao_share, keys=hongbao_share_keys)
        hongbao_share['order_id'] = str(hongbao_share['order_id'])
        hongbao_share['updated_at'] = timestamp2datetime(hongbao_share['updated_at'])
        hongbao_shares.append(hongbao_share)
    return hongbao_shares,count


def gets_hongbao_grab(args):
    query = get_hongbao_query(args)
    with thrift_client('eus') as eus:
        count = eus.walle_count_weixin_hongbao_record(query)
        query.offset = args.get('offset', None)
        query.limit = args.get('limit', None)
        results = eus.walle_query_weixin_hongbao_record(query)
    hongbao_grab_list = []
    hongbao_grab_keys = ['id','sn','group_sn','sns_uid','sns_username','sns_avatar','phone','amount','sum_condition','status','name','source','created_at','updated_at','user_id']
    for hongbao_grab in results:
        hongbao_grab = ttype2dict(hongbao_grab, keys=hongbao_grab_keys)
        hongbao_grab['created_at'] = timestamp2datetime(hongbao_grab['created_at'])
        hongbao_grab['updated_at'] = timestamp2datetime(hongbao_grab['updated_at'])
        hongbao_grab_list.append(hongbao_grab)
    return hongbao_grab_list,count


def gets_by_userid(user_id):
    page_no, page_size = get_paging_params()
    t_query = thirdparty_svc.eus.THongbaoQuery()
    t_query.user_id = user_id
    t_query.statuses = [STATUS_UNUSED, STATUS_USED]
    t_query.offset = (page_no - 1) * page_size
    t_query.limit = page_size

    with thrift_client('eus') as eus:
        hongbaos = eus.query_hongbao(t_query)

    results = []
    disp_keys = ['sn', 'sum_condition', 'begin_date', 'end_date', 'amount','used_amount']
    for hongbao in hongbaos:
        hongbao_dict = ttype2dict(hongbao, keys=disp_keys)

        hongbao_dict['left_amount'] =\
            hongbao_dict['amount'] - hongbao_dict['used_amount']

        if hongbao_dict['left_amount'] != 0:
            results.append(hongbao_dict)

    return results


def delete(hongbao_sn):
    with thrift_client('eus') as eus:
        eus.invalid_hongbao(hongbao_sn)