#!/usr/bin/env python2
# -*- coding: utf8 -*-

from __future__ import absolute_import, print_function, division

from json import loads
from datetime import datetime

from flask import abort, request

from walis.utils.time import timestamp2datetime
from walis.model.walis.activity import (
    PaymentNoticeRecord,
    PaymentNoticeReply,
)
from walis.service.activity.pay_notice.base import (
    update_sms_status,
    save_sms_reply,
)
from walis import config


initial = 0
sending = 1
success = 2
fail = 3
partial_success = 4
timeout = 5

STATUS_MAP = {
    success: PaymentNoticeRecord.STATUS_SUCCESS,
    fail: PaymentNoticeRecord.STATUS_SMS_FAILED,
    timeout: PaymentNoticeRecord.STATUS_SMS_TIMEOUT,
}


def push():
    if not check_hermes_auth():
        abort(403)

    raw_data = request.data or request.json
    if not raw_data:
        abort(400)

    data_map = loads(raw_data)
    n_type = data_map['n_type']
    data = data_map['data']

    if n_type == 0:
        # update sms status and update_time
        sms_task_id = int(data['task_id'])
        try:
            to_status = STATUS_MAP[data['new_status']]
            update_time = datetime.strptime(data['update_time'],
                                            "%Y-%m-%d %H:%M:%S")
        except Exception:
            return ''
        _update_sms_status(sms_task_id, to_status, update_time)

    elif n_type == 1:
        # sms reply
        reply_id = int(data['reply_id'])
        phone_number = data['phone_number']
        message = data['message']
        reply_at = timestamp2datetime(data['timestamp'])
        _save_sms_reply(
            reply_id, phone_number, message, reply_at)

    else:
        abort(400)

    return ''


def check_hermes_auth():
    return config.HERMES['sender_key'] == request.headers.get(
        'X-HERMES-AUTHENTICATE', '')


def _update_sms_status(sms_task_id, to_status, update_time):
    update_sms_status(sms_task_id, to_status, update_time)


def _save_sms_reply(reply_id, phone_number, message, reply_at):
    reply = PaymentNoticeReply.get(reply_id)
    if reply:
        return False

    save_sms_reply(reply_id, phone_number, message, reply_at)
    return True
