#!/usr/bin/env python2
# coding=utf8

from __future__ import absolute_import, division, print_function
from walis.model.walis import DBSession
from walis.model.walis.voicecall import VoiceOrder


def get_voice_order(order_id):
    voice_order = DBSession.query(VoiceOrder).filter(
        VoiceOrder.order_id == order_id).first()
    return voice_order.serialize()


def mget_voice_order(order_ids):
    voice_orders = DBSession.query(VoiceOrder).filter(
        VoiceOrder.order_id.in_(order_ids)).all()
    return {v_order.order_id: v_order.serialize() for v_order in voice_orders}
