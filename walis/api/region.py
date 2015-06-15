#!/usr/bin/env python2
# -*- coding: utf8 -*-

from __future__ import absolute_import, division, print_function

from walis.core.api import api
from walis.api.handler.region import (
    city as city_handler,
    zone as zone_handler,
    district as district_handler,
    entry as entry_handler,
    region as region_handler,
    city_manage as city_manage_handler,
    brand as region_brand_handler,
    white_collar as white_collar_handler,
)

from .base import BaseApi


class RegionApi(BaseApi):
    route_base = 'region'
    handler = region_handler

    def post(self):
        return self.handler.post()

    def get(self, pk):
        return self.handler.get(pk)

    def put(self, pk):
        return self.handler.put(pk)

    def delete(self, pk):
        return self.handler.delete(pk)


    @api("/get_regions_by_city_id", methods=['GET', ])
    def get_regions_by_city_id(self):
        self.id = self.handler.get_regions_by_city_id()
        return self.id


class RegionBrandApi(BaseApi):
    route_base = 'region_brand'
    handler = region_brand_handler

    def post(self):
        return self.handler.save()

    def get(self, pk):
        return self.handler.get(pk)

    def put(self, pk):
        return self.handler.update(pk)

    def delete(self, pk):
        return self.handler.delete(pk)

    def gets(self):
        return self.handler.query()


class CityApi(BaseApi):
    route_base = "city"
    handler = city_handler

    # todo mget

    def post(self):
        return self.handler.post()

    def get(self, pk):
        return self.handler.get(pk)

    def put(self, pk):
        return self.handler.put(pk)

    @api('/set_is_valid', methods=['POST'])
    def set_is_valid(self):
        return self.handler.set_is_valid()

    @api('/get_by_user', methods=['GET', ])
    def get_by_user(self):
        return self.handler.get_by_user()

    @api('get_all_valid', methods=['GET', ])
    def get_all_valid(self):
        return self.handler.get_all_valid()

    @api('/get_all_by_user_with_alphabet')
    def get_all_by_user_with_alphabet(self):
        return self.handler.get_all_by_user_with_alphabet()

    @api('/<int:city_id>/region')
    def get_region(self, city_id):
        return city_handler.get_regions_by_city_id(city_id)


class DistrictApi(BaseApi):
    route_base = "district"
    handler = district_handler

    def post(self):
        return self.handler.post()

    def get(self, pk):
        return self.handler.get(pk)

    def put(self, pk):
        return self.handler.put(pk)

    @api('/set_is_valid', methods=['POST'])
    def set_is_valid(self):
        return self.handler.set_is_valid()


class ZoneApi(BaseApi):
    route_base = "zone"
    handler = zone_handler

    def post(self):
        return self.handler.post()

    def get(self, pk):
        return self.handler.get(pk)

    def put(self, pk):
        return self.handler.put(pk)

    @api('/set_is_valid', methods=['POST'])
    def set_is_valid(self):
        return self.handler.set_is_valid()


class EntryApi(BaseApi):
    route_base = "entry"
    handler = entry_handler

    def post(self):
        return self.handler.post()

    def get(self, pk):
        return self.handler.get(pk)

    def put(self, pk):
        return self.handler.put(pk)

    @api('/set_is_valid', methods=['POST'])
    def set_is_valid(self):
        return self.handler.set_is_valid()


class WhiteCollarBuildingApi(BaseApi):
    route_base = 'region'
    handler = white_collar_handler

    @api('/building', methods=['POST'])
    def get_building_list(self):
        return self.handler.get_building_list_by_area()


######################################################
# 和区域相关的业务API
######################################################


class CityManageApi(BaseApi):
    route_base = "/city_manage/city"
    handler = city_manage_handler

    def post(self):
        return self.handler.post()

    def get(self, pk=None):
        return self.handler.get(pk)

    def gets(self):
        return self.handler.gets()

    def put(self, pk):
        return self.handler.put(pk)
