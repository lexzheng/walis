#!/usr/bin/env python2
# -*- coding: utf8 -*-

from __future__ import print_function, absolute_import, division

from walis.api.handler.sms import (
    sms as sms_handler,
    hermes_receiver as hms_rec_handler
)
from walis.core.api import api

from .base import BaseApi


class SmsApi(BaseApi):
    route_base = 'sms'

    @api('/query_receive_by_mobile', methods=['GET'])
    def query_receive_by_mobile(self):
        return sms_handler.query_receive_by_mobile()


class HermesReceiverApi(BaseApi):
    route_base = 'hermes'

    @api('/push/', methods=['POST', 'PUT'])
    def push(self):
        return hms_rec_handler.push()
