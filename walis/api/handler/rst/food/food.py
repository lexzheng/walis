#!/usr/bin/env python2
# -*- coding: utf8 -*-

from __future__ import division, print_function, absolute_import

from flask import request

from walis.utils.dirty import fix_food_b2f
from walis.thirdparty import thrift_client
from walis.service.rst.food import food as food_base

def post():
    return food_base.post_or_put()

def get(food_id):
    food_id = int(food_id)
    with thrift_client('ers') as ers:
        food = ers.master_get_food(food_id)
        fix_food_b2f(food)
        return food

def put(food_id):
    food_base.post_or_put(food_id)
    return ''

def delete(food_id):
    food_id = int(food_id)
    with thrift_client('ers') as ers:
        result = ers.remove_food(food_id)
        return ''

def set_position():
    """
    设置食物排序
    """
    food_id = request.json['food_id']
    position = request.json['position']
    with thrift_client('ers') as ers:
        result = ers.set_food_position(food_id, position)
        return ''
