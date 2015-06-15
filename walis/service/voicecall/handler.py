#!/usr/bin/env python2
# coding=utf8

from __future__ import absolute_import, division, print_function

import json
import logging
from datetime import datetime
from collections import defaultdict

import requests

from .utils import get_rst_takeout_phone
from walis.service.voicecall.settings import call_settings, voicecall_url
from walis.model import db_commit
from walis.model.walis.voicecall import VoiceOrder, VoiceCall
from walis.thirdparty import (
    thirdparty_svc,
    thrift_client,
)
from walis.exception.util import raise_user_exc
from walis.exception.error_code import VOICE_CALL_NOT_FOUND


log = logging.getLogger(__name__)

SUBMIT_FAILED = 0
SUBMIT_SUCCESS = 1


@db_commit
def voice_order_handler(orders):
    """ save voice-call and voice-order """
    order_groups = defaultdict(list)
    for order in orders:
        order_groups[order.restaurant_id].append(order)

    for restaurant_id, orders in order_groups.items():
        orders = _validate_order(orders)
        if not orders:
            continue

        with thrift_client('ers') as ers:
            restaurant = ers.get(restaurant_id)
        restaurant_phone = get_rst_takeout_phone(restaurant)
        if not restaurant_phone:
            continue

        voice_call = VoiceCall.add(restaurant_id=restaurant_id,
                                   call_status=VoiceCall.STATUS_NOT_DIAL,
                                   created_at=datetime.now(),
                                   phone=restaurant_phone,
                                   flush=True)
        for order in orders:
            VoiceOrder.add(order_id=order.id,
                           status_code=order.status_code,
                           sequence_number=order.restaurant_number,
                           created_at=datetime.fromtimestamp(order.created_at),
                           call_id=voice_call.id)
        log.info('voice order received with restaurant_id [{}], call_id [{}]'.
                 format(restaurant_id, voice_call.id))


def _validate_order(orders):
    order_results = []
    for order in orders:
        if not VoiceOrder.get_by_order_id(order.id):
            order_results.append(order)

    return order_results


def _generate_call_params(voice_call, voice_orders):
    phone = str(voice_call.phone)
    if '-' in phone:
        phone = phone.replace('-', '')

    call_params = {'userField': voice_call.id,
                   'orderNumber': len(voice_orders),
                   'customerNumber': phone}
    param_name = ['orderNumber']
    param_types = ['1']
    for index, order in enumerate(voice_orders):
        # (order_id, order_index, order_msg)

        id_key = "orderId{}".format(index + 1)
        index_key = "orderIndex{}".format(index + 1)
        msg_key = "orderMessage{}".format(index + 1)

        param_name.append(','.join([id_key, index_key, msg_key]))
        param_types.append('1,1,2')

        call_params[id_key] = order.order_id
        call_params[index_key] = order.sequence_number
        call_params[msg_key] = "暂无信息"

    call_params["paramNames"] = ','.join(param_name)
    call_params["paramTypes"] = ','.join(param_types)
    call_params.update(call_settings)
    log.debug('call params is %s' % call_params.items())
    return call_params


def _send_call(call_params):
    response = requests.get(voicecall_url, params=call_params, timeout=20)
    call_result = json.loads(response.text)
    result = int(call_result.get('result'))

    submit_status_map = {
        SUBMIT_FAILED: VoiceCall.STATUS_EXCEED_CALL_LIMIT,
        SUBMIT_SUCCESS: VoiceCall.STATUS_DIALING
    }
    log.info('voice call is already sent to {} with status {}'.format(
        call_params.get('customerNumber'), submit_status_map[result]))
    return submit_status_map[result]


@db_commit
def voice_call_handler(call_id):
    """ handle only one call each time. """
    STATUS_PROCESSING = thirdparty_svc.eos.ORDER_STATUS.STATUS_PROCESSING
    voice_call = VoiceCall.get(call_id)
    if not voice_call:
        raise_user_exc(VOICE_CALL_NOT_FOUND, call_id=call_id)
    voice_orders = VoiceOrder.get_by_call_id(voice_call.id)

    # recheck
    with thrift_client('eos') as eos_client:
        order_ids = [order.order_id for order in voice_orders]
        t_orders = eos_client.mget(order_ids)

    t_orders = filter(
        lambda _o: _o.status_code == STATUS_PROCESSING,
        t_orders)
    t_order_ids = [order.id for order in t_orders]

    voice_orders = [v_order for v_order in voice_orders
                    if v_order.order_id in t_order_ids]

    if not voice_orders:
        return

    call_params = _generate_call_params(voice_call, voice_orders)
    call_status = _send_call(call_params)

    voice_call.call_status = call_status
