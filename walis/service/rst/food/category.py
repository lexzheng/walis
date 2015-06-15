#!/usr/bin/env python2
# -*- coding: utf8 -*-

from __future__ import division, print_function, absolute_import

from flask import request

from walis.thirdparty import thrift_client, thirdparty_svc
from walis.utils.dirty import fix_food_category_json_f2b

def post_or_put(category_id=None):
    if category_id is not None:
        category_id = int(category_id)
    category = thirdparty_svc.ers.TFoodCategory()
    category_json = request.json
    fix_food_category_json_f2b(category_json)
    for k, v in category_json.iteritems():
        setattr(category, k, v)
    if category_id is None and category.weight is None:
        category.weight = 0
    with thrift_client('ers') as ers:
        result = ers.save_food_category(category_id, category)
        return {'id': result}


def foods(category_id):
    with thrift_client('ers') as ers:
        food_query = thirdparty_svc.ers.TFoodQuery()
        food_query.category_id = category_id
        food_query.is_valid = True
        food_query.limit = 1000
        foods = ers.query_food(food_query)
        return foods
