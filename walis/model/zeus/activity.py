#!/usr/bin/env python2
# coding=utf8

from __future__ import absolute_import, division, print_function
import datetime

from sqlalchemy import Column, Integer, SmallInteger, Numeric, DateTime, String, \
    Date

from walis.model.walis import ModelBase


JAVIS_MAX_QUERY_LIMIT = 1000
JAVIS_DEFAULT_QUERY_LIMIT = 50


# ##################
# zeus models
###################
class SubsidyPayRecord(ModelBase):
    __tablename__ = 'subsidy_pay_record'

    CATEGORY_RESTAURANT_ACTIVITY = 12
    CATEGORY_FOOD_ACTIVITY = 11

    ACTIVITY_COUPON = 3
    ACTIVITY_NEW_USER_DISCOUNT = 7
    ACTIVITY_EXTRA_DISCOUNT = 100

    RESTAURANT_ACTIVITY_LIST = [
        ACTIVITY_COUPON, ACTIVITY_NEW_USER_DISCOUNT, ACTIVITY_EXTRA_DISCOUNT]

    STATUS_PENDING = 1
    STATUS_SUBMITTED = 2
    STATUS_SUCCESS = 3
    STATUS_FAIL = 4

    # column definitions
    id = Column(Integer, primary_key=True)
    restaurant_id = Column(Integer)
    activity_id = Column(Integer)
    activity_category_id = Column(SmallInteger)
    batch_id = Column(Integer, default=-1)
    amount = Column(Numeric(10, 2), default=-1)
    order_count = Column(Integer, default=-1)
    subsidy_count = Column(Integer, default=-1)
    status = Column(SmallInteger, default=STATUS_PENDING)
    created_at = Column(DateTime, default=datetime.datetime.now)


class SubsidyProcessRecord(ModelBase):
    __tablename__ = 'subsidy_process_record'

    STATUS_SUBMITTED = 2
    STATUS_SUCCESS = 3
    STATUS_FAIL = 4

    # column definitions
    id = Column(Integer, primary_key=True)
    pay_record_id = Column(Integer)
    bank_id = Column(SmallInteger)
    cardholder_name = Column(String(255))
    card_id = Column(String(32))
    amount = Column(Numeric(10, 2))
    status = Column(SmallInteger)
    created_at = Column(DateTime, default=datetime.datetime.now)
    processed_at = Column(DateTime, default=datetime.datetime.now)


class ActivityStats(ModelBase):
    __tablename__ = 'activity_stats'

    STATUS_PENDING = 1
    STATUS_NO_SUBSIDY = 2
    STATUS_PAY_RECORD_GENERATED = 3
    STATUS_PAY_SUCCESS = 4
    STATUS_PAY_FAIL = 5
    STATUS_INVALID = 6

    # column definitions
    id = Column(Integer, primary_key=True)
    restaurant_id = Column(Integer)
    activity_id = Column(Integer)
    activity_category_id = Column(SmallInteger)
    city_id = Column(Integer)
    date = Column(Date)
    quantity = Column(Integer)
    discount_amount = Column(Numeric(7, 2))
    total_subsidy = Column(Numeric(7, 2), default=0)
    order_count = Column(Integer)
    status = Column(SmallInteger)
    pay_record_id = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.datetime.now)
