#!/usr/bin/env python2
# -*- coding: utf8 -*-

from __future__ import division, print_function, absolute_import

from flask import request
from walis.thirdparty import thrift_client

def get(food_id):
    food_id = int(food_id)
    # todo image_size未使用!
    image_size = request.args.get('image_size', None)
    with thrift_client('ers') as ers:
        food = ers.master_get_food(food_id)
        image_hash = food.image_hash
        image_path = ''
        if image_hash:
            with thrift_client('fuss') as fuss:
                image_path = fuss.file_get_sized(image_hash, image_size)
    return image_path
