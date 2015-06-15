#!/usr/bin/env python2
# coding=utf8

from __future__ import absolute_import, division, print_function

from walis.thirdparty import thrift_client, thirdparty_svc


def query_contract(condition):
    with thrift_client('ers') as ers:
        return ers.query_activity_subsidy_contract(condition)


def count_contract(condition):
    condition.offset = None
    condition.limit = None
    with thrift_client('ers') as ers:
        return ers.count_activity_subsidy_contract(condition)


def create_contract_query_condition(city_ids=None, activity_category_id=None, restaurant_ids=None, status=None,
                                    created_at_from=None, offset=None, limit=thirdparty_svc.ers.DEFAULT_LIST_SIZE):
    condition = thirdparty_svc.ers.TActivitySubsidyContractQuery()

    if city_ids is not None:
        condition.city_ids = city_ids

    if activity_category_id is not None:
        condition.activity_category_id = activity_category_id

    if restaurant_ids is not None:
        condition.restaurant_ids = restaurant_ids

    if status is not None:
        condition.statuses = status if type(status) is list else [status, ]

    if created_at_from is not None:
        condition.created_at_from = created_at_from

    if offset is not None:
        condition.offset = offset

    if limit is not None:
        condition.limit = min(limit, thirdparty_svc.ers.MAX_LIST_SIZE)

    return condition
