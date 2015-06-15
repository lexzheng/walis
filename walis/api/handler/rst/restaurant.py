#!/usr/bin/env python2
# -*- coding: utf8 -*-

from __future__ import division, print_function, absolute_import

import datetime

from flask import request
from flask.ext.login import current_user

from walis.service.activity import rst_activity as rst_act_base
from walis.service.rst.const import  RestaurantConst
from walis.service.rst import restaurant as restaurant_base
from walis.service.activity import (
    pay as act_pay_base,
    food_activity as food_act_base,
)
from walis.exception.util import raise_auth_exc
from walis.exception.error_code import AUTH_FAILED_ERROR,AUTH_UTP_FAILED_ERROR
from walis.thirdparty import thrift_client, thirdparty_svc
from walis.utils.http import args_parser, Arg, jsonpickle_dumps
from walis.utils.paging import get_paging_params
from walis.utils.time import (
    get_today_begin_time,
    get_today_end_time,
    datetime2timestamp,
    str2datetime
)
from walis.model.zeus.activity import SubsidyPayRecord
from walis.utils.thrift import ThriftEnum
from walis.service.activity.pay_notice.query import get_pay_activities_by_restaurant
from walis.service.activity.utils import get_restaurant_activity_name
from walis.api.handler.rst.utils import get_activity_ids

from walis.api.handler.auth_utp import  check_is_rst_owner,deco_check_is_rst_owner


SubsidyContractStatus = thirdparty_svc.ers.SubsidyContractStatus
_RestaurantActivityConst = thirdparty_svc.ers.RestaurantActivityConst
RestaurantActivityConstType = ThriftEnum(_RestaurantActivityConst,[
    'STATUS_TYPE_NO_CONTRACT',
    'STATUS_TYPE_CONTRACT_PROCESSING',
    'STATUS_TYPE_PARTICIPATED',
    'STATUS_TYPE_CONTRACT_NOTSET',]
)
RestaurantActivityConstStatusType = ThriftEnum(_RestaurantActivityConst,
    [
        'TYPE_COUPON',
        'TYPE_NEW_USER_DISCOUNT',
        'TYPE_EXTRA_DISCOUNT',
        'TYPE_OLPAYMENT_REDUCE',
        'TYPE_ADVANCED_DISCOUNT',
        'TYPE_NEW_USER_DISCOUNT_EXCLUSIVE',
        'TYPE_ORDER_HONGBAO',
    ]
)
_SubsidyConst = thirdparty_svc.ers.SubsidyConst
SubsidyConst = ThriftEnum(_SubsidyConst)

from walis.utils.dirty import fix_restaurant_attribute, fix_food_b2f
from walis.service.coffee import mkt as mkt_service


class RestaurantManager(RestaurantConst):

    restaurant_base = restaurant_base

    def get_olpay_records(self, restaurant_id, type, begin_date, end_date):

        admin_id = self._get_admin_id(restaurant_id)

        if begin_date is None:
            begin_date = get_today_begin_time(return_timestamp=True)
        else:
            begin_date = self._get_hour0_timestamp(begin_date)

        if end_date is None:
            end_date = get_today_end_time(return_timestamp=True)
        else:
            end_date = self._get_hour24_timestamp(end_date)

        return self.restaurant_base.get_olpay_records(
            admin_id, begin_date, end_date, type)

    def get_olpay_detail(self, restaurant_id, date=None, status=None):

        admin_id = self._get_admin_id(restaurant_id)
        page_no, page_size = get_paging_params()

        begin_date = end_date = None
        if date is not None:
            begin_date = self._get_hour0_timestamp(date)
            end_date = self._get_hour24_timestamp(date)

        # unify status code
        if status == self.TR_COMING_INCOME:
            status = self.TR_PROCESSING
        elif status == self.TR_ARRIVED_INCOME:
            status = self.TR_SUCCESS

        details, total_num = self.restaurant_base.get_olpay_detail(
            admin_id, begin_date, end_date, (page_no - 1) * page_size,
            page_size, status)

        # unify status code
        detail_result = []
        for detail in details:
            if detail.status == self.TR_PROCESSING:
                detail.status = self.TR_COMING_INCOME
                detail_result.append(detail)
            elif detail.status == self.TR_SUCCESS:
                detail.status = self.TR_ARRIVED_INCOME
                detail_result.append(detail)

        return detail_result, total_num

    def get_withdraw_records(self, restaurant_id, status, begin_date, end_date):

        page_no, page_size = get_paging_params()

        if begin_date is not None:
            begin_date = self._get_hour0_timestamp(begin_date)

        if end_date is not None:
            end_date = self._get_hour24_timestamp(end_date)

        # unify status code
        if status is not None:
            status = self._withdraw_status_map('api2zeus', status)

        records, total_num = self.restaurant_base.get_withdraw_records(
            restaurant_id, status, begin_date, end_date,
            (page_no - 1) * page_size, page_size)

        # unify status code
        for record in records:
            record.status = self._withdraw_status_map('zeus2api', record.status)

        return records, total_num

    def get_balance_change(self, restaurant_id, trade_type, begin_date,
                           end_date):

        admin_id = self._get_admin_id(restaurant_id)
        page_no, page_size = get_paging_params()

        if begin_date is not None:
            begin_date = self._get_hour0_timestamp(begin_date)

        if end_date is not None:
            end_date = self._get_hour24_timestamp(end_date)

        # unify trade_type
        if trade_type is not None:
            trade_type = self._balance_change_status_map('api2zeus', trade_type)
        else:
            trade_type = [0, 1, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

        records, total_num = self.restaurant_base.get_balance_change(
            admin_id, trade_type, begin_date, end_date,
            (page_no - 1) * page_size, page_size)

        # unify trade_type
        for record in records:
            record.trade_type = self._balance_change_status_map(
                'zeus2api', record.trade_type)

        return records, total_num

    def _get_admin_id(self, restaurant_id):
        return self.restaurant_base.get_admin_id(restaurant_id)

    @staticmethod
    def _get_hour0_timestamp(date_str):
        _datetime = str2datetime(date_str)
        hour0_datetime = datetime.datetime(
            year=_datetime.tm_year,
            month=_datetime.tm_mon,
            day=_datetime.tm_mday,
            hour=0,
            minute=0,
            second=0)
        return datetime2timestamp(hour0_datetime)

    @staticmethod
    def _get_hour24_timestamp(date_str):
        _datetime = str2datetime(date_str)
        hour24_datetime = datetime.datetime(
            year=_datetime.tm_year,
            month=_datetime.tm_mon,
            day=_datetime.tm_mday,
            hour=23,
            minute=59,
            second=59)
        return datetime2timestamp(hour24_datetime)


restaurant_manager = RestaurantManager()

GARNISH_CATEGORY_ID = 2147483647

@deco_check_is_rst_owner
def get(restaurant_id):
    restaurant_id = int(restaurant_id)

    with thrift_client('ers') as ers_client:
        restaurant = ers_client.get(restaurant_id)
        fix_restaurant_attribute(restaurant)
        return restaurant


@deco_check_is_rst_owner
def put(restaurant_id):
    restaurant_id = int(restaurant_id)

    restaurant = thirdparty_svc.ers.TRestaurant()
    for k, v in request.json.iteritems():
        setattr(restaurant, k, v)
    if getattr(restaurant,'attribute',None) is not None:
        restaurant.attribute = jsonpickle_dumps(restaurant.attribute)
    with thrift_client('ers') as ers_client:
        result = ers_client.update_restaurant(restaurant_id, current_user.id, restaurant)
        return ''


def mget():
    args_spec = {
        'ids':Arg(),
    }
    args = args_parser.parse(args_spec)
    ids = args.get('ids', None)
    ids = ids if ids else request.json.get('restaurant_ids')
    with thrift_client('ers') as ers:
        result = ers.mget(ids)
        return result


def menu(restaurant_id):
    """
    获取餐厅菜单
    """
    with thrift_client('ers') as ers:
        categories = ers.query_food_category_with_foods(restaurant_id)
        for category in categories:
            _activity_ids = get_activity_ids(category.foods)
            # _activities = _week_activity_ids_to_full(_activity_ids)
            category.food_category._activity = _activity_ids
            category.food_category._activity_objs = [food_act_base.get(_id) if _id else None for _id in _activity_ids]
            for food in category.foods:
                fix_food_b2f(food)
        categories = [category for category in categories
                      if category.food_category.id != GARNISH_CATEGORY_ID]
        return categories


def sign_contract():
    """
    餐厅签署活动合同
    """
    args_spec = {
        'contract_id':Arg(int),
        'restaurant_id':Arg(int),
    }
    args = args_parser.parse(args_spec)
    with thrift_client('ers') as ers:
        result = ers.sign_activity_subsidy_contract(args['contract_id'],
                                                    args['restaurant_id'])
    return ''


def refuse_contract():
    """
    餐厅拒绝签署活动合同
    """
    args_spec = {
        'contract_id':Arg(int),
        'restaurant_id':Arg(int),
    }
    args = args_parser.parse(args_spec)
    with thrift_client('ers') as ers:
        result = ers.refuse_activity_subsidy_contract(args['contract_id'],
                                                      args['restaurant_id'])
    return ''


def food_category(restaurant_id):
    """
    获取餐厅菜单上所有分类
    """
    with thrift_client('ers') as ers:
        categories = ers.query_food_category_by_restaurant(restaurant_id)
        return categories


def food_activity_map(restaurant_id):
    """
    wait to add
    """
    with thrift_client('ers') as ers:
        _map = ers.get_weekday_food_activity_id_map([], restaurant_id)
        return _map


def set_restaurant_activity():
    """
    参加餐厅活动
    """
    args_spec = {
        'restaurant_id':Arg(),
        'activity_id':Arg(),
        'activity_type':Arg()
    }

    args = args_parser.parse(args_spec)
    restaurant_id = args['restaurant_id']
    activity_id = args['activity_id']
    activity_type = args['activity_type']

    if activity_type is not None and activity_id is None:
        TRestaurantActivity = thirdparty_svc.ers.TRestaurantActivity
        with thrift_client('ers') as ers:
            zeus_result = ers.javis_query_restaurant_activity_by_restaurant(restaurant_id)
        restaurant_activity_map = {}
        for activity in zeus_result:
            activity_type_value = activity.type
            if activity_type_value in RestaurantActivityConstType._v2n.keys():
                restaurant_activity_map[activity_type_value] = activity
        for activity_type_value in RestaurantActivityConstType._v2n.keys():
            restaurant_activity_map.setdefault(activity_type_value,TRestaurantActivity())
        restaurant_activity = restaurant_activity_map[activity_type]
        activity_id = restaurant_activity.id
    else:
        # 取消掉activity_type,这样就是参加活动.下面的代码依赖这个来决定调用哪个接口-.-
        activity_type = None
    if activity_id is None:
        raise Exception('activity id is None or quit an unexist activity')
    with thrift_client('ers') as ers:
        if activity_type:
            result = ers.quit_restaurant_activity(restaurant_id,activity_id)
        else:
            result = ers.participate_restaurant_activity(restaurant_id,activity_id)
    return ''


def quit_restaurant_activity():
    """
    # deprecate
    退出餐厅活动(即设置餐厅活动为未设置状态)
    """
    args_spec = {
        'restaurant_id':Arg(),
        'activity_id':Arg(),
    }
    args = args_parser.parse(args_spec)
    restaurant_id = args['restaurant_id']
    activity_id = args['activity_id']
    with thrift_client('ers') as ers:
        result = ers.quit_restaurant_activity(restaurant_id,activity_id)
    return ''


def restaurant_activity(restaurant_id):
    """
    获取餐厅活动
    """
    restaurant_id = int(restaurant_id)
    TRestaurantActivity = thirdparty_svc.ers.TRestaurantActivity
    with thrift_client('ers') as ers:
        zeus_result = ers.javis_query_restaurant_activity_by_restaurant(restaurant_id)
        result = {}
        for activity in zeus_result:
            activity_type_value = activity.type
            if activity_type_value in RestaurantActivityConstType._v2n.keys():
                result[activity_type_value] = activity
        for activity_type_value in RestaurantActivityConstType._v2n.keys():
            result.setdefault(activity_type_value,TRestaurantActivity())
        for type_name,type_value in RestaurantActivityConstType._n2v.iteritems():
            status = ers.get_restaurant_activity_status(restaurant_id,type_value)
            setattr(result[type_value],'_status',status)
            activity = result[type_value]
            activity_id = activity.id
            amount = rst_act_base.get_amount(restaurant_id,activity_id)
            setattr(activity,'_amount',amount)
        return result


def apply_for_activity_subsidy_contract():
    """
    申请参加活动.会生成一份活动对应的合同等待同意
    """
    #todo 权限效验 current_user.id
    args_spec = {
        'restaurant_id': Arg(int),
        'activity_id': Arg(int),
        'activity_category_id': Arg(int),
        'subsidy': Arg(float),
    }
    args = args_parser.parse(args_spec)
    with thrift_client('ers') as ers:
        ers.apply_for_activity_subsidy_contract(args['restaurant_id'],
                                                args['activity_id'],
                                                args['activity_category_id'],
                                                args['subsidy'],
                                                current_user.id)
    return ''


def apply_for_complex_activity_subsidy_contract():
    """
    申请参加活动.会生成一份活动对应的合同等待同意
    """
    #todo 权限效验 current_user.id
    args_spec = {
        'restaurant_id': Arg(int),
        'activity_id': Arg(int),
        'activity_category_id': Arg(int),
        'subsidy': Arg(str),
    }
    args = args_parser.parse(args_spec)
    with thrift_client('ers') as ers:
        ers.apply_for_complex_activity_subsidy_contract(args['restaurant_id'],
                                                        args['activity_id'],
                                                        args['activity_category_id'],
                                                        args['subsidy'],
                                                        current_user.id)
    return ''


def participatable_food_activity(restaurant_id):
    with thrift_client('ers') as ers:
        result = ers.get_participatable_food_activity_ids(restaurant_id)
        activity_ids = []
        result['8'] = set(result.values()[0]) if len(result) else set()
        for day in range(1,8):
            result.setdefault(day,[])
            activity_ids.extend(result[day])
            result['8'] &= set(result[day])
        activities = food_act_base.mget(activity_ids)
        activity_map = {activity.id:activity for activity in activities}
        for day in range(1,8):
            day_activity_ids = result[day]
            result[day] = [activity_map[_id] for _id in day_activity_ids]
        week_activity_ids = result['8']
        result['8'] = [activity_map[_id] for _id in week_activity_ids]
    return result


def participatable_restaurant_activity(restaurant_id):
    """
    获取可参加的餐厅活动
    返回值为活动+补贴的组合-.-
    """
    restaurant_id = int(restaurant_id)
    result = {}
    with thrift_client('ers') as ers:
        for type_name,type_value in RestaurantActivityConstType._n2v.iteritems():
            zeus_result = ers.get_participatable_restaurant_activity_ids(restaurant_id,type_value)
            zeus_result = [rst_act_base.get(_id) for _id in zeus_result]
            result[type_value] = zeus_result
        for type_name,type_value in RestaurantActivityConstType._n2v.iteritems():
            for activity in result[type_value]:
                activity_id = activity.id
                amount = rst_act_base.get_amount(restaurant_id,activity_id)
                setattr(activity,'_amount',amount)
    return result


def food_activity(restaurant_id):
    """
    获取食物活动
    包括食物活动状态是已参加,查询对应合同获取补贴金额,否则补贴金额为None
    """
    restaurant_id = int(restaurant_id)
    result = []
    with thrift_client('ers') as ers:
        zeus_result = ers.get_food_activity_status(restaurant_id)
        for activity_id,status in zeus_result.iteritems():
            activity_id = int(activity_id)
            activity = food_act_base.get(activity_id)
            amount = food_act_base.get_amount(restaurant_id,activity_id)
            setattr(activity,'_amount',amount)
            setattr(activity,'_status',status)
            result.append(activity)
    return result


def appliable_restaurant_activity(restaurant_id):
    """
    可申请参加的餐厅活动,即可以申请一份活动对应的合同去签署.注意不等同于可参加的餐厅活动
    """
    restaurant_id = int(restaurant_id)
    _result = {}
    with thrift_client('ers') as ers:
        for type_name,type_value in RestaurantActivityConstType._n2v.iteritems():
            zeus_result = ers.get_restaurant_appliable_activity_ids(restaurant_id,SubsidyConst.CATEGORY_RESTAURANT_ACTIVITY,type_value)
            zeus_result = [rst_act_base.get(_id) for _id in zeus_result]
            _result[type_value] = zeus_result
    result = []
    for _type,_activity_list in _result.iteritems():
        result.extend(_activity_list)
    return result


def appliable_food_activity(restaurant_id):
    """
    可申请参加的食物活动,即可以申请一份活动对应的合同去签署.注意不等同于可参加的食物活动
    """
    restaurant_id = int(restaurant_id)
    with thrift_client('ers') as ers:
        activities = ers.get_restaurant_appliable_activity_ids(restaurant_id, SubsidyConst.CATEGORY_FOOD_ACTIVITY, None)
        activities = [food_act_base.get(_id) for _id in activities]
    return activities


def get_success_pay_activities(restaurant_id):
    """
    获取指定餐厅的所有活动名称
    """
    activities = get_pay_activities_by_restaurant(restaurant_id)

    results = [{'activity_id': act[0],
                'activity_category_id': act[1],
                'activity_name': ''}
               for act in activities]

    for act in results:
        if act['activity_category_id'] == \
                SubsidyPayRecord.CATEGORY_FOOD_ACTIVITY:
            try:
                with thrift_client('ers') as ers:
                    act['activity_name'] =\
                        ers.get_food_activity(act['activity_id']).name
            except:
                act['activity_name'] = ''

        elif act['activity_category_id'] == \
                SubsidyPayRecord.CATEGORY_RESTAURANT_ACTIVITY:
            try:
                with thrift_client('ers') as ers:
                    act['activity_name'] = get_restaurant_activity_name(
                        ers.get_restaurant_activity(act['activity_id']))
            except:
                act['activity_name'] = ''

    return results


def payment_log(restaurant_id):
    args = args_parser.parse_all()
    activity_id = args.get('activity_id')
    activity_category_id = args.get('activity_category_id')

    page_no, page_size = get_paging_params()
    records, total_num = act_pay_base.get_pay_records2(
        restaurant_id,
        activity_id,
        activity_category_id,
        offset=(page_no-1) * page_size,
        limit=page_size,
    )

    return {'records': records, 'total_num': total_num}


def olpay_income_records(restaurant_id):
    args = args_parser.parse({
        'type': Arg(int, required=False),
        'begin_date': Arg(str, required=False),
        'end_date': Arg(str, required=False),
    })
    records = restaurant_manager.get_olpay_records(
        restaurant_id, **args)
    return {'records': records}


def olpay_income_details(restaurant_id, date):
    args = args_parser.parse({
        'status': Arg(int, required=False),
    })
    records, total_num = restaurant_manager.get_olpay_detail(
        restaurant_id, date=date, **args)
    return {'records': records, 'total_num': total_num}


def withdraw_records(restaurant_id):
    args = args_parser.parse({
        'status': Arg(int, required=False),
        'begin_date': Arg(str, required=False),
        'end_date': Arg(str, required=False),
    })
    records, total_num = restaurant_manager.get_withdraw_records(
        restaurant_id, **args)
    return {'records': records, 'total_num': total_num}


def balance_change(restaurant_id):
    args = args_parser.parse({
        'trade_type': Arg(int, required=False),
        'begin_date': Arg(str, required=False),
        'end_date': Arg(str, required=False),
    })
    records, total_num = restaurant_manager.get_balance_change(
        restaurant_id, **args)
    return {'records': records, 'total_num': total_num}
