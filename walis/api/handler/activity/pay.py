#!/usr/bin/env python2
# coding=utf8

from __future__ import absolute_import, division, print_function
from collections import defaultdict
import os
import tempfile

from flask import send_file
from webargs import Arg

from walis.utils.format import generate_excel
from walis.utils.http import args_parser
from walis.service.activity import (
    pay as pay_base,
)
from walis.service.rst import restaurant as rst_base
from walis.service.region import city as city_base


def get_pending_status():
    args = args_parser.parse_all()

    audit_enabled = pay_base.get_audit_status()
    activity_payments = pay_base.get_pending_activity_stats(args)

    restaurants = rst_base.mget(
        [pay.get('restaurant_id') for pay in activity_payments])
    rest_map = {r.id: r.name for r in restaurants}
    for index, payments in enumerate(activity_payments):
        payments['restaurant_name'] = rest_map.get(
            payments['restaurant_id'], u'')

    activity_payments = pay_base.set_activity_names(activity_payments)
    activity_payments = pay_base.set_bank_card_exist_or_not(
        activity_payments)

    final_payments = {}
    for act_pay in activity_payments:
        payment = final_payments.get(act_pay['restaurant_id'])
        if payment:
            payment['activities'].append({
                'activity_name': act_pay['activity_name'],
                'activity_id': act_pay['activity_id'],
                'activity_category_id': act_pay['activity_category_id'],
                'first_date': act_pay['first_date'],
                'last_date': act_pay['last_date'],
                'quantity': act_pay['quantity'],
                'total_subsidy': act_pay['total_subsidy']
            })
        else:
            act_pay['activities'] = [{
                'activity_name': act_pay['activity_name'],
                'activity_id': act_pay['activity_id'],
                'activity_category_id': act_pay['activity_category_id'],
                'first_date': act_pay['first_date'],
                'last_date': act_pay['last_date'],
                'quantity': act_pay['quantity'],
                'total_subsidy': act_pay['total_subsidy']}]
            act_pay.__delitem__('activity_id')
            act_pay.__delitem__('activity_category_id')
            act_pay.__delitem__('activity_name')
            act_pay.__delitem__('first_date')
            act_pay.__delitem__('last_date')
            act_pay.__delitem__('quantity')
            act_pay.__delitem__('total_subsidy')
            final_payments[act_pay['restaurant_id']] = act_pay

    return {
        'payments': final_payments.values(),
        'audit_enabled': audit_enabled,
        'total_num': 0
    }


def get_all_status():
    args = args_parser.parse_all()

    activity_payments = pay_base.get_all_activity_stats(args)

    # set restaurant name
    restaurants = rst_base.mget(
        [pay.get('restaurant_id') for pay in activity_payments])
    for index, payments in enumerate(activity_payments):
        payments['restaurant_name'] = restaurants[index].name
        if not restaurants[index].is_valid:
            payments['restaurant_name'] += u'（餐厅已无效）'

    activity_payments = pay_base.set_activity_names(activity_payments)
    activity_payments = pay_base.set_bank_card_exist_or_not(
        activity_payments)
    visible_city_ids = city_base.get_city_id_name_pairs_by_user()

    no_subsidy_indication, pay_fail_indication = pay_base.\
        get_failed_status_indication(args)

    return {
        'payments': activity_payments,
        'city_ids': visible_city_ids,
        'no_subsidy_indication': no_subsidy_indication,
        'pay_fail_indication': pay_fail_indication,
        'total_num': 0
    }


def export_excel():
    args = args_parser.parse_all()

    activity_payments = pay_base.get_all_activity_stats(args)

    # set restaurant name
    restaurants = rst_base.mget(
        [pay.get('restaurant_id') for pay in activity_payments])
    for index, payments in enumerate(activity_payments):
        payments['restaurant_name'] = restaurants[index].name

    activity_payments = pay_base.set_activity_names(activity_payments)
    activity_payments = pay_base.set_act_category_names(activity_payments)

    temp_file = tempfile.TemporaryFile()
    workbook = generate_excel(activity_payments, u'活动打款审核记录',
                              (('restaurant_id', u'餐厅id'),
                               ('restaurant_name', u'餐厅名称'),
                               ('activity_name', u'活动名称'),
                               ('activity_id', u'活动id'),
                               ('first_date', u'起始日期'),
                               ('last_date', u'结束日期'),
                               ('activity_category_id', u'活动类别'),
                               ('total_subsidy', u'打款总额'),
                               ('quantity', u'数量'),))
    workbook.save(temp_file)

    temp_file.seek(0)
    response = send_file(temp_file, as_attachment=True,
                         mimetype='application/vnd.ms-excel',
                         attachment_filename='活动打款审核记录.xls',
                         add_etags=False)

    temp_file.seek(0, os.SEEK_END)
    size = temp_file.tell()
    temp_file.seek(0)
    response.headers.extend({
        'Content-Length': size,
        'Cache-Control': 'no-cache'
    })
    return response


def approval_payment():
    payment_dict = _get_approval_reject_args()
    pay_base.approval_payment(payment_dict)
    return ''


def reject_payment():
    payment_dict = _get_approval_reject_args()
    pay_base.reject_payment(payment_dict)
    return ''


def _get_approval_reject_args():
    args_spec = {'payments': Arg([]), }
    args = args_parser.parse(args_spec)
    payments = args.get('payments')

    payment_dict = defaultdict(list)
    for payment in payments:
        activity_id = str(payment['activity_id'])
        category_id = str(payment['activity_category_id'])
        restaurant_id = payment['restaurant_id']

        payment_dict['_'.join((activity_id, category_id))].append(restaurant_id)

    return dict(payment_dict)


def _get_batch_approval_reject_args():
    args_spec = {'restaurant_ids': Arg([])}
    args = args_parser.parse(args_spec)
    restaurant_ids = args['restaurant_ids']
    return restaurant_ids
