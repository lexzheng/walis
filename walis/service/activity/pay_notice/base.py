#!/usr/bin/env python2
# coding=utf8

from __future__ import absolute_import, division, print_function
import logging

from walis.core.db.redis import redis
from walis.model.walis import db_commit
from walis.utils.db import redis_sadd, redis_srem
from walis.model.zeus.activity import SubsidyPayRecord
from walis.service.rst import restaurant as rst_base
from walis.service.activity import pay as pay_base
from walis.model.walis.activity import (
    PaymentNoticeRecord,
    PaymentNoticeReply,
)
from .query import (
    get_success_pay_records,
    get_activity_stats,
    get_new_pay_records
)
from .utils import (
    strpdate,
    date_format,
    datetime_format,
    is_mobile_valid,
    sms_content_filter,
    send_pay_notice_sms,
)

PAY_NOTIFY_PENDING_RECORD_IDS = 'pay_notify:pending_record_ids'
PAY_NOTIFY_PROCESS_AT_RECORD_ID = 'pay_notify:process_at_record_id'
log = logging.getLogger('scheduler.pay_notice')


def get_pay_records():
    """ Get new successful pay_records (Max: 400)
    """

    total_success_pays = []
    pending_pays = []

    process_at = get_process_at_record_id()
    # 1. Get new generated pay records
    newly_add_pays = get_new_pay_records(process_at)

    for pay in newly_add_pays:
        if pay[4] == SubsidyPayRecord.STATUS_SUCCESS:
            total_success_pays.append(pay)
        else:
            pending_pays.append(pay)

    # 2. Get old pay records which status changed to success
    total_success_pays.extend(
        get_success_pay_records(get_pending_record_ids())[0:200])

    save_pending_record_ids([r[0] for r in pending_pays])

    return total_success_pays


def preprocess_pay_records(pay_records):
    """ Preprocess : assemble pay_records attributes
    """

    pay_record_infos = []
    for record in pay_records:
        if record[1] is None:
            continue

        restaurant = rst_base.get(record[1])
        act_stats = get_activity_stats(record[0])

        for act_stat in act_stats:
            activity_name = pay_base.get_activity_name(act_stat[0], act_stat[1])
            try:
                pay_record_infos.append({
                    'record_id': record[0],
                    'restaurant_id': record[1],
                    'phone': _get_restaurant_phone(restaurant),
                    'activity_name': activity_name,
                    'first_date': date_format(act_stat[3]),
                    'last_date': date_format(act_stat[4]),
                    'amount': act_stat[5],
                    'total_subsidy': act_stat[2],
                    'process_date': datetime_format(
                        record[3]),
                    'card_num_tail': record[2][-4:],
                    'restaurant_name': sms_content_filter(
                        restaurant.name),
                })
            except Exception as e:
                log.error(e)
                continue
    return pay_record_infos


@db_commit
def process_pay_records(pay_record_infos):
    """ Process : send sms and make data persistence
    """

    process_at = 0
    for pay_record in pay_record_infos:

        sms_task_id = None
        for key, value in pay_record.items():
            pay_record[key] = unicode(value)

        log.info('ready to send payment notification sms to {}.'.
                 format(pay_record['phone']))
        try:
            if is_mobile_valid(pay_record['phone']):
                sms_task_id = send_pay_notice_sms(
                    pay_record['phone'], pay_record)
                status = PaymentNoticeRecord.STATUS_SENDING
            else:
                status = PaymentNoticeRecord.STATUS_MOBILE_INVALID
        except Exception as e:
            log.error(e)
            status = PaymentNoticeRecord.STATUS_SMS_FAILED

        pay_record['first_date'] = strpdate(pay_record['first_date'])
        pay_record['last_date'] = strpdate(pay_record['last_date'])
        pay_record['process_date'] = strpdate(pay_record['process_date'])
        PaymentNoticeRecord.add(status=status,
                                sms_task_id=sms_task_id or -1,
                                **pay_record)

        rm_pending_record_ids(pay_record['record_id'])

        if pay_record['record_id'] > process_at:
            process_at = pay_record['record_id']

    log.info('pay_record_id process at {}'.format(process_at))

    set_process_at_record_id(process_at)


def _get_restaurant_phone(restaurant):
    if restaurant.mobile:
        return restaurant.mobile

    phones = restaurant.phone.lstrip().split(' ')
    return phones[0]


def get_process_at_record_id():
    """
    获取最近一次处理的record_id

    :return:
    """
    record_id = redis.get(PAY_NOTIFY_PROCESS_AT_RECORD_ID)
    if record_id is None:
        return 0

    return int(record_id)


def set_process_at_record_id(record_id):
    """
    设置最近一次处理的record_id

    :return:
    """
    process_at = get_process_at_record_id()

    if int(record_id) > process_at:
        redis.set(PAY_NOTIFY_PROCESS_AT_RECORD_ID, record_id)
        return True

    return False


def get_pending_record_ids():
    """
    获取'已提交'状态的打款记录

    :return:
    """
    process_ids = redis.smembers(PAY_NOTIFY_PENDING_RECORD_IDS)
    if not process_ids:
        return []
    return process_ids


def save_pending_record_ids(record_ids):
    """
    保存'已提交'状态的打款记录

    :param record_ids:
    :return:
    """
    return redis_sadd(PAY_NOTIFY_PENDING_RECORD_IDS, record_ids)


def rm_pending_record_ids(record_ids):
    """
    删除'已提交'状态的打款记录

    :param record_ids:
    :return:
    """
    return redis_srem(PAY_NOTIFY_PENDING_RECORD_IDS, record_ids)


@db_commit
def update_sms_status(sms_task_id, to_status, update_time):
    record = PaymentNoticeRecord.get_by_sms_task_id(sms_task_id)
    if not record:
        log.error('Activity pay record with id {} is not exist.'.
                  format(sms_task_id))
        return

    record.update(to_status, update_time)


@db_commit
def save_sms_reply(reply_id, phone_number, message, create_time):
    PaymentNoticeReply.add(reply_id, phone_number, message, create_time)
