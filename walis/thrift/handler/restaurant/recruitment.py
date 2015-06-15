#!/usr/bin/env python2
# coding=utf8

from __future__ import absolute_import, division, print_function
import json

from flask.ext.restless.search import search as make_search_query

from walis.model.walis import DBSession, db_commit
from walis.model.walis.rst import RestaurantRecruitment


@db_commit
def add_restaurant_recruitment(data):
    s = DBSession()
    obj = RestaurantRecruitment.from_tobj(data)
    s.add(obj)
    s.flush()
    obj_id = obj.id
    return obj_id


def get_restaurant_recruitment(_id):
    obj = DBSession.query(RestaurantRecruitment).get(_id)
    return obj.serialize()


def query_restaurant_recruitment(q):
    s = DBSession()
    search_params = json.loads(q)
    result = make_search_query(s, RestaurantRecruitment, search_params)
    is_single = search_params.get('single', False)
    if is_single:
        result = [result.serialize()]
    else:
        result = [obj.serialize() for obj in result]
    return result


@db_commit
def update_restaurant_recruitment(data):
    s = DBSession()
    obj = RestaurantRecruitment.from_tobj(data)
    # todo 检查data中id是否存在,数据库中对应id是否存在
    s.merge(obj)
    return True


@db_commit
def patch_update_restaurant_recruitment(data):
    obj_json = json.loads(data)
    _id = obj_json['id']
    obj = DBSession().query(RestaurantRecruitment).get(_id)
    for k, v in obj_json.iteritems():
        setattr(obj, k, v)
    return True


@db_commit
def delete_restaurant_recruitment(_id):
    s = DBSession()
    obj = s.query(RestaurantRecruitment).get(_id)
    s.delete(obj)
    s.commit()
    return True