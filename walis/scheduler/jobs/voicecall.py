#!/usr/bin/env python2
# coding=utf8

from __future__ import absolute_import, division, print_function
import time
import logging
from walis.service.voicecall import settings
from walis.service.voicecall.handler import (
    voice_order_handler,
    voice_call_handler,
)
from walis.service.voicecall.utils import (
    get_call_lock_key,
    get_rst_lock_key,
)
from walis.core.async import (
    enqueue,
    BSTALK_TUBES,
)
from walis.model.walis import db_commit
from walis.model.walis.voicecall import (
    VoicecallBan,
    VoiceCall,
)
from walis.thirdparty import (
    thirdparty_svc,
    thrift_client,
)
from walis.utils.lock import unlock, lock


log = logging.getLogger(__name__)


def voiceorder_job():
    """ query all unprocessed orders from now

    """

    now = time.time()
    ORDER_CONST = thirdparty_svc.eos.ElemeOrderConst
    order_trigger_time = int(now - settings.send_vc_deadline)

    order_query = thirdparty_svc.eos.TOrderQuery()
    order_query.from_datetime = order_trigger_time
    order_query.statuses = (ORDER_CONST.STATUS_PROCESSING,)
    order_query.order_modes = (ORDER_CONST.ORDER_MODE_ELEME,)
    order_query.limit = 1000
    with thrift_client('eos') as eos:
        orders = _filter_orders(eos.query_order(order_query))

    log.info('total {} unprocessed sms orders.'.format(len(orders)))
    if _trigger_voicecall(
            orders,
            order_trigger_time,
            order_trigger_time + settings.voice_order_interval - 1):

        log.info('triggered voicecall with orders {}'.format(orders))
        enqueue(BSTALK_TUBES['tube_vo'], voice_order_handler, orders)


@db_commit
def voicecall_job():
    """ get calls from database, and send call request

    """
    not_dialed_calls = VoiceCall.get_by_status(VoiceCall.STATUS_NOT_DIAL)
    if not not_dialed_calls:
        return

    calls = _filter_calls(not_dialed_calls)
    if not calls:
        return

    for call in calls:
        # lock voice call
        if not lock(get_call_lock_key(call.id), time_out=30):
            continue

        # lock restaurant's line
        if lock(get_rst_lock_key(call.restaurant_id)):
            enqueue(BSTALK_TUBES['tube_vo'], voice_call_handler, call.id)
        else:
            unlock(get_call_lock_key(call.id))


@db_commit
def voicecall_ban_daily_clean_job():
    """ clean voicecall banned restaurant info in middle night

    """
    log.info('cleaning voicecall restaurant ban.')
    VoicecallBan.clean_today_ban()


def _trigger_voicecall(orders, from_time, to_time):
    if not orders:
        return False

    for order in orders:
        if from_time <= order.created_at <= to_time:
            return True

    return False


def _filter_orders(orders):
    """ filter orders by write and black list

    """
    if settings.write_list:
        orders = filter(lambda order: order.restaurant_id in
                        settings.write_list, orders)

    if settings.black_list:
        orders = filter(lambda order: order.restaurant_id not in
                        settings.black_list, orders)

    return orders


def _filter_calls(calls):
    """ filter calls by banned restaurant ids """
    banned_restaurants = VoicecallBan.mget_by_restaurant_ids(
        [c.restaurant_id for c in calls])

    if not banned_restaurants:
        return calls

    banned_restaurant_ids = [b.restaurant_id for b in banned_restaurants]

    call_results = []
    for call in calls:

        if call.restaurant_id in banned_restaurant_ids:
            call.update(VoiceCall.STATUS_BANNED)
        else:
            call_results.append(call)

    return call_results

