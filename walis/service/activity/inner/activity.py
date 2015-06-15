#!/usr/bin/env python2
# coding=utf8

from __future__ import absolute_import, division, print_function

from walis.thirdparty import thrift_client, thirdparty_svc

CATEGORY_RESTAURANT_ACTIVITY = thirdparty_svc.ers.SubsidyConst.CATEGORY_RESTAURANT_ACTIVITY
CATEGORY_FOOD_ACTIVITY = thirdparty_svc.ers.SubsidyConst.CATEGORY_FOOD_ACTIVITY


def mget_restaurant_activities(ids):
    with thrift_client('ers') as ers:
        return ers.mget_restaurant_activity(ids)


def mget_food_activities(ids):
    with thrift_client('ers') as ers:
        return ers.mget_food_activity(ids)
