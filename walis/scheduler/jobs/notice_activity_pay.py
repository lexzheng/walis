#!/usr/bin/env python2
# coding=utf8

from __future__ import absolute_import, division, print_function
from datetime import datetime

from walis.service.activity.pay_notice.base import (
    get_pay_records,
    preprocess_pay_records,
    process_pay_records,
)
from walis.scheduler.jobs import job_deco


@job_deco
def notice_activity_pay():
    """
    notify restaurant owners with successful payment
    """
    # 0. check time
    if not _check_work_time():
        return

    # 1. Get
    pay_records = get_pay_records()
    if not pay_records:
        return

    # 2. Preprocess
    pay_records = preprocess_pay_records(pay_records)

    # 3. Send sms
    process_pay_records(pay_records)


# notice enabled time
NOTIFY_START_HOUR = 8
NOTIFY_END_HOUR = 22


def _check_work_time():
    now = datetime.now()
    if NOTIFY_START_HOUR < now.hour < NOTIFY_END_HOUR:
        return True

    return False
