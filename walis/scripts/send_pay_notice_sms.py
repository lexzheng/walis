#!/usr/bin/env python2
# coding=utf8

from __future__ import absolute_import, division, print_function
from walis.service.activity.pay_notice.utils import send_pay_notice_sms, strpdate
from walis.model.walis.activity import PaymentNoticeRecord

pay_record = {
    'record_id': 1910276,
    'restaurant_id': 139650,
    'phone': '15836915808',
    'activity_name': u'不与其他活动同享的新用户优惠5元',
    'first_date': '01.03',
    'last_date': '01.03',
    'amount': 2,
    'total_subsidy': 10,
    'process_date': '01.10',
    'card_num_tail': '8705',
    'restaurant_name': u'润仟祥黄焖鸡米饭',
}


def send_one():
    sms_task_id = -1
    try:
        sms_task_id = send_pay_notice_sms(pay_record['phone'], pay_record)
        status = PaymentNoticeRecord.STATUS_SENDING
    except Exception:
        status = PaymentNoticeRecord.STATUS_SMS_FAILED

    pay_record['first_date'] = strpdate(pay_record['first_date'])
    pay_record['last_date'] = strpdate(pay_record['last_date'])
    pay_record['process_date'] = strpdate(pay_record['process_date'])
    PaymentNoticeRecord.add(pay_record['record_id'],
                            status=status,
                            sms_task_id=sms_task_id,
                            **pay_record)


if __name__ == '__main__':
    send_one()