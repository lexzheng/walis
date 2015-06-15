#!/usr/bin/env python2
# -*- coding: utf8 -*-

from walis.thirdparty import thrift_client, thirdparty_svc

def get_arbitrating_orders():
    offset = 0
    total_orders = []

    while True:
        query = _create_order_query(offset)
        with thrift_client('eos') as eos:
            orders = eos.query_order(query)

        if not orders:
            break

        offset += len(orders)
        total_orders.extend(orders)

    order_ids = [o.id for o in total_orders]

    content = ''
    for _id in order_ids:
        content = '<br>'.join((content, str(_id)))
    return content

def _create_order_query(offset):
    query = thirdparty_svc.eos.TOrderQuery()
    query.refund_statuses = (2, 4, )
    query.statuses = (3, )
    query.limit = 200
    query.offset = offset
    return query
