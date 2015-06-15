#!/usr/bin/env python2
# -*- coding: utf8 -*-

from __future__ import absolute_import, division, print_function

from walis.model.walis.region import RegionBrand


def save(name, type_code, city_id, area):
    return RegionBrand.save(name, type_code, city_id, area)


def update(id, name=None, type_code=None, city_id=None, area=None):
    return RegionBrand.update(id, name, type_code, city_id, area)


def get(id):
    return RegionBrand.get(id)


def query(city_id=None, offset=None, limit=None):
    return RegionBrand.query(city_id, offset, limit)


def delete(id):
    return RegionBrand.delete(id)
