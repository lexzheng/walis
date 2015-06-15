#!/usr/bin/env python2
# -*- coding: utf8 -*-
from __future__ import absolute_import, division, print_function

import arrow
from flask.ext.login import current_user
from webargs import Arg

from walis.service.order.audit import CustomerServiceUserBase, OrderAuditBase, \
    OrderBase, UserBanBase, PhoneBanBase
from walis.service.rst import restaurant as rst_base
from walis.core.db.mongo import mongo
from walis.utils.http import args_parser


STATUS_DEFAULT = None
STATUS_DOING = 1
STATUS_FINISHED = 2

cs_user_base = CustomerServiceUserBase()
order_base = OrderBase()
user_ban_base = UserBanBase()
order_audit_base = OrderAuditBase()
phone_ban_base = PhoneBanBase()


def get_customer_service_user(pk=None):
    return cs_user_base.get(pk)


def update_customer_service_user(pk):
    args = args_parser.parse_all()
    cs_user_base.post_or_put(pk, args)
    return ''


def get_suspicious_page():
    args_spec = {
        'restaurant_id': Arg(int),
        'date': Arg(unicode,
                    default=arrow.now().replace(days=-1).date().__str__()),
        # 当前使用前端分页
    }
    args = args_parser.parse(args_spec)
    restaurant_id = args['restaurant_id']
    date = args['date']
    auditor_id = current_user.id
    if not restaurant_id:
        auditor_amount = CustomerServiceUserBase.get_auditor_amount()
        if not auditor_amount:
            auditor_amount = 1
        try:
            restaurant_id = order_audit_base.assign_suspicious_orders(
                auditor_id,
                auditor_amount,
                date)
            orders = order_audit_base.get_suspicious_orders(restaurant_id, date)
        except:
            restaurant_id = 1
            orders = []
    else:
        orders = order_audit_base.get_suspicious_orders(restaurant_id, date)

    restaurant = rst_base.get(restaurant_id)

    # restaurant_suspicious
    spec = {
        'restaurant_id': restaurant_id,
    }
    doc = mongo.restaurant.find_one(spec)
    if not doc:
        doc = {
            'is_suspicious': False,
            'suspicious_description': '',
        }
    restaurant.update(doc)

    today_total = \
    order_audit_base.filter_suspicious_orders_amount(None, None, date)[
        'total_count']
    # status0 = order_audit_base.filter_suspicious_orders_amount(auditor_id,None,date)
    # status1 = order_audit_base.filter_suspicious_orders_amount(auditor_id,STATUS_DOING,date)
    status2 = order_audit_base.filter_suspicious_orders_amount(auditor_id,
                                                               STATUS_FINISHED,
                                                               date)
    total_auditor = mongo.dop_user.find({'allow_order_audit': True}).count()
    if not total_auditor:
        total_auditor = 1
    need_process_count = int(today_total // total_auditor)
    status = {
        'default': need_process_count,
        'doing': need_process_count,
        'finished': status2['total_count'],
    }

    return {
        'restaurant': restaurant,
        'orders': orders,
        'status': status,
    }


def finish_suspicious_group_auditing():
    args_spec = {
        'restaurant_id': Arg(int),
        'date': Arg(unicode, ),
    }
    args = args_parser.parse(args_spec)
    return order_audit_base.finish_suspicious_group_auditing(**args)


def filter_suspicious_orders_amount():
    args_spec = {
        'auditor_id': Arg(int),
        'status': Arg(int),
        'date': Arg(unicode),
    }
    args = args_parser.parse(args_spec)
    return order_audit_base.filter_suspicious_orders_amount(**args)


def set_order_valid():
    args_spec = {
        'order_id': Arg(int),
    }
    args = args_parser.parse(args_spec)
    order_id = args['order_id']
    return order_base.set_valid(order_id)


def set_order_invalid():
    args_spec = {
        'order_id': Arg(int),
        'order_ids': Arg(default=[]),
        'reason_type': Arg(int, default=1),
        'remark': Arg(unicode, default=u''),
    }
    args = args_parser.parse(args_spec)
    order_id = args['order_id']
    order_ids = args['order_ids']
    if order_id:
        order_ids.append(order_id)
    reason_type = args['reason_type']
    remark = args['remark']
    for _id in order_ids:
        order_base.set_invalid(_id, reason_type, remark)
    return ''


def set_order_phone_confirmed():
    args_spec = {
        'order_id': Arg(int),
        'confirmed': Arg(bool),
    }
    args = args_parser.parse(args_spec)
    return order_base.set_phone_confirmed(**args)


def set_user_active():
    args_spec = {
        'user_id': Arg(int),
        'is_active': Arg(bool),
        'description': Arg(unicode),
    }
    args = args_parser.parse(args_spec)
    args['admin_user_id'] = current_user.id
    user_ban_base.set_active(**args)
    return ''


def set_phone_banned():
    args_spec = {
        'phone': Arg(unicode),
        'is_banned': Arg(bool),
        'description': Arg(unicode),
    }
    args = args_parser.parse(args_spec)
    args['admin_user_id'] = current_user.id
    phone_ban_base.set_banned(**args)
    return ''


def set_restaurant_suspicious():
    args_spec = {
        'restaurant_id': Arg(int),
        'is_suspicious': Arg(bool),
        'suspicious_description': Arg(unicode),
    }
    args = args_parser.parse(args_spec)
    order_audit_base.set_restaurant_suspicious(**args)
    return ''


def is_auditor(user_id):
    spec = {
        'user_id': user_id,
    }
    doc = mongo.dop_user.find_one(spec)
    if doc is None:
        result = False
    else:
        result = doc['allow_order_audit']
    return {'result': result}
