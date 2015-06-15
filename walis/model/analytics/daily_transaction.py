#! /usr/bin/env python2
# -*- coding:utf-8 -*-

from __future__ import absolute_import, division, print_function


from sqlalchemy import Column, Integer, Date, String, Numeric

from walis.model import (
    WalisModel,
    ModelBase,
)


class RstDailyTransaction(WalisModel, ModelBase):
    __tablename__ = 'st_trd_restaurant_sale_res'

    order_date = Column(Date, primary_key=True)
    restaurant_id = Column(Integer, primary_key=True)
    restaurant_name = Column(String(200))
    city_id = Column(Integer)
    region_id = Column(Integer)
    type_code = Column(Integer)
    is_valid = Column(Integer)
    is_saas = Column(Integer)
    saas_status = Column(Integer)
    order_mode = Column(Integer)
    is_online_payment = Column(Integer)
    has_food_img = Column(Integer)
    has_food_activity = Column(Integer)
    order_amt = Column(Numeric(20, 2))
    order_num = Column(Numeric(10, 2))
    online_order_amt = Column(Numeric(20, 2))
    online_order_num = Column(Numeric(10, 2))
    suspicious_order_num = Column(Numeric(10, 2))
    phone_order_amt = Column(Numeric(20, 2))
    phone_order_num = Column(Numeric(10, 2))
    ts_order_amt = Column(Numeric(20, 2))
    ts_order_num = Column(Numeric(10, 2))
