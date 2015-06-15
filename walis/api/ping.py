# coding=utf8

from __future__ import absolute_import, division, print_function
from walis.api.base import BaseApi


class PingApi(BaseApi):
    route_base = 'ping'

    def get(self):
        return 'pong'
