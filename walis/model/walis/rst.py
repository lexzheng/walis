#!/usr/bin/env python2
# -*- coding: utf8 -*-

from __future__ import absolute_import, division, print_function

import datetime

from sqlalchemy import Column, Integer, DateTime, \
    SmallInteger, BigInteger, String, Numeric, UnicodeText, Time

from walis.model.walis import ModelBase, DBSession as Session, walis_session
from walis.thrift.utils import jvs_thrift
from walis.utils.model import (
    serialize_to_ttype,
    ttype_to_obj,
    t_time_to_time,
    t_timestamp_to_datetime,
)
from walis.exception.util import raise_user_exc
from walis.exception.error_code import (
    BANKCARD_STATUS_INVALID,
    BANKCARD_UPDATE_ERR
)

DEFAULT_RECORD_LIMIT = 10

class CertificationProcessingRecord(ModelBase):
    __tablename__ = 'certification_processing_record'

    id = Column(Integer, primary_key=True)
    process_user_id = Column(BigInteger, default=-1)
    restaurant_id = Column(BigInteger)
    certification_type = Column(SmallInteger)
    status_from = Column(SmallInteger)
    status_to = Column(SmallInteger)
    created_at = Column(DateTime, default=datetime.datetime.now)
    comment = Column(String, default=u'')

    @classmethod
    def add(cls, process_user_id, restaurant_id, certification_type,
            status_from, status_to, comment):
        processing_record = cls(
            process_user_id=process_user_id,
            restaurant_id=restaurant_id,
            certification_type=certification_type,
            status_from=status_from,
            status_to=status_to,
            comment=comment
        )
        Session().add(processing_record)

    @classmethod
    def get_by_restaurant_id(cls, restaurant_id):
        with walis_session() as session:
            return session.query(cls).filter(
                cls.restaurant_id == restaurant_id). \
                order_by(cls.created_at.asc()).all()

    @classmethod
    def get_latest_record(cls, restaurant_id, status_to=None):
        with walis_session() as session:
            query = session.query(cls).filter(
                cls.restaurant_id == restaurant_id).order_by(
                cls.created_at.desc())

            if status_to:
                query.filter(cls.status_to == status_to)
            return query.first()

    @classmethod
    def mget_latest_record(cls,restaurant_ids,status_to=None):
        with walis_session() as session:
            # subquery order by created_at, the first one of each restaurant will be pick up when group by
            subquery = session.query(cls).order_by(cls.created_at.desc()).subquery()
            query = session.query(cls, subquery).group_by(subquery.c.restaurant_id)\
                .filter(subquery.c.restaurant_id.in_(restaurant_ids))
            if status_to:
                query.filter(subquery.c.status_to == status_to)
            return query.all()


class RstBankCardProcessingRecord(ModelBase):
    __tablename__ = "restaurant_bankcard_processing_record"

    id = Column(BigInteger, primary_key=True)
    rst_id = Column(BigInteger)
    bankcard_id = Column(BigInteger)
    process_user_id = Column(BigInteger)
    status_to = Column(SmallInteger)
    created_at = Column(DateTime, default=datetime.datetime.now)
    messages = Column(String(100), default='')

    @classmethod
    def add(cls, rst_id, bankcard_id, messages, process_user_id, status_to):
        processing_record = cls(
            rst_id=rst_id,
            bankcard_id=bankcard_id,
            messages=messages,
            process_user_id=process_user_id,
            status_to=status_to,
        )
        Session().add(processing_record)

    @classmethod
    def query(cls, rst_id, bankcard_id, limit=DEFAULT_RECORD_LIMIT):
        query = Session().query(cls)
        query = query.filter(cls.bankcard_id == bankcard_id)\
            .filter(cls.rst_id == rst_id)\
            .order_by(cls.created_at.desc())
        query = query.limit(limit)
        return query.all()

    @classmethod
    def mget_last_record(cls, bankcard_ids):
        session = Session()
        subquery = session.query(cls)\
            .order_by(cls.created_at.desc()).subquery()
        query = session.query(cls, subquery).group_by(subquery.c.rst_id)\
            .filter(subquery.c.id.in_(bankcard_ids))
        return query.all()

class RestaurantRecruitment(ModelBase):
    __tablename__ = 'restaurant_recruitment'

    STATUS_UNPROCESSED = 0
    STATUS_PROCESSED = 1

    id = Column(Integer, primary_key=True)
    city_id = Column(Integer, default=-1)
    restaurant_id = Column(Integer, default=-1)
    headcount = Column(Integer, default=0)
    salary = Column(Numeric(10, 2), default=0)
    working_time_start = Column(Time, default=datetime.time(0, 0, 0))
    working_time_end = Column(Time, default=datetime.time(0, 0, 0))
    status = Column(String, default=STATUS_UNPROCESSED)
    comment = Column(UnicodeText, default=u'')
    created_at = Column(DateTime, default=datetime.datetime.now)

    def serialize(self):
        return serialize_to_ttype(self, jvs_thrift.TRestaurantRecruitment)

    @classmethod
    def from_tobj(cls, tobj):
        obj = ttype_to_obj(tobj, cls, exclude=['working_time_start',
                                               'working_time_end',
                                               'created_at'])
        obj.working_time_start = t_time_to_time(tobj.working_time_start)
        obj.working_time_end = t_time_to_time(tobj.working_time_end)
        obj.created_at = t_timestamp_to_datetime(tobj.created_at)
        return obj

class RstBankCard(ModelBase):

    TYPE_NEW = 0
    TYPE_EDIT = 1

    STATUS_PENDING = 0
    STATUS_HISTORY = -1
    STATUS_VALID = 1
    STATUS_INVALID = 2

    __tablename__ = "restaurant_bankcard"
    id = Column(BigInteger, primary_key=True)
    type_code = Column(SmallInteger, default=TYPE_NEW)
    status = Column(SmallInteger, default=STATUS_PENDING)
    rst_id = Column(BigInteger)
    username = Column(String(255))
    mobile = Column(String(20))
    card_id = Column(String(255), default='')
    bank_id = Column(SmallInteger, default=0)
    cardholder_name = Column(String(255), default='')
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(DateTime, default=datetime.datetime.now,
                        onupdate=datetime.datetime.now)
    comment = Column(String(100), default='')
    bankcard_image_front = Column(String(128), nullable=True)
    identity_card_image_front = Column(String(128), nullable=True)
    identity_card_image_back = Column(String(128), nullable=True)
    ol_pay_contract_image = Column(String(128), nullable=True)
    misc_image = Column(String(128), nullable=True)

    @classmethod
    def add(cls, rst_id, username, mobile, card_id, bank_id,
            cardholder_name, type_code,
            bankcard_image_front=None, identity_card_image_front=None,
            identity_card_image_back=None, ol_pay_contract_image=None,
            misc_image=None):
        rst_bankcard = cls(
            rst_id=rst_id, username=username, mobile=mobile,
            card_id=card_id, bank_id=bank_id,
            cardholder_name=cardholder_name,
            type_code=type_code
        )
        rst_bankcard.bankcard_image_front = bankcard_image_front
        rst_bankcard.identity_card_image_back = identity_card_image_back
        rst_bankcard.identity_card_image_front = identity_card_image_front
        rst_bankcard.ol_pay_contract_image = ol_pay_contract_image
        rst_bankcard.misc_image = misc_image

        Session().add(rst_bankcard)
        return rst_bankcard

    @classmethod
    def get(cls, rst_id, id):
        query = Session().query(cls)
        query = query.filter(cls.id == id).filter(cls.rst_id == rst_id)
        return query.first()

    @classmethod
    def query_by_status(cls, rst_ids=None, status=None, type_code=None, offset=0, limit=None,):
        query = Session().query(cls)
        if rst_ids is not None:
            query = query.filter(cls.rst_id.in_(rst_ids))
        if status is not None:
            query = query.filter(cls.status == status)
        if type_code is not None:
            query = query.filter(cls.type_code == type_code)
        query = query.order_by(cls.created_at.desc(), cls.rst_id)
        if offset:
            query = query.offset(offset)
        if limit:
            query = query.limit(limit)
        return query.all()

    @classmethod
    def query_by_rst(cls, rst_id, status=None, offset=0, limit=None):
        query = Session().query(cls)
        query = query.filter(cls.rst_id == rst_id)
        if status is not None:
            query = query.filter(cls.status == status)
        query = query.order_by(cls.updated_at.desc()).order_by(cls.status.desc())
        if offset:
            query = query.offset(offset)
        if limit:
            query = query.limit(limit)
        return query.all()

    @classmethod
    def update(cls, id, **bankcard_dict):
        query = Session().query(cls)
        query = query.filter(cls.id == id)
        rst_bankcard = query.first()
        if not rst_bankcard:
            return ''

        status = bankcard_dict.get('status')
        if status == cls.STATUS_VALID \
                and rst_bankcard.status == cls.STATUS_VALID:
            raise_user_exc(BANKCARD_UPDATE_ERR)

        if rst_bankcard.status == cls.STATUS_HISTORY:
            raise_user_exc(BANKCARD_STATUS_INVALID)

        for k, v in bankcard_dict.iteritems():
            if hasattr(rst_bankcard, k):
                setattr(rst_bankcard, k, v)

        Session().add(rst_bankcard)

    @classmethod
    def get_next(cls, id, status=STATUS_PENDING):
        query = Session().query(cls)
        query = query.filter(cls.status == status)\
            .filter(cls.id < id).order_by(cls.id.desc())
        return query.first()

    @classmethod
    def get_pre(cls, id, status=STATUS_PENDING):
        query = Session().query(cls)
        query = query.filter(cls.status == status)\
            .filter(cls.id > id).order_by(cls.id)
        return query.first()

    @classmethod
    def count(cls, rst_ids=None, status=None, type_code=None):
        query = Session().query(cls)

        if rst_ids is not None:
            query = query.filter(cls.rst_id.in_(rst_ids))
        if status is not None:
            query = query.filter(cls.status == status)
        if type_code is not None:
            query = query.filter(cls.type_code == type_code)
        return query.count()
