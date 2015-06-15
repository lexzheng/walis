#!/usr/bin/env python2
# coding=utf8

from __future__ import absolute_import, division, print_function

from flask.ext.login import current_user
from webargs import Arg

from walis.service.activity.pay_notice.query import query_sms_send_count
from walis.service.activity.pay_notice.utils import strpdatetime
from walis.model.walis.activity import PaymentNoticeRecord, \
    PaymentNoticeReply
from walis.utils.http import args_parser
from walis.utils.paging import get_paging_params


def get_summery():

    args_spec = {
        'from': Arg(str, allow_missing=True),
        'to': Arg(str, allow_missing=True),
    }
    args = args_parser.parse(args_spec)

    start_date = end_date = None
    if args.get('from'):
        start_date = strpdatetime(args.get('from'))
    if args.get('to'):
        end_date = strpdatetime(args.get('to'))

    total_sms_num = query_sms_send_count(
        start_time=start_date,
        end_time=end_date)

    sending_sms_num = query_sms_send_count(
        status=PaymentNoticeRecord.STATUS_SENDING,
        start_time=start_date,
        end_time=end_date)
    success_sms_num = query_sms_send_count(
        status=PaymentNoticeRecord.STATUS_SUCCESS,
        start_time=start_date,
        end_time=end_date)
    failed_sms_num = query_sms_send_count(
        status=PaymentNoticeRecord.STATUS_SMS_FAILED,
        start_time=start_date,
        end_time=end_date)
    timeout_sms_num = query_sms_send_count(
        status=PaymentNoticeRecord.STATUS_SMS_TIMEOUT,
        start_time=start_date,
        end_time=end_date)
    invalid_sms_num = query_sms_send_count(
        status=PaymentNoticeRecord.STATUS_MOBILE_INVALID,
        start_time=start_date,
        end_time=end_date)

    response_dict = {
        'sending_sms_num': sending_sms_num,
        'success_sms_num': success_sms_num,
        'failed_sms_num': failed_sms_num,
        'timeout_sms_num': timeout_sms_num,
        'invalid_sms_num': invalid_sms_num,
        'total_sms_num': total_sms_num
    }

    if total_sms_num != 0:
        response_dict['success_rate'] = success_sms_num / total_sms_num
        response_dict['unstatused_rate'] = sending_sms_num / total_sms_num
        response_dict['timeout_rate'] = timeout_sms_num / total_sms_num

    return response_dict


def get_sms_info():
    args_spec = {
        'phone': Arg(str, allow_missing=True),
        'restaurant_name': Arg(unicode, allow_missing=True),
        'activity_name': Arg(unicode, allow_missing=True),
        'first_date': Arg(str, allow_missing=True),
        'last_date': Arg(str, allow_missing=True),
        'statuses': Arg(int, multiple=True, allow_missing=True),
    }
    args = args_parser.parse(args_spec)
    page_no, page_size = get_paging_params()
    if page_no and page_size:
        args['offset'] = (page_no - 1) * page_size
        args['limit'] = page_size
    if current_user.restaurant_ids:
        args['restaurant_ids'] = current_user.restaurant_ids

    result = PaymentNoticeRecord.query(**args)
    sms_list = [
        {'phone': r.phone,
         'restaurant_id': r.restaurant_id,
         'restaurant_name': r.restaurant_name,
         'activity_name': r.activity_name,
         'first_date': r.first_date,
         'last_date': r.last_date,
         'amount': r.amount,
         'total_subsidy': float(r.total_subsidy),
         'process_date': r.process_date,
         'card_num_tail': r.card_num_tail,
         'status': r.status,
         'created_at': r.created_at,
         'update_time': r.update_time if r.update_time else r.created_at,
         } for r in result]
    total_num = PaymentNoticeRecord.query_count(**args)

    return {
        'sms_list': sms_list,
        'total_num': total_num
    }


def get_sms_reply():
    args_spec = {
        'phone': Arg(str, allow_missing=True),
    }
    args = args_parser.parse(args_spec)
    page_no, page_size = get_paging_params()
    if page_no and page_size:
        args['offset'] = (page_no - 1) * page_size
        args['limit'] = page_size
    result = PaymentNoticeReply.query(**args)
    reply_list = [
        {'phone': r.phone_number,
         'message': r.message,
         'reply_at': r.reply_at} for r in result]
    total_num = PaymentNoticeReply.query_count(**args)
    return {
        'reply_list': reply_list,
        'total_num': total_num
    }
