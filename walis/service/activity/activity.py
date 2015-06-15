#!/usr/bin/env python2
# coding=utf8

from __future__ import absolute_import, division, print_function

from walis.utils.misc import ttype2dict

from walis.service.activity.utils import get_restaurant_activity_name
from walis.service.activity.inner import activity as activity_base


def get_restaurant_activities(ids):
    ids = list(set(ids))
    restaurant_activities = activity_base.mget_restaurant_activities(ids)

    def create_name(acty):
        setattr(acty, 'name', get_restaurant_activity_name(acty))
        return acty
    return [ttype2dict(create_name(activity)) for activity in restaurant_activities]


def get_food_activities(ids):
    ids = list(set(ids))
    food_activities = activity_base.mget_food_activities(ids)
    return [ttype2dict(activity) for activity in food_activities]


def is_restaurant_activity(activity_category_id):
    return activity_category_id == activity_base.CATEGORY_RESTAURANT_ACTIVITY


def is_food_activity(activity_category_id):
    return activity_category_id == activity_base.CATEGORY_FOOD_ACTIVITY
