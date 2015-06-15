#!/usr/bin/env python2
# coding=utf8

from __future__ import absolute_import, division, print_function
from walis.api.base import BaseApi
from walis.api.handler.banner import BannerHandler
from walis.core.api import api


class BannerApi(BaseApi):
    route_base = 'banner'
    handler = BannerHandler()

    @api('/<int:id>')
    def get(self, id):
        return self.handler.get(id)

    def post(self):
        return self.handler.post()

    @api('get_list')
    def get_list(self):
        return self.handler.gets()

    def put(self, id):
        return self.handler.put(id)

    @api('/set_valid', methods=['PUT'])
    def set_valid(self):
        return self.handler.set_valid()

    @api('/get_region_struct')
    def get_region_struct(self):
        return self.handler.get_region_struct()

    @api('/get_activities')
    def get_activities(self):
        return self.handler.get_activities()

    @api('/get_user_city_ids')
    def get_user_city_ids(self):
        return self.handler.get_user_city_ids()