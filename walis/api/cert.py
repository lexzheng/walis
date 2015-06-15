#!/usr/bin/env python2
# -*- coding: utf8 -*-

from __future__ import print_function, division, absolute_import

from .base import BaseApi

from walis.api.handler.cert import cert as cert_handler
from walis.core.api import api


class CertificationApi(BaseApi):
    route_base = 'certification'
    handler = cert_handler

    def get(self, restaurant_id):
        return self.handler.get(restaurant_id)

    def post(self):
        return self.handler.add()

    def put(self):
        return self.handler.update()

    @api('/<int:restaurant_id>/get_by_uploader')
    def get_by_uploader(self, restaurant_id):
        return self.handler.get_by_uploader(restaurant_id)

    @api('/<int:restaurant_id>/get_by_admin')
    def get_by_admin(self, restaurant_id):
        return self.handler.get_by_admin(restaurant_id)

    @api('/get_certification_list_from_mm')
    def get_certification_list_from_mm(self):
        return self.handler.get_list_from_mm()

    @api('/<int:restaurant_id>/get_processing_record')
    def get_processing_record(self, restaurant_id):
        return self.handler.get_processing_record(restaurant_id)

    @api('/process', methods=['PUT'])
    def process(self):
        self.handler.processing()
