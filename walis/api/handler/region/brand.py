#!/usr/bin/env python2
# -*- coding: utf8 -*-

from __future__ import absolute_import, division, print_function
import json

import geojson
from flask.ext.login import current_user

from walis.exception.util import raise_user_exc, raise_auth_exc
from walis.exception.error_code import (
    REGION_INVALID,
    REGION_TYPE_INVALID,
    AUTH_FAILED_ERROR,
)
from walis.service.region import brand as region_brand


from walis.utils.http import args_parser, Arg

from walis.model.walis.region import RegionBrand
from walis.model.walis import db_commit


@db_commit
def save():
    args_spec = {
        'city_id': Arg(int, required=True),
        'type_code': Arg(int, required=True),
        'area': Arg(dict, required=True),
        'name': Arg(unicode, required=True),
    }
    args = args_parser.parse(args_spec)

    if not city_permission(args.get('city_id')):
        raise_auth_exc(AUTH_FAILED_ERROR)

    _check_region_type(args.get('type_code'))
    _check_region_json(args.get('area'))

    args.update(area=json.dumps(args['area']))
    result = region_brand.save(**args)
    return result


@db_commit
def update(pk):
    args_spec = {
        'city_id': Arg(int),
        'type_code': Arg(int),
        'area': Arg(dict),
        'name': Arg(unicode),
    }
    args = args_parser.parse(args_spec)

    pk = int(pk)
    if not region_permission(pk):
        raise_auth_exc(AUTH_FAILED_ERROR)

    _check_region_type(args.get('type_code'))
    _check_region_json(args.get('area'))

    if args.get('area', None) is not None:
        args.update(area=json.dumps(args['area']))
    result = region_brand.update(pk, **args)
    return result


def get(pk):
    pk = int(pk)
    if not region_permission(pk):
        raise_auth_exc(AUTH_FAILED_ERROR)

    rb = region_brand.get(pk)
    if not rb:
        return {}

    return {
        'id': rb.id,
        'name': rb.name,
        'type_code': rb.type_code,
        'city_id': rb.city_id,
        'area': rb.area,
        'created_at': rb.created_at
    }


@db_commit
def delete(pk):
    pk = int(pk)
    if not region_permission(pk):
        raise_auth_exc(AUTH_FAILED_ERROR)

    result = region_brand.delete(pk)
    return result


def query():
    args_spec = {
        'city_id': Arg(int),
    }
    args = args_parser.parse(args_spec)

    result = []
    rbs = region_brand.query(**args)
    for rb in rbs:
        result.append({
            'id': rb.id,
            'name': rb.name,
            'type_code': rb.type_code,
            'city_id': rb.city_id,
            'area': rb.area,
            'created_at': rb.created_at
        })
    return result


def _check_region_type(type_code):
    if type_code is not None:
        if int(type_code) not in (RegionBrand.TYPE_CBD, RegionBrand.TYPE_SCHOOL):
            raise_user_exc(REGION_TYPE_INVALID)

    return True


def _check_region_json(area):
    if area is not None:
        try:
            geojson.loads(json.dumps(area))
        except ValueError:
            raise_user_exc(REGION_INVALID)

    return True


def city_permission(city_id):
    if current_user.is_super_admin():
        return True

    if city_id in current_user.city_ids:
        return True

    return False


def region_permission(region_id):
    if current_user.is_super_admin():
        return True

    if region_id in current_user.region_ids:
        return True
    elif current_user.city_ids:
        city_id = region_brand.get(region_id)['city_id']
        if city_permission(city_id):
            return True

    return False
