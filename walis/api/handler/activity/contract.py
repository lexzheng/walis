#!/usr/bin/env python2
# coding=utf8

from __future__ import absolute_import, division, print_function

import arrow
from webargs import Arg
from flask.ext.login import current_user

from walis.utils.paging import get_paging_params
from walis.service.activity.utils import get_marketman_relative_city_ids
from walis.service.region.city import get_city_ids_by_user
from walis.thirdparty import thirdparty_svc
from walis.thirdparty import thrift_client
from walis.utils.http import args_parser

from walis.service.activity import (
    contract as activity_contract_service,
    activity as activity_service,
)
from walis.service.activity.inner import activity as activity_base
from walis.service.rst import restaurant as rst_service
from walis.service.region import city as city_service


contract_args_spec = {
    'contract_id': Arg(int),
    'contract_ids': Arg(default=[]),
}


def approve():
    """
    城市经理批准活动合同
    """
    # 当前城市总经理
    args = args_parser.parse(contract_args_spec)
    contract_id = args['contract_id']
    contract_ids = args['contract_ids']
    if contract_id:
        contract_ids.append(contract_id)
    with thrift_client('ers') as ers:
        ers.approve_activity_subsidy_contract(contract_ids)
    return ''


def reject():
    """
    城市经理拒绝活动合同
    """
    # todo 当前城市总经理
    args = args_parser.parse(contract_args_spec)
    contract_id = args['contract_id']
    contract_ids = args['contract_ids']
    if contract_id:
        contract_ids.append(contract_id)
    with thrift_client('ers') as ers:
        ers.reject_activity_subsidy_contract(contract_ids)
    return ''


def list_for_market():
    """
    获取活动合同列表
    """
    user_args = {
        'activity_category_id': Arg(int, allow_missing=True),
        'restaurant_id': Arg(int, allow_missing=True),
        'status': Arg(int, allow_missing=True),
    }
    page_no, page_size = get_paging_params(db_style=True)
    args = args_parser.parse(user_args)
    args.update(offset=page_no, limit=page_size)
    city_ids = _get_current_user_relative_city_ids()
    result = activity_contract_service.query(
        city_ids=city_ids,
        activity_category_id=args.get('activity_category_id'),
        restaurant_ids=[args.get('restaurant_id')] if args.get(
            'restaurant_id') else None,
        status=args.get('status'),
        offset=args.get('offset'),
        limit=args.get('limit')
    )
    result['contracts'] = _decorate_contracts(result['contracts'])
    return result


def contract_count_wait_to_process():
    """
    当前未处理的合同(仅活动管理员用于同意或拒绝)
    """

    contracts = _get_current_use_relative_contracts(current_user.id)
    wait_to_process = [contract for contract in contracts if
                       contract.status == thirdparty_svc.ers.SubsidyContractStatus.UNCENSORED]
    return len(wait_to_process)


def _get_current_use_relative_contracts(uid):
    """
    这几把查询...我只能query_all了-.-...
    """
    with thrift_client('ers') as ers:
        contracts = []
        city_ids = get_marketman_relative_city_ids(uid)
        before_one_month = arrow.now().replace(days=-8).timestamp
        if current_user.is_super_admin():
            city_query = thirdparty_svc.ers.TCityQuery()
            cities = ers.query_city(city_query)
            city_ids.extend([city.id for city in cities])
        if city_ids:
            q = thirdparty_svc.ers.TActivitySubsidyContractQuery()
            q.city_ids = city_ids
            q.created_at_from = before_one_month
            _contracts = ers.query_activity_subsidy_contract(q)
            contracts.extend(_contracts)
        restaurant_ids = get_marketman_relative_city_ids(current_user.id)
        if restaurant_ids:
            q = thirdparty_svc.ers.TActivitySubsidyContractQuery()
            q.restaurant_ids = restaurant_ids
            q.created_at_from = before_one_month
            _contracts = ers.query_activity_subsidy_contract(q)
            contracts.extend(_contracts)
        return contracts


def _get_current_user_relative_city_ids():
    return get_city_ids_by_user() if current_user.is_super_admin() else get_marketman_relative_city_ids(current_user.id)


def _decorate_contracts(contracts):
    restaurant_activity_ids = []
    food_activity_ids = []
    restaurant_ids = []
    citys_ids = []
    for contract in contracts:
        if activity_service.is_restaurant_activity(contract['activity_category_id']):
            restaurant_activity_ids.append(contract['activity_id'])
        if activity_service.is_food_activity(contract['activity_category_id']):
            food_activity_ids.append(contract['activity_id'])
        restaurant_ids.append(contract['restaurant_id'])
        citys_ids.append(contract['city_id'])

    activities_map = {}
    if restaurant_activity_ids:
        restaurant_activities = activity_service.get_restaurant_activities(
            restaurant_activity_ids)
        activities_map.update({
            '{}:{}'.format(activity_base.CATEGORY_RESTAURANT_ACTIVITY, activity['id']): activity for activity in restaurant_activities
        })
    if food_activity_ids:
        food_activities = activity_service.get_food_activities(
            food_activity_ids)
        activities_map.update({
            '{}:{}'.format(activity_base.CATEGORY_FOOD_ACTIVITY, activity['id']): activity for activity in food_activities
        })

    restaurants_map = {}
    if restaurant_ids:
        restaurants_map = rst_service.get_restaurants_map(restaurant_ids)

    citys_map = {}
    if citys_ids:
        citys_map = city_service.get_citys_map(citys_ids)

    result = []
    for contract in contracts:
        key = '{}:{}'.format(
            contract['activity_category_id'], contract['activity_id']
        )
        activity = activities_map.get(key, None)
        if activity is None:
            continue

        # more richer contract
        restaurant = restaurants_map.get(contract['restaurant_id'], None)
        contract.update(
            {'_restaurant_name': restaurant['name'] if restaurant else ''}
        )
        city = citys_map.get(contract['city_id'], None)
        contract.update(
            {'_city_name': city['name'] if city else ''}
        )

        # more richer activity (@TODO remove this)
        activity.update({'_name': activity['name']})

        # create result
        result.append({'contract': contract, 'activity': activity})

    return result
