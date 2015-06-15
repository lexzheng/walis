#! /usr/bin/env python2
# -*- coding:utf-8 -*-

from walis.service.utils.notice import notifier

SMS_TEMPLATE_ID = "ers_restaurant_banking_change_notice"

def send_bankcard_approve_sms(phone, params):
    return notifier.template_send(
        str(phone),
        SMS_TEMPLATE_ID,
        params)
