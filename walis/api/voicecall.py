#!/usr/bin/env python2
# coding=utf8

from __future__ import absolute_import, division, print_function
from walis.api.base import BaseApi
from walis.core.api import api
from .handler import voicecall


class VoiceCallApi(BaseApi):
    route_base = "voicecall"

    @api('/async_result', methods=['GET', 'POST'])
    def sync_result(self):
        return voicecall.update_status()

    @api('/keysback', methods=['GET', 'POST'])
    def keysback(self):
        return voicecall.update_keysback()

    @api('/call_end', methods=['GET', 'POST'])
    def call_end(self):
        return voicecall.call_end_handler()
