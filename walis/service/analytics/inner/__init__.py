#! /usr/bin/env python2
# -*- coding:utf-8 -*-

from __future__ import absolute_import, division, print_function

from sqlalchemy import func
from walis.model.analytics.order_transaction import OrderTransaction

from walis.model.walis.region import CityTransactionQueryConfig
from walis.model.walis import DBSession, db_commit

from walis.model.analytics.daily_transaction import RstDailyTransaction
from walis.model.analytics import WDBSession, PGSession

DEFALUT_CITY_TRS_CFG_LIMIT = 1000
DEFALUT_CITY_TRS_CFG_OFFSET = 0


#######################
##### trs_query_cfg
#######################

@db_commit
def add_trs_query_cfg(city_id, date_from, date_end):
    city_trs_query_cfg = CityTransactionQueryConfig(city_id=city_id,
                                                    date_from=date_from,
                                                    date_end=date_end)

    DBSession().add(city_trs_query_cfg)
    return city_trs_query_cfg


@db_commit
def _update(trs_query_cfg, **kwargs):
    trs_query_cfg.update(**kwargs)


def get_trs_query_cfg_by_city(city_id):
    q = DBSession().query(CityTransactionQueryConfig)
    q = q.filter(CityTransactionQueryConfig.city_id == city_id)
    return q.first()


def add_or_update_trs_query_cfg(city_id, date_from, date_end):
    trs_query_cfg = get_trs_query_cfg_by_city(city_id)
    if not trs_query_cfg:
        return add_trs_query_cfg(city_id, date_from, date_end)
    else:
        _update(trs_query_cfg, date_from=date_from, date_end=date_end)
        return trs_query_cfg


def query_trs_query_cfg(city_id=None,
                        offset=DEFALUT_CITY_TRS_CFG_OFFSET,
                        limit=DEFALUT_CITY_TRS_CFG_LIMIT):
    if city_id is not None:
        return get_trs_query_cfg_by_city(city_id)
    q = DBSession().query(CityTransactionQueryConfig)
    q = q.offset(offset).limit(limit)
    return q.all()


#############################
##### transaction
#############################
def count_daily_trs(rst_ids, date_from, date_end):
    q = WDBSession().query(func.sum(RstDailyTransaction.order_amt).label('amount'))
    q = q.filter(RstDailyTransaction.restaurant_id.in_(rst_ids))\
        .filter(RstDailyTransaction.order_date >= date_from)\
        .filter(RstDailyTransaction.order_date <= date_end)
    return q.first()


def get_order_transaction(city_id, polygon):
    session = PGSession()
    return session.query(func.sum(OrderTransaction.total)).\
        filter(func.ST_Contains(polygon, OrderTransaction.loc)).scalar()
        # filter(OrderTransaction.city_id == city_id).\

