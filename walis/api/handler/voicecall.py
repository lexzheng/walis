#!/usr/bin/env python2
# coding=utf8

from __future__ import absolute_import, division, print_function
import logging

from flask import request

from walis.service.voicecall.utils import get_rst_lock_key
from walis.model.walis import db_commit
from walis.model.walis.voicecall import VoiceCall, VoiceOrder, VoicecallBan
from walis.thirdparty import thirdparty_svc, thrift_client
from walis.utils.format import to_int
from walis.utils.lock import unlock


log = logging.getLogger(__name__)

# keys pressed by restaurant admin
KEY_AFFIRM = 1
KEY_REFUSE = 2
KEY_BAN_TODAY = 9


class CallResultCode(object):
    SUCCESS = 1
    FAILED = 0
    TTS_FAILED = 15


RESULT_STATUS_MAP = {
    CallResultCode.SUCCESS: VoiceCall.STATUS_SUCCESS,
    CallResultCode.FAILED: VoiceCall.STATUS_FAILED,
    CallResultCode.TTS_FAILED: VoiceCall.STATUS_TTS_FAILED,
}


@db_commit
def update_status():
    """ Get voice call's result asynchronously """
    args = request.args if request.method == 'GET' else request.form
    log.info('Async results args: %s' % args.items())

    call_id = int(args.get('userField'))
    result = int(args.get('result'))

    voice_call = VoiceCall.get(call_id)
    voice_call.call_status = RESULT_STATUS_MAP[result]

    # unlock restaurant
    if voice_call.call_status == VoiceCall.STATUS_FAILED:
        restaurant_id = VoiceCall.get(call_id).restaurant_id
        unlock(get_rst_lock_key(restaurant_id))

    return {'result': 'success'}


@db_commit
def update_keysback():
    """ Get back voice call's keys which restaurant inputs """
    ElemeOrderConst = thirdparty_svc.eos.ElemeOrderConst
    OrderRecordConst = thirdparty_svc.eos.OrderRecordConst

    args = request.args if request.method == 'GET' else request.form
    log.info('Keysback args: %s' % args.items())
    order_id = to_int(args.get('orderId'))
    key_pressed = to_int(args.get('press'))
    call_id = to_int(args.get('userField'), silence=False)

    voice_order = VoiceOrder.get_by_order_id(order_id)

    if key_pressed == KEY_AFFIRM:
        status_to = ElemeOrderConst.STATUS_PROCESSED_AND_VALID

        with thrift_client('eos') as eos:
            eos.eleme_process_order(
                order_id, status_to, OrderRecordConst.PROCESSED_BY_MACHINE,
                OrderRecordConst.PROCESS_GROUP_ADMIN, '', 0)

        voice_order.status_code = status_to
        log.info('update eleme order to status: %d.' % status_to)

    elif key_pressed == KEY_BAN_TODAY:
        restaurant_id = VoiceCall.get(call_id).restaurant_id
        VoicecallBan.add(restaurant_id, VoicecallBan.BAN_TYPE_TODAY)
        log.info('add voice call ban for restaurant {}'.format(
            restaurant_id))

    voice_order.key_pressed = key_pressed

    return {'result': 'success'}


def call_end_handler():
    """ get call end signal """
    args = request.args if request.method == 'GET' else request.form
    try:
        call_id = int(args.get('userField'))
    except TypeError, e:
        log.error(e)
        return {'result': 'Error! Arguments is not correctly provided.'}

    log.info('voicecall end_call args is {}'.format(args.items()))

    voice_call = VoiceCall.get(call_id)
    restaurant_id = voice_call.restaurant_id

    lock_key = get_rst_lock_key(restaurant_id)
    result = unlock(lock_key)
    if not result:
        log.warn('Voice call to restaurant [id: {}] may be timed out'.
                 format(restaurant_id))

    return {'result': 'success'}
