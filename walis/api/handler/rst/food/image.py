#!/usr/bin/env python2
# -*- coding: utf8 -*-

from __future__ import division, print_function, absolute_import

import os

from flask import request

from walis.thirdparty import thrift_client, thirdparty_svc
from walis.service.rst.food import image as food_image_base

from walis.exception.util import raise_server_exc
from walis.exception.error_code import IMAGE_UPLOAD_ERR

def get(food_id):
    image_path = food_image_base.get(food_id)
    return {'image_url':image_path}

def put(food_id):
    food_id = int(food_id)
    with thrift_client('fuss') as fuss:
        image_file = request.files['image']
        # image_file_name = secure_filename(image_file.filename)
        #todo fix it...中文文件名错误
        image_file_name = image_file.filename
        ext = os.path.splitext(image_file_name)[1]
        ext = ext.lstrip('.')
        fuss_file = thirdparty_svc.fuss.FussFile()
        fuss_file.content = image_file.stream.read()
        fuss_file.extension = ext
        sizes = [(640, 480), (240, 180), (190, 142)]
        image_hash = fuss.file_upload_sized_with_watermarker(fuss_file,
                                                            sizes)
        #todo temp
        if not image_hash:
            raise_server_exc(IMAGE_UPLOAD_ERR)
    with thrift_client('ers') as ers:
        food = thirdparty_svc.ers.TFood()
        food.image_hash = image_hash
        food_id = ers.save_food(food_id,food)
    return ''

def delete(food_id):
    food_id = int(food_id)
    with thrift_client('ers') as ers:
        food = thirdparty_svc.ers.TFood()
        food.image_hash = ''
        result = ers.save_food(food_id, food)
    return ''
