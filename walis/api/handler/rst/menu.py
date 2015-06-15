#!/usr/bin/env python2
# -*- coding: utf8 -*-

from __future__ import division, print_function, absolute_import

import datetime
import copy

from flask import request

from walis.thirdparty import thrift_client, thirdparty_svc
from walis.utils.http import Arg, args_parser, jsonpickle_dumps
from walis.utils.dirty import fix_food_b2f
from walis.api.handler.rst.utils import parse_args1

def food_activity_map():
    restaurant_ids, category_ids, food_ids, restaurant_id, category_id, \
    food_id = parse_args1()
    _food_ids = copy.copy(food_ids)
    with thrift_client('ers') as ers:
        if not category_ids and not food_ids and len(restaurant_ids) == 1:
            _map = ers.get_weekday_food_activity_id_map([], restaurant_id)
        else:
            for _id in restaurant_ids:
                food_query = thirdparty_svc.ers.TFoodQuery()
                food_query.restaurant_id = _id
                food_query.is_valid = True
                food_query.limit = 1000
                foods = ers.query_food(food_query)
                _food_ids.extend([food.id for food in foods])
            for _id in category_ids:
                food_query = thirdparty_svc.ers.TFoodQuery()
                food_query.category_id = _id
                food_query.is_valid = True
                food_query.limit = 1000
                foods = ers.query_food(food_query)
                _food_ids.extend([food.id for food in foods])
            _food_ids = list(set(_food_ids))
            _map = ers.get_weekday_food_activity_id_map(_food_ids, None)
        return _map


def available_food_activity():
    """
    获取当前可以设置的食物活动
    """
    # ...这个接口对应的zeus接口歧义太锤子了...
    args_spec = {
        'city_id':Arg(int,default=None),
        'city_ids':Arg(default=[]),
        'restaurant_id':Arg(int,default=None),
        'restaurant_ids':Arg(default=[]),
    }
    args = args_parser.parse(args_spec)
    city_id = args['city_id']
    city_ids = args['city_ids']
    if city_id:
        city_ids.append(city_id)
    restaurant_id = args['restaurant_id']
    restaurant_ids = args['restaurant_ids']
    if restaurant_id:
        restaurant_ids.append(restaurant_id)
    # attention,这里接口跟zeus的略不一致.
    if restaurant_id and not city_id:
        with thrift_client('ers') as ers:
            restaurant = ers.get(restaurant_id)
            city_id = restaurant.city_id
            if city_id not in city_ids:
                city_ids.append(city_id)
    #
    now_str = str(datetime.datetime.now()).split()[0]
    results = {}
    with thrift_client('ers') as ers:
        for x in range(0, 8):
            query = thirdparty_svc.ers.TFoodActivityQuery()
            query.city_ids = city_ids
            query.weekday = [x, ]
            # query.begin_date = now_str
            query.end_date = now_str
            query.is_valid = True
            result = ers.query_food_activity(query)
            for activity in result:
                results[activity.id] = activity
    activities = results.values()
    return activities


def set_food_activity():
    """
    设置食物活动
    """
    restaurant_ids, category_ids, food_ids, restaurant_id, category_id, \
    food_id = parse_args1()
    _food_ids = copy.copy(food_ids)
    with thrift_client('ers') as ers:
        for _id in restaurant_ids:
            food_query = thirdparty_svc.ers.TFoodQuery()
            food_query.restaurant_id = _id
            food_query.is_valid = True
            food_query.limit = 1000
            foods = ers.query_food(food_query)
            _food_ids.extend([food.id for food in foods])
        for _id in category_ids:
            food_query = thirdparty_svc.ers.TFoodQuery()
            food_query.category_id = _id
            food_query.is_valid = True
            food_query.limit = 1000
            foods = ers.query_food(food_query)
            _food_ids.extend([food.id for food in foods])
    _food_ids = list(set(_food_ids))
    act_id = request.json.get('activity_id', None)
    weekdays = request.json.get('weekdays', [])
    with thrift_client('ers') as ers:
        if act_id:
            ers.add_food_activity(act_id, _food_ids, weekdays)
        else:
            ers.clear_food_activity(_food_ids, weekdays)
    return ''


def set_discount():
    """
    设置食物折扣
    """
    restaurant_ids, category_ids, food_ids, restaurant_id, category_id, \
    food_id = parse_args1()
    discount = float(request.json['discount'])
    with thrift_client('ers') as ers:
        for _id in restaurant_ids:
            ers.set_restaurant_food_eleme_buy_discount(_id, discount)
        _food_ids = copy.copy(food_ids)
        for _id in category_ids:
            food_query = thirdparty_svc.ers.TFoodQuery()
            food_query.category_id = _id
            food_query.is_valid = True
            food_query.limit = 1000
            foods = ers.query_food(food_query)
            _food_ids.extend([food.id for food in foods])
        foods = ers.mget_food(_food_ids)
        for food in foods:
            fix_food_b2f(food)
            food.attribute['eleme_buy_discount'] = discount
            food.attribute = jsonpickle_dumps(food.attribute)
            for k in food.__dict__.iterkeys():
                if k not in ['id', 'attribute']:
                    setattr(food, k, None)
            result = ers.save_food(food.id, food)
    return ''


def set_stock_full():
    """
    设置食物库存为最大值(置满)
    """
    return _set_stock(True)


def set_stock_empty():
    """
    设置食物库存为空(置空)
    """
    return _set_stock(False)


def batch_add_menu():
    """
    按照一定格式批量编辑菜单.
    """
    menu = request.json['menu']
    restaurant_id = request.json['restaurant_id']
    new_categories_name = set([category for name, price, category in menu
                               if isinstance(category, basestring)])
    category_id_map = {}
    new_foods = []
    new_categories = []
    with thrift_client('ers') as ers:
        for new_category_name in new_categories_name:
            category = thirdparty_svc.ers.TFoodCategory()
            category.name = new_category_name
            category.restaurant_id = restaurant_id
            category.weight = 0
            new_category_id = ers.save_food_category(None, category)
            new_category = ers.get_food_category(new_category_id)
            new_categories.append(new_category)
            category_id_map[new_category_name] = new_category_id
        for name, price, category in menu:
            if not name and not price:
                continue
            if isinstance(category, basestring):
                category = category_id_map[category]
            food = thirdparty_svc.ers.TFood()
            food.name = name
            food.price = price
            food.restaurant_id = restaurant_id
            food.category_id = category
            new_food_id = ers.save_food(None, food)
            new_food = ers.master_get_food(new_food_id)
            new_foods.append(new_food)
    other_foods = []
    for category in new_categories:
        category._foods = []
    new_category_id_map = {c.id: c for c in new_categories}
    for food in new_foods:
        fix_food_b2f(food)
        if food.category_id in new_category_id_map.keys():
            new_category_id_map[food.category_id]._foods.append(food)
        else:
            other_foods.append(food)
    result = [
        {'food_category': category, 'foods': copy.copy(category._foods)}
        for category in new_categories]
    for category in new_categories:
        category._activity = [None]*7
    if other_foods:
        result.append({'foods': other_foods})
    for category in new_categories:
        delattr(category, '_foods')
    return result


def set_packing_fee():
    """
    设置餐盒费
    """
    restaurant_ids, category_ids, food_ids, restaurant_id, category_id, \
    food_id = parse_args1()
    packing_fee = request.json['packing_fee']
    _food_ids = copy.copy(food_ids)
    with thrift_client('ers') as ers:
        for _restaurant_id in restaurant_ids:
            food_query = thirdparty_svc.ers.TFoodQuery()
            food_query.restaurant_id = _restaurant_id
            food_query.is_valid = True
            food_query.limit = 1000
            foods = ers.query_food(food_query)
            _food_ids.extend([_food.id for _food in foods])
        for _category_id in category_ids:
            food_query = thirdparty_svc.ers.TFoodQuery()
            food_query.category_id = _category_id
            food_query.is_valid = True
            food_query.limit = 1000
            foods = ers.query_food(food_query)
            _food_ids.extend([_food.id for _food in foods])
        for _food_id in set(_food_ids):
            food = thirdparty_svc.ers.TFood()
            food.packing_fee = packing_fee
            result = ers.save_food(_food_id, food)
    return ''

# todo move to base
def _set_stock(is_max):
    restaurant_ids, category_ids, food_ids, restaurant_id, category_id, \
    food_id = parse_args1()
    with thrift_client('ers') as ers:
        _category_ids = copy.copy(category_ids)
        categories = ers.query_food_category_by_restaurant(restaurant_id)
        _category_ids.extend([c.id for c in categories])
        for _category_id in _category_ids:
            ers.mset_food_stock_by_category(_category_id, is_max)
        for _food_id in food_ids:
            ers.mset_food_stock_by_food_ids(_food_id, is_max)
    return ''