#!/usr/bin/env python2
# coding=utf8

from __future__ import absolute_import, division, print_function
import datetime
from walis.service.utils.notice import notifier


SMS_TEMPLATE_ID = 'rizzrack_activity_transfer_notification'


def is_mobile_valid(mobile):
    if not mobile:
        return False

    mobile = mobile.strip()
    if len(mobile) != 11 or mobile[0] != '1':
        return False

    return True


def send_pay_notice_sms(phone, params):
    return notifier.template_send(
        str(phone),
        SMS_TEMPLATE_ID,
        params,
        need_reply=True,
        retry=1)


def sms_content_filter(content):
    if isinstance(content, str):
        content = content.decode('utf-8')
    if not isinstance(content, unicode):
        return ''
    return content.replace(u'【', '[').replace(u'】', ']')


def date_format(date):
    return date.strftime('%Y.%m.%d')


def datetime_format(date_time):
    if not date_time:
        return ''

    return date_time.strftime('%Y.%m.%d')


def strpdate(_str):
    return datetime.datetime.strptime(_str, '%Y.%m.%d').date()


def strpdatetime(_str):
    return datetime.datetime.strptime(_str, '%Y-%m-%d')
