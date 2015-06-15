#!/usr/bin/env python2
# coding=utf8

from __future__ import print_function, absolute_import, division

from walis.api.handler.rst import (
    restaurant as restaurant_handler,
    menu as rst_menu_handler,
    recruit as recruit_handler,
    bankcard as bankcard_handler,
    group as group_handler,
)
from walis.api.handler.rst.food import (
    category as food_category_handler,
    image as food_image_handler,
    food as food_handler,
)
from walis.api.handler.rst.notice import modify_info_notice as modify_handler
from walis.core.api import api

from .base import BaseApi

# TODO some api should be split as tow. like methods=['GET','POST']

class RestaurantApi(BaseApi):
    route_base = 'restaurant'
    handler = restaurant_handler

    def get(self, restaurant_id):
        return self.handler.get(restaurant_id)

    def put(self, restaurant_id):
        return self.handler.put(restaurant_id)

    @api('/mget', methods=['GET', 'POST'])
    def mget(self):
        return self.handler.mget()

    #sub rest
    @api('/<int:restaurant_id>/menu')
    def menu(self, restaurant_id):
        return self.handler.menu(restaurant_id)

    @api('/sign_contract',methods=['POST'])
    def sign_contract(self):
        return self.handler.sign_contract()

    @api('/refuse_contract',methods=['POST'])
    def refuse_contract(self):
        return self.handler.refuse_contract()

    @api('/<int:restaurant_id>/food_category')
    def food_category(self, restaurant_id):
        return self.handler.food_category(restaurant_id)

    @api('/<int:restaurant_id>/food_activity_map')
    def food_activity_map(self, restaurant_id):
        return self.handler.food_activity_map(restaurant_id)

    @api('/set_restaurant_activity',methods=['POST'])
    def set_restaurant_activity(self):
        return self.handler.set_restaurant_activity()

    @api('/quit_restaurant_activity')
    def quit_restaurant_activity(self):
        return self.handler.quit_restaurant_activity()

    @api('/<int:restaurant_id>/restaurant_activity')
    def restaurant_activity(self, restaurant_id):
        return self.handler.restaurant_activity(restaurant_id)

    @api('/apply_for_activity_subsidy_contract',methods=['POST'])
    def apply_for_activity_subsidy_contract(self):
        return self.handler.apply_for_activity_subsidy_contract()

    @api('/apply_for_complex_activity_subsidy_contract',methods=['POST'])
    def apply_for_complex_activity_subsidy_contract(self):
        return self.handler.apply_for_complex_activity_subsidy_contract()

    @api('/<int:restaurant_id>/participatable_food_activity',methods=['GET','POST'])
    def participatable_food_activity(self,restaurant_id):
        return self.handler.participatable_food_activity(restaurant_id)

    @api('/<int:restaurant_id>/participatable_restaurant_activity',methods=['GET', 'POST'])
    def participatable_restaurant_activity(self,restaurant_id):
        return self.handler.participatable_restaurant_activity(restaurant_id)

    @api('/<int:restaurant_id>/food_activity',methods=['GET', 'POST'])
    def food_activity(self,restaurant_id):
        return self.handler.food_activity(restaurant_id)

    @api('/<int:restaurant_id>/appliable_restaurant_activity',methods=['GET', 'POST'])
    def appliable_restaurant_activity(self,restaurant_id):
        return self.handler.appliable_restaurant_activity(restaurant_id)

    @api('/<int:restaurant_id>/appliable_food_activity',methods=['GET','POST'])
    def appliable_food_activity(self,restaurant_id):
        return self.handler.appliable_food_activity(restaurant_id)

    @api('/<int:restaurant_id>/get_success_pay_activities')
    def get_success_pay_activities(self, restaurant_id):
        return self.handler.get_success_pay_activities(restaurant_id)

    @api('/<int:restaurant_id>/payment_log')
    def payment_log(self, restaurant_id):
        return self.handler.payment_log(restaurant_id)

    @api('/<int:restaurant_id>/olpay_income_records')
    def olpay_income_records(self, restaurant_id):
        return self.handler.olpay_income_records(restaurant_id)

    @api('/<int:restaurant_id>/olpay_income_records/<date>')
    def olpay_income_details(self, restaurant_id, date):
        return self.handler.olpay_income_details(restaurant_id,date)

    @api('/<int:restaurant_id>/withdraw_records')
    def withdraw_records(self, restaurant_id):
        return self.handler.withdraw_records(restaurant_id)

    @api('/<int:restaurant_id>/balance_change')
    def balance_change(self, restaurant_id):
        return self.handler.balance_change(restaurant_id)


class FoodCategoryApi(BaseApi):
    route_base = 'food_category'
    handler = food_category_handler

    def post(self):
        return self.handler.post()

    def get(self, category_id):
        return self.handler.get(category_id)

    def put(self, category_id):
        return self.handler.put(category_id)

    def delete(self, category_id):
        return self.handler.delete(category_id)

    @api('/<int:category_id>/with_activity')
    def with_activity(self, category_id):
        return self.handler.with_activity(category_id)

    @api('/<int:category_id>/foods')
    def foods(self, category_id):
        return self.handler.foods(category_id)

    @api('/<int:category_id>/activity')
    def activity(self, category_id):
        return self.handler.activity(category_id)

    @api('/set_position', methods=['GET', 'POST'])
    def set_position(self):
        return self.handler.set_position()


class FoodImageApi(BaseApi):
    """
    注意.food_image并非restful的-.-
    """
    #todo 未检查上传内容,似乎fuss那边或许有处理.未知

    route_base = 'food_image'
    handler = food_image_handler


    def get(self, food_id):
        return self.handler.get(food_id)

    def put(self, food_id):
        return self.handler.put(food_id)

    def delete(self, food_id):
        return self.handler.delete(food_id)


class FoodApi(BaseApi):
    route_base = 'food'
    handler = food_handler

    def post(self):
        return self.handler.post()

    def get(self, food_id):
        return self.handler.get(food_id)

    def put(self, food_id):
        return self.handler.put(food_id)

    def delete(self, food_id):
        return self.handler.delete(food_id)

    @api('/set_position', methods=['GET', 'POST'])
    def set_position(self):
        return self.handler.set_position()


class RestaurantMenuApi(BaseApi):
    route_base = 'restaurant_menu'
    handler = rst_menu_handler

    @api('/food_activity_map', methods=['GET', 'POST'])
    def food_activity_map(self):
        return self.handler.food_activity_map()

    @api('/available_food_activity', methods=['GET', 'POST'])
    def available_food_activity(self):
        return self.handler.available_food_activity()

    @api('/set_food_activity', methods=['GET', 'POST'])
    def set_food_activity(self):
        return self.handler.set_food_activity()

    @api('/set_discount', methods=['GET', 'POST'])
    def set_discount(self):
        return self.handler.set_discount()

    @api('/set_stock_full', methods=['GET', 'POST'])
    def set_stock_full(self):
        return self.handler.set_stock_full()

    @api('/set_stock_empty', methods=['GET', 'POST'])
    def set_stock_empty(self):
        return self.handler.set_stock_empty()

    @api('/batch_add_menu', methods=['GET', 'POST'])
    def batch_add_menu(self):
        return self.handler.batch_add_menu()

    @api('/set_packing_fee', methods=['POST'])
    def set_packing_fee(self):
        return self.handler.set_packing_fee()


class RecruitApi(BaseApi):
    route_base = 'recruitment'
    handler = recruit_handler

    @api('get_list_by_user')
    def get_list_by_user(self):
        return self.handler.get_by_user()

    def put(self):
        return self.handler.put()


class RstInfoNotificationApi(BaseApi):
    route_base = 'restaurant_info_notification'
    handler = modify_handler

    def get(self):
        return self.handler.get()

    def put(self):
        return self.handler.put()


class RstBankCardApi(BaseApi):
    route_base = 'restaurant'
    handler = bankcard_handler

    @api('/<int:rst_id>/bankcard/<int:bankcard_id>')
    def get_bankcard(self, rst_id, bankcard_id):
        return self.handler.get_rst_bankcard(rst_id, bankcard_id)

    @api('/bankcard/<int:bankcard_id>/pre_next')
    def get_pre_next(self, bankcard_id):
        return self.handler.get_rst_bankcard_pre_next(bankcard_id)

    @api('/<int:rst_id>/bankcard')
    def gets_by_rst(self,rst_id):
        return self.handler.get_rst_bankcard_list(rst_id)

    @api('/<int:rst_id>/bankcard', methods=['POST',])
    def add_rst_bankcard(self, rst_id):
        return self.handler.add_rst_bankcard(rst_id)

    @api('/<int:rst_id>/bankcard/<int:bankcard_id>', methods=['PUT'])
    def update_rst_bankcard(self, rst_id, bankcard_id):
        return self.handler.update_rst_bankcard(rst_id, bankcard_id)

    @api('/<int:rst_id>/bankcard/<bankcard_id>/processing_record')
    def get_processing_record(self, rst_id, bankcard_id):
        return self.handler.get_processing_record(rst_id, bankcard_id)

    @api('/<int:rst_id>/rst_admin')
    def get_rst_admin(self,rst_id):
        return self.handler.get_rst_admin(rst_id)

    @api('/bankcard', methods=['GET'])
    def gets(self):
        return self.handler.get_all_bankcard_list()

    @api('/<int:rst_id>/bankcard/<bankcard_id>/status', methods=['POST'])
    def bankcard_approve(self, rst_id, bankcard_id):
        return self.handler.bankcard_approve(rst_id, bankcard_id)

    @api('/<int:rst_id>/bankcard/<bankcard_id>/status', methods=['DELETE'])
    def bankcard_reject(self, rst_id, bankcard_id):
        return self.handler.bankcard_reject(rst_id, bankcard_id)

    @api('/<int:rst_id>/bankcard/current', methods=['DELETE'])
    def unbind_bankcard(self, rst_id):
        return self.handler.unbind_bankcard(rst_id)


class RstGroupApi(BaseApi):
    route_base = 'restaurant/group'

    def get(self, city_id):
        return group_handler.group_rsts(city_id)
