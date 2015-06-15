#! /usr/bin/env python2
# -*- coding:utf-8 -*-

from __future__ import absolute_import, division, print_function

from walis.service.analytics import inner
from walis.exception.error_code import CITY_NOT_EXISTS
from walis.exception.util import raise_user_exc

from walis.service.region import city as city_service


def gets(city_id=None, offset=inner.DEFALUT_CITY_TRS_CFG_OFFSET, limit=inner.DEFALUT_CITY_TRS_CFG_LIMIT):
    cfg_list = inner.query_trs_query_cfg(city_id, offset, limit)
    return [cfg.to_dict() for cfg in cfg_list]


def add(city_id, date_from, date_end):
    if not _check_city_exists(city_id):
        raise_user_exc(CITY_NOT_EXISTS, city_id)
    trs_query_cfg = inner.add_trs_query_cfg(city_id, date_from, date_end)
    return {'city_transaction_query_config_id': trs_query_cfg.id}


def get_by_city(city_id):
    city_trs_query_config = inner.get_trs_query_cfg_by_city(city_id)
    return city_trs_query_config.to_dict() if city_trs_query_config else city_trs_query_config


def add_or_update(city_id, date_from, date_end):
    if not _check_city_exists(city_id):
        raise_user_exc(CITY_NOT_EXISTS, city_id)
    trs_query_cfg = inner.add_or_update_trs_query_cfg(city_id, date_from, date_end)
    return {'city_transaction_query_config_id': trs_query_cfg.id}


def _check_city_exists(city_id):
    city = city_service.get(city_id)
    return True if city else False
