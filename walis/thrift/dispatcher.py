#!/usr/bin/env python2
# -*- coding: utf8 -*-

from __future__ import absolute_import, division, print_function

from .handler import order
from .handler import voicecall as vc
from .handler import restaurant as rst
from .handler import cs


class JvsService:

    def ping(self):
        return 'pong'

    def restaurant_recruitment_post_t(self, data):
        return rst.add_restaurant_recruitment(data)

    def restaurant_recruitment_get_t(self, _id):
        return rst.get_restaurant_recruitment(_id)

    def restaurant_recruitment_search_t(self, q):
        return rst.query_restaurant_recruitment(q)

    def restaurant_recruitment_put_t(self, data):
        return rst.update_restaurant_recruitment(data)

    def restaurant_recruitment_patch(self, data):
        return rst.patch_update_restaurant_recruitment(data)

    def restaurant_recruitment_delete(self, _id):
        return rst.delete_restaurant_recruitment(_id)

    def get_voice_order(self, order_id):
        return vc.get_voice_order(order_id)

    def mget_voice_order(self, order_ids):
        return vc.mget_voice_order(order_ids)

    def is_suspicious_order_auditor(self, auditor_id):
        return order.is_suspicious_order_auditor(auditor_id)

    def get_restaurant_director_ids(self, restaurant_id):
        return rst.get_restaurant_director_ids(restaurant_id)

    def change_director_region(self, user_id, old_region, new_region):
        return rst.change_director_region(user_id, old_region, new_region)

    def set_bd_restaurant_director(self, user_id, rst_ids, notice_enabled=None, in_charge=None):
        return rst.set_bd_restaurant_director(user_id, rst_ids, notice_enabled, in_charge)

    def add_cs_process_type_change_record(self, user_id, from_type, to_type):
        return cs.add_process_type_change_record(user_id, from_type, to_type)
