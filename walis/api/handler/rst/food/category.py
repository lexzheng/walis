#!/usr/bin/env python2
# -*- coding: utf8 -*-

from __future__ import print_function, division, absolute_import

from flask import request

from walis.service.rst.food import category as category_base
from walis.thirdparty import thrift_client, thirdparty_svc
from walis.api.handler.rst.utils import get_activity_ids

from walis.utils.dirty import fix_food_b2f

def post():
    return category_base.post_or_put()

def get(category_id):
    category_id = int(category_id)
    with thrift_client('ers') as ers:
        category = ers.get_food_category(category_id)
        return category

def put(category_id):
    category_base.post_or_put(category_id)
    return ''

def delete(category_id):
    category_id = int(category_id)
    with thrift_client('ers') as ers:
        result = ers.remove_food_category(category_id)
        return ''

def with_activity(category_id):
    """
    获取食物分类(连同对应的活动)
    """
    category_id = int(category_id)
    with thrift_client('ers') as ers:
        food_query = thirdparty_svc.ers.TFoodQuery()
        food_query.category_id = category_id
        food_query.is_valid = True
        food_query.limit = 1000
        foods = ers.query_food(food_query)
        food_category = ers.get_food_category(category_id)
        _activity_ids = get_activity_ids(foods)
        # _activities = _week_activity_ids_to_full(_activity_ids)
        food_category._activity = _activity_ids
        return food_category

def foods(category_id):
    """
    获取食物分类下的所有食物
    """
    category_id = int(category_id)
    foods = category_base.foods(category_id)
    for food in foods:
        fix_food_b2f(food)
    return foods

def activity(category_id):
    """
    获取食物分类对应的活动
    """
    category_id = int(category_id)
    with thrift_client('ers') as ers:
        food_query = thirdparty_svc.ers.TFoodQuery()
        food_query.category_id = category_id
        food_query.is_valid = True
        food_query.limit = 1000
        foods = ers.query_food(food_query)
        activity_ids = get_activity_ids(foods)
        return activity_ids

def set_position():
    """
    设置食物分类的位置
    """
    category_id = request.json['category_id']
    position = request.json['position']
    with thrift_client('ers') as ers:
        result = ers.set_food_category_position(category_id, position)
        return ''
