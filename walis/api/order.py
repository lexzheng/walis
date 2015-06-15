#!/usr/bin/env python2
# -*- coding: utf8 -*-

from __future__ import absolute_import, division, print_function

from .base import BaseApi
from walis.core.api import api
from .handler.order import audit

from walis.api.handler.order import (
    order_query as order_query_handler,
    order_query_export as order_query_export_handler
)


class CustomerServiceUserApi(BaseApi):
    route_base = '/customer_service_user'

    # @api('', trailing_slash=False, strict_slashes=True)
    def gets(self):
        return audit.get_customer_service_user()

    def put(self, pk):
        return audit.update_customer_service_user(pk)


class OrderAuditApi(BaseApi):
    route_base = '/order_audit'

    @api('/get_suspicious_page')
    def get_suspicious_page(self):
        return audit.get_suspicious_page()

    @api('/finish_suspicious_group_auditing', methods=['POST'])
    def finish_suspicious_group_auditing(self):
        return audit.finish_suspicious_group_auditing()

    @api('/filter_suspicious_orders_amount')
    def filter_suspicious_orders_amount(self):
        return audit.filter_suspicious_orders_amount()

    @api('/set_order_valid', methods=['POST'])
    def set_order_valid(self):
        return audit.set_order_valid()

    @api('/set_order_invalid', methods=['POST'])
    def set_order_invalid(self):
        return audit.set_order_invalid()

    @api('/set_order_phone_confirmed', methods=['POST'])
    def set_order_phone_confirmed(self):
        return audit.set_order_phone_confirmed()

    @api('/set_user_active', methods=['POST'])
    def set_user_active(self):
        return audit.set_user_active()

    @api('/set_phone_banned', methods=['POST'])
    def set_phone_banned(self):
        return audit.set_phone_banned()

    @api('/set_restaurant_suspicious', methods=['POST'])
    def set_restaurant_suspicious(self):
        return audit.set_restaurant_suspicious()

    @api('/is_auditor/<int:user_id>')
    def is_auditor(self, user_id):
        return audit.is_auditor(user_id)


class OrderQueryApi(BaseApi):
    route_base = '/order_query'
    handler = order_query_handler

    @api('query', methods=['POST', 'GET'])
    def query(self):
        return self.handler.query()

    @api('/struct')
    def struct(self):
        return self.handler.struct()

    @api('/query_suspicous')
    def query_suspicous(self):
        return self.handler.query_suspicous()


class OrderQueryExportApi(BaseApi):
    route_base = '/order_query_export'
    decorators = []
    handler = order_query_export_handler

    @api('export', methods=['POST', 'GET'])
    def export(self):
        return self.handler.export()

