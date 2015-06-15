#!/usr/bin/env python2
# -*- coding: utf8 -*-

from __future__ import division, print_function, absolute_import

from flask import request

from walis.utils.dirty import fix_food_json_f2b
from walis.thirdparty import thrift_client, thirdparty_svc

def post_or_put(food_id=None):
    if food_id is not None:
        food_id = int(food_id)
    food_json = request.json
    fix_food_json_f2b(food_json)
    with thrift_client('ers') as ers:
        food = thirdparty_svc.ers.TFood()
        for k, v in food_json.iteritems():
            if k in food.__dict__:
                setattr(food, k, v)
        result = ers.save_food(food_id, food)
        return {'id': result}
