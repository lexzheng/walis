#!/usr/bin/env python2
# coding=utf8

from __future__ import absolute_import, division, print_function
from walis.thirdparty import (
    thrift_client,
    thirdparty_svc,
)


def gets():
    with thrift_client('ers') as ers:
        return ers.query_amended_poi(None, None)


def save(poi_dict):
    return update(None, poi_dict)


def update(id, poi_dict):
    t_poi = thirdparty_svc.ers.TAmendedPoi()
    for k, v in poi_dict.items():
        setattr(t_poi, k, v)

    with thrift_client('ers') as ers:
        ers.save_amended_poi(id, t_poi)

    return ''
