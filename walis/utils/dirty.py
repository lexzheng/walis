#!/usr/bin/env python2
# -*- coding: utf8 -*-

"""
    This py file should be remove the future
"""

import math
import json
import __builtin__

from walis.thirdparty import thrift_client
from walis.utils.http import jsonpickle_dumps
from walis.utils.misc import any_to_raw, dic_to_tobj


_food_tags_fields = ['is_new', 'is_featured', 'is_gum', 'is_spicy']


def fix_food_b2f(food):
    from walis.api.handler.rst.food import image as food_image_handler

    try:
        food.attribute = json.loads(food.attribute)
    except:
        food.attribute = {}
    if not isinstance(food.attribute, dict):
        food.attribute = {}
    try:
        food._image_url = food_image_handler.get(food.id)['image_url']
    except:
        food._image_url = None
    try:
        if math.isnan(food.attribute.get('eleme_buy_discount', None)):
            food.attribute.pop('eleme_buy_discount', None)
    except:
        pass
    food.attribute.setdefault('eleme_buy_discount', None)
    # _tags = []
    # for field in _food_tags_fields:
    # if getattr(food,field,0):
    #         _tags.append(field)
    # food.__setattr__('_tags',_tags)


def fix_food_json_f2b(food_json):
    read_only_attrs = [
        'icons',
        'recent_num_ratings',
        'recent_rating',
    ]
    del_attrs = ['sort_order', '_image_url']
    for _attr in read_only_attrs + del_attrs:
        food_json.pop(_attr, None)
    if 'attribute' in food_json:
        attribute = food_json.get('attribute', {})
        if 'eleme_buy_discount' in attribute:
            discount = attribute['eleme_buy_discount']
            if discount is not None:
                if not 0 <= discount <= 1:
                    # todo raise error-.-
                    attribute.pop('eleme_buy_discount', None)
            else:
                attribute.pop('eleme_buy_discount', None)
        food_json['attribute'] = jsonpickle_dumps(food_json['attribute'])


def fix_food_category_json_f2b(food_category_json):
    read_only_attrs = ['attribute_list']
    del_attrs = ['weight']
    for _attr in read_only_attrs + del_attrs:
        food_category_json.pop(_attr, None)


def fix_restaurant_attribute(restaurant):
    try:
        restaurant.attribute = json.loads(restaurant.attribute)
    except:
        restaurant.attribute = {}
    if not isinstance(restaurant.attribute, dict):
        restaurant.attribute = {}


def zeus_query(service, func_name, query_type, **kwargs):
    """
    这个-.-额.等把第一个参数和第二个参数和在一起把...
    """
    with thrift_client(service) as client:
        func = getattr(client, func_name)
        q = dic_to_tobj(kwargs, query_type)
        result = func(q)
        result = any_to_raw(result)
        return result


def setdefault(obj, name, value):
    # __getattribute__?__getattr__,in __dict__ in __slot__
    # 其他实现方法?且不出错?
    # 补上异常处理
    try:
        exec '{}.{}'.format(obj, name)
    except:
        setattr(obj, name, value)


# def setdefault(obj,):

def setattr(object, name, value):
    return __builtin__.setattr(object, name, value)


def tobj_fields_process(tobj, includes=None, excludes=None):
    tobj_fields = tobj.__dict__.keys()
    # 先白后黑
    if includes is not None:
        excludes = set(tobj_fields) - set(includes)
    if excludes is not None:
        [delattr(tobj, field) for field in excludes]
        return tobj
    return tobj


def dic_fields_process(dic, includes=None, excludes=None):
    fields = dic.keys()
    # 先白后黑
    if includes is not None:
        excludes = set(fields) - set(includes)
    if excludes is not None:
        [dic.pop(field, None) for field in excludes]
    return dic


from xpinyin import Pinyin

pinyin = Pinyin()


def get_current_user_id():
    from flask.ext.login import current_user

    return current_user.id


def ess_search2(index, doc_type, query):
    with thrift_client('ess') as ess_client:
        result = ess_client.search2(index, doc_type, query)
    result = json.loads(result)
    return result


def extract_ess_search_result(ess_search_result):
    hits = ess_search_result['hits']
    objects = []
    for entity in hits:
        source = entity['_source']
        entity.pop('_source')
        source.update(entity)
        objects.append(source)
    total = ess_search_result['total']
    result = {
        'objects': objects,
        'total': total,
    }
    return result
