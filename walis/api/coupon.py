#!/usr/bin/env python2
# -*- coding: utf8 -*-

from __future__ import print_function, division, absolute_import

from walis.api.handler.coupon import (
    coupon as coupon_handler,
    batch as coupon_batch_handler
)
from walis.core.api import api
from .base import BaseApi


class CouponApi(BaseApi):
    route_base = 'coupon'
    handler = coupon_handler

    def post(self):
        return self.handler.save()

    def get(self, coupon_id):
        return self.handler.get(coupon_id)

    def put(self, coupon_id):
        return self.handler.update(coupon_id)

    def gets(self):
        return self.handler.query()

    @api('/sn_validation/<sn>', methods=['GET'])
    def validate_sn(self, sn):
        return self.handler.validate_sn(sn)


class CouponBatchApi(BaseApi):
    route_base = 'coupon_batch'
    handler = coupon_batch_handler

    def post(self):
        return self.handler.save()

    def gets(self):
        return self.handler.query()

