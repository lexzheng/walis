#!/usr/bin/env python2
# -*- coding: utf8 -*-

from __future__ import print_function, division, absolute_import

from walis.core.api import api
from walis.api.handler.misc import (
    chaos as chaos_handler,
    eleme_order as eleme_order_handler,
    simple_url as simple_url_handler,
    bank as bank_handler,
    )

from .base import BaseApi

class ChaosApi(BaseApi):

    route_base = "chaos"
    handler = chaos_handler

    @api('/edit_username_mobile',methods=['POST'])
    def edit_username_mobile(self):
        return self.handler.edit_username_mobile()

    @api('/get_user/<int:user_id>')
    def get_user(self,user_id):
        return self.handler.get_user(user_id)

class ElemeOrder(BaseApi):

    route_base = 'elemeorder'
    decorators = []
    handler = eleme_order_handler

    @api("/get_arbitrating_orders")
    def get_arbitrating_orders(self):
        return self.handler.get_arbitrating_orders()


class SimpleURLApi(BaseApi):

    route_base = 'simple_url'
    decorators = []
    handler = simple_url_handler

    @api("/get_empty_image_hash_restaurant")
    def get_empty_image_hash_restaurant(self):
        return self.handler.get_empty_image_hash_restaurant()

class BankApi(BaseApi):
    route_base = "bank"
    handler = bank_handler

    def gets(self):
        return self.handler.get_bank_list()
