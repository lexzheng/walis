#!/usr/bin/env python2
# -*- coding: utf8 -*-

from __future__ import absolute_import, division, print_function

from walis.thirdparty import thrift_client


def get_citys(ids):
    with thrift_client('ers') as ers:
        citys = ers.mget_city(ids)
    return citys.values()
