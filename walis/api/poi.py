#!/usr/bin/env python2
# coding=utf8

from __future__ import absolute_import, division, print_function
from walis.api.base import BaseApi
from .handler import poi


class AmendedPoiApi(BaseApi):
    route_base = 'amended_poi'

    def get(self):
        return poi.get()

    def post(self):
        return poi.save()

    # TODO change url to 'put(self, id)'
    def put(self):
        return poi.update()

