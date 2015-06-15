#!/usr/bin/env python2
# coding=utf8

from __future__ import absolute_import, division, print_function
import json
import logging
from walis.thirdparty import (
    thrift_client,
    thirdparty_svc,
)
from walis.utils.lock import locked

ElemeOrderConst = thirdparty_svc.eos.ElemeOrderConst
OrderRecordConst = thirdparty_svc.eos.OrderRecordConst
EOSUserException = thirdparty_svc.eos.EOSUserException

BOT_ADMIN_ID = 0

# TPD order
SERVICE_CATEGORY_A = 1
SERVICE_CATEGORY_B = 2
SERVICE_CATEGORY_C = 3

log = logging.getLogger(__name__)


@locked(timeout=10)
def auto_process_order(order_id):
    """ beanstalk handler """
    with thrift_client('eos') as eos:
        order = eos.get(order_id)

    if not _is_order_unprocessed(order.id):
        return

    if order.order_mode == ElemeOrderConst.ORDER_MODE_ELEME:
        _process_sms_order(order)
    elif order.order_mode == ElemeOrderConst.ORDER_MODE_TPD_ELEME:
        _process_tpd_order(order)


def _process_sms_order(order):
    try:
        with thrift_client('eos') as eos:
            eos.eleme_process_order(
                order.id,
                ElemeOrderConst.STATUS_PROCESSING,
                OrderRecordConst.PROCESSED_BY_MACHINE,
                OrderRecordConst.PROCESS_GROUP_ADMIN,
                '', 0)
    except EOSUserException:
        log.error('auto process sms order {} failed.'.format(order.id))
        return

    with thrift_client('sms') as sms:
        sms.admin_order_send(order.id, BOT_ADMIN_ID)
    log.info('auto process sms order with id {} [OK].'.format(order.id))


def _process_tpd_order(order):
    if not _check_tpd_order(order):
        return

    try:
        with thrift_client('eos') as eos:
            eos.admin_process_delivery(
                order.id,
                ElemeOrderConst.DELIVERY_STATUS_PROCESSING,
                OrderRecordConst.PROCESSED_BY_MACHINE,
                '')
    except EOSUserException:
        log.error('auto process tpd order {} failed.'.format(order.id))
        return

    log.info('auto process tpd order with id {} [OK].'.format(order.id))


def _check_tpd_order(order):
    if get_service_category(order) != SERVICE_CATEGORY_B:
        return False

    if order.come_from == ElemeOrderConst.COME_FROM_PLATFORM and \
            order.phone_rating != ElemeOrderConst.PHONE_RATING_NORMAL:
        return False

    return True


def get_service_category(order):
    order_attr_d = json.loads(order.attribute_json)
    return order_attr_d.get('service_category')


def _is_order_unprocessed(order_id):
    # check unprocessed
    try:
        with thrift_client('eos') as eos:
            eleme_order = eos.master_get(order_id)

        if eleme_order.status_code != ElemeOrderConst.STATUS_UNPROCESSED:
            log.info('eleme order {} is already processed.'.format(order_id))
            return False
    except EOSUserException:
        log.error('eleme order {} does not exist when auto processing.'.
                  format(order_id))
        return False

    return True
