#!/usr/bin/env python2
# coding=utf8

from __future__ import absolute_import, division, print_function
import datetime

from sqlalchemy import Column, Integer, SmallInteger, Numeric, DateTime, String, \
    Date
from sqlalchemy.sql.functions import count

from walis.model.walis import ModelBase, DBSession, walis_db_handler
from walis.utils.time import (
    get_day_start_timestamp,
    get_day_end_timestamp,
)


JAVIS_MAX_QUERY_LIMIT = 1000
JAVIS_DEFAULT_QUERY_LIMIT = 50


class PaymentNoticeRecord(ModelBase):
    __tablename__ = 'payment_notice_record'

    id = Column(Integer, primary_key=True)
    record_id = Column(Integer)
    phone = Column(String(32))
    restaurant_id = Column(Integer)
    restaurant_name = Column(String(64))
    activity_name = Column(String(200))
    first_date = Column(Date)
    last_date = Column(Date)
    amount = Column(Integer)
    total_subsidy = Column(Numeric(7, 2), default=0)
    process_date = Column(Date)
    card_num_tail = Column(String(32))
    sms_task_id = Column(Integer)
    status = Column(SmallInteger)
    created_at = Column(DateTime, default=datetime.datetime.now)
    update_time = Column(DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)

    STATUS_SENDING = 0
    STATUS_SUCCESS = 1
    STATUS_SMS_FAILED = -1
    STATUS_SMS_TIMEOUT = -2
    STATUS_MOBILE_INVALID = -3

    @classmethod
    def add(cls, record_id, phone, restaurant_id, restaurant_name,
            activity_name, first_date, last_date, amount, total_subsidy,
            process_date, card_num_tail, sms_task_id, status):

        DBSession().add(cls(
            record_id=record_id,
            phone=phone,
            restaurant_id=restaurant_id,
            restaurant_name=restaurant_name,
            activity_name=activity_name,
            first_date=first_date,
            last_date=last_date,
            amount=amount,
            total_subsidy=total_subsidy,
            process_date=process_date,
            card_num_tail=card_num_tail,
            sms_task_id=sms_task_id,
            status=status,
        ))

    def update(self, to_status, update_time):
        self.status = to_status
        self.update_time = update_time

    @classmethod
    def get_by_sms_task_id(cls, sms_task_id):
        return DBSession().query(cls).\
            filter(cls.sms_task_id == sms_task_id).first()

    @classmethod
    @walis_db_handler
    def query(cls, phone=None, restaurant_ids=None, restaurant_name=None,
              activity_name=None, first_date=None, last_date=None,
              statuses=None, offset=None, limit=None):
        q = session.query(cls)
        q = cls._query_filter(q, phone, restaurant_ids, restaurant_name,
                              activity_name, first_date, last_date, statuses,
                              offset)

        if limit is not None:
            q = q.limit(min(limit, JAVIS_MAX_QUERY_LIMIT))
        else:
            q = q.limit(JAVIS_DEFAULT_QUERY_LIMIT)

        return q.all()

    @classmethod
    @walis_db_handler
    def query_count(cls, phone=None, restaurant_ids=None, restaurant_name=None,
                    activity_name=None, first_date=None, last_date=None,
                    statuses=None, **kwargs):
        q = session.query(count(cls.id))
        q = cls._query_filter(q, phone, restaurant_ids, restaurant_name,
                              activity_name, first_date, last_date, statuses)

        return q.scalar()

    @classmethod
    def _query_filter(cls, q, phone=None, restaurant_ids=None,
                      restaurant_name=None, activity_name=None, first_date=None,
                      last_date=None, statuses=None, offset=None):
        if phone is not None:
            q = q.filter(cls.phone == phone)

        if restaurant_ids is not None:
            q = q.filter(cls.restaurant_id.in_(restaurant_ids))

        if restaurant_name is not None:
            q = q.filter(cls.restaurant_name == restaurant_name)

        if activity_name is not None:
            q = q.filter(cls.activity_name == activity_name)

        if first_date is not None:
            q = q.filter(cls.created_at >= get_day_start_timestamp(first_date))

        if last_date is not None:
            q = q.filter(cls.created_at <= get_day_end_timestamp(last_date))

        if statuses is not None:
            q = q.filter(cls.status.in_(statuses))

        if offset is not None:
            q = q.offset(offset)

        return q


class PaymentNoticeReply(ModelBase):
    __tablename__ = 'payment_notice_reply'

    reply_id = Column(Integer, primary_key=True)
    phone_number = Column(String(32))
    message = Column(String(255))
    reply_at = Column(DateTime)
    created_at = Column(DateTime, default=datetime.datetime.now)

    @classmethod
    def get(cls, reply_id):
        return DBSession.query(cls).get(reply_id)

    @classmethod
    def add(cls, reply_id, phone_number, message, reply_at):
        DBSession().add(cls(
            reply_id=reply_id,
            phone_number=phone_number,
            message=message,
            reply_at=reply_at
        ))

    @classmethod
    @walis_db_handler
    def query(cls, phone=None, offset=None, limit=None):
        q = session.query(cls)

        if phone is not None:
            q = q.filter(cls.phone_number == phone)

        if offset is not None:
            q = q.offset(offset)

        if limit is not None:
            q = q.limit(min(limit, JAVIS_MAX_QUERY_LIMIT))
        else:
            q = q.limit(JAVIS_DEFAULT_QUERY_LIMIT)

        return q.all()

    @classmethod
    @walis_db_handler
    def query_count(cls, phone=None, **kwargs):
        q = session.query(count(cls.reply_id))

        if phone is not None:
            q = q.filter(cls.phone_number == phone)

        return q.scalar()
