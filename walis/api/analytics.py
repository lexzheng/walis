#! /usr/bin/env python2
# -*- coding:utf-8 -*-

from __future__ import absolute_import, division, print_function

from walis.api.base import BaseApi
from walis.api.handler.analytics import (
    transaction as transaction_handler,
    trs_query_config as query_cfg_handler,
    )

from walis.core.api import api


class TransactionQueryConfigApi(BaseApi):
    route_base = 'analytics/transaction'

    @api('/city/query_config', methods=['GET', ])
    def gets(self):
        return query_cfg_handler.gets()

    @api('/city/query_config', methods=['POST', ])
    def post(self):
        return query_cfg_handler.post()

    @api('/city/<int:city_id>/query_config')
    def get(self, city_id):
        return query_cfg_handler.get(city_id)

    @api('/city/<int:city_id>/query_config', methods=['PUT', ])
    def put(self, city_id):
        return query_cfg_handler.put(city_id)


class RegionTransactionApi(BaseApi):
    route_base = 'analytics/transaction'

    @api('/region', methods=['POST', ])
    def query(self):
        return transaction_handler.query_by_area()

    @api('/city/<int:city_id>')
    def get_by_city(self, city_id):
        return transaction_handler.query_by_city(city_id)
