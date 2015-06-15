#!/usr/bin/env python2
# -*- coding: utf8 -*-

from __future__ import absolute_import, print_function, division

import tablib

from walis.core.response import make_excel_res
from walis.utils.http import Arg, args_parser
from walis.thirdparty import thrift_client
from walis.api.handler.order import order_query_helper


def export():
    args_spec = {
        'query': Arg(unicode, default='{}'),
        'struct': Arg(unicode, default='{}'),
    }
    args = args_parser.parse(args_spec)
    result = order_query_helper.ess_search2(**args)

    orders = result['objects']

    head_line = [
        u"订单号",
        u"订单时间",
        u"用户名",
        u"餐厅名称",
        u"餐厅id",
        # u"订餐电话",
        u"地址",
        u"备注",
        u"订餐内容（菜单）",
        u"总价",
        u"ip",
    ]
    lines = []
    for order in orders:
        with thrift_client('eos') as eos:
            _o = eos.get(int(order['order_id']))
        line_list = [
            order['order_id'],
            order['active_at'],
            order['user_name'],
            order['restaurant_name'],
            unicode(order['restaurant_id']),
            # order['phone'][0],
            order['address'],
            order['description'],
            order['content_text'],
            unicode(order['total']),
            _o.ip
        ]
        line_list = [x.replace('\n', '') for x in line_list]
        lines.append(line_list)

    data = tablib.Dataset(*lines, headers=head_line)

    return make_excel_res(data.xls)
