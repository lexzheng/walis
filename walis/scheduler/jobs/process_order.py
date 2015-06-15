#!/usr/bin/env python2
# coding=utf8

from __future__ import absolute_import, division, print_function
import logging
from walis.service.order.auto_process import auto_process_order
from walis.core.async import (
    BSTALK_TUBES,
    enqueue,
)
from walis.scheduler.jobs import job_deco
from walis.thirdparty import (
    thirdparty_svc,
    thrift_client,
)

log = logging.getLogger(__name__)


@job_deco
def process_order():
    """ get unprocessed order, put into beanstalk handlers """
    # 短信订单 & 第三方配送订单
    order_modes = (thirdparty_svc.eos.ElemeOrderConst.ORDER_MODE_ELEME,
                   thirdparty_svc.eos.ElemeOrderConst.ORDER_MODE_TPD_ELEME)
    with thrift_client('eos') as eos:
        order_ids = eos.get_unprocessed_order_ids(order_modes)

    if not order_ids:
        return

    for order_id in order_ids:
        enqueue(
            BSTALK_TUBES['tube_order_auto_proc'],
            auto_process_order,
            order_id
        )
