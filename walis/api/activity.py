#!/usr/bin/env python2
# -*- coding: utf8 -*-
from __future__ import absolute_import, division, print_function
from walis.api.base import BaseApi
from .handler.activity import (
    pay,
    contract,
    pay_notice,
    rst_activity,
    food_activity,
)
from walis.core.api import api


class RstActivityApi(BaseApi):
    route_base = 'restaurant_activity'

    def post(self):
        return rst_activity.add()

    def get(self, act_id):
        return rst_activity.get(act_id)

    def put(self):
        return rst_activity.update()

    @api('/get_by_city_and_period')
    def get_by_city_and_period(self):
        return rst_activity.get_by_city_and_period()

    @api('/query_restaurant_activity_for_admin')
    def query_restaurant_activity_for_admin(self):
        return rst_activity.query_restaurant_activity_for_admin()


class FoodActivityApi(BaseApi):
    route_base = 'food_activity'

    def get(self, act_id):
        return food_activity.get(act_id)


class ActivityContractApi(BaseApi):
    route_base = 'activity_contract'

    @api('/approve', methods=['POST'])
    def approve(self):
        return contract.approve()

    @api('/reject', methods=['POST'])
    def reject(self):
        return contract.reject()

    @api('/list_for_market')
    def list_for_market(self):
        return contract.list_for_market()

    @api('/contract_count_wait_to_process')
    def contract_count_wait_to_process(self):
        return contract.contract_count_wait_to_process()


class ActivityPaymentApi(BaseApi):
    route_base = 'activity_payment'

    @api('/get_pending_status')
    def get_pending_status(self):
        return pay.get_pending_status()

    @api('/get_all_status')
    def get_all_status(self):
        return pay.get_all_status()

    @api('/export_excel')
    def export_excel(self):
        return pay.export_excel()

    @api('/approval', methods=['POST'])
    def approval_payment(self):
        return pay.approval_payment()

    @api('/reject', methods=['POST'])
    def reject_payment(self):
        return pay.reject_payment()


class ActPayNoticeApi(BaseApi):
    route_base = 'activity_pay_notice'

    @api('/get_summery')
    def get_summery(self):
        return pay_notice.get_summery()

    @api('get_sms_info')
    def get_sms_info(self):
        return pay_notice.get_sms_info()

    @api('/get_sms_reply')
    def get_sms_reply(self):
        return pay_notice.get_sms_reply()
