#!/usr/bin/env python2
# coding=utf8

from __future__ import absolute_import, division, print_function
from walis.service.activity import rst_activity, food_activity
from walis.service.activity.utils import get_restaurant_activity_name
from walis.thirdparty import thirdparty_svc


def get(activity_id, category_id):
    ACTIVITY_CATEGORY = thirdparty_svc.ers.SubsidyConst()
    if category_id == ACTIVITY_CATEGORY.CATEGORY_RESTAURANT_ACTIVITY:
        return rst_activity.get(activity_id)
    elif category_id == ACTIVITY_CATEGORY.CATEGORY_FOOD_ACTIVITY:
        return food_activity.get(activity_id)


def mget(activity_ids, category_id):
    ACTIVITY_CATEGORY = thirdparty_svc.ers.SubsidyConst()
    if category_id == ACTIVITY_CATEGORY.CATEGORY_RESTAURANT_ACTIVITY:
        return rst_activity.mget(activity_ids)
    elif category_id == ACTIVITY_CATEGORY.CATEGORY_FOOD_ACTIVITY:
        return food_activity.mget(activity_ids)


def get_name(activity_id, category_id):
    ACTIVITY_CATEGORY = thirdparty_svc.ers.SubsidyConst()
    if category_id == ACTIVITY_CATEGORY.CATEGORY_RESTAURANT_ACTIVITY:
        restaurant_activity = rst_activity.get(activity_id)
        return get_restaurant_activity_name(restaurant_activity)
    elif category_id == ACTIVITY_CATEGORY.CATEGORY_FOOD_ACTIVITY:
        return food_activity.get(activity_id).name
