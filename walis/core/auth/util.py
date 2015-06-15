#!/usr/bin/env python2
# coding=utf8

from __future__ import absolute_import, division, print_function

superadmin = ['superadmin']

# 风控组权限
risk_service_manager = ['risk_service_manager']

# 市场经理权限
directors = [
    'region_director',
    'city_director',
    'entry_director']

# 客服权限
customer_service = [
    'customer_service_director',
    'customer_service']

# Deprecated
# 合同客服权限
contract_customer = ['contract_customer_service',
    'contract_customer_service_manager']

# 活动管理员
activity_manager = [
    'activity_manager', ]

# 财务人员权限
finance = [
    'finance_mananger',
    'finance_teller']

# File access auth
file_auth = [
    'city_director',
    'region_director',
    'entry_director',
    'customer_service_director',
    'customer_service',
    'finance_mananger',
    'finance_teller',
]


def union(*args):
    if not args:
        return []

    return list(reduce(lambda l1, l2: set(l1) | set(l2), args))
