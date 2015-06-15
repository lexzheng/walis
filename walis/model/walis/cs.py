#!/usr/bin/env python2
# coding=utf8

from __future__ import absolute_import, division, print_function
from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    DateTime,
    BigInteger,
    SmallInteger,
    String,
    Text)
from sqlalchemy.orm import validates
from walis.exception.error_code import DATABASE_VALIDATION_ERROR
from walis.exception.util import raise_server_exc
from . import (
    ModelBase,
    WalisModel,
    db_commit)


class CSEvent(WalisModel, ModelBase):
    __tablename__ = 'cs_event'

    STATUS_PENDING = 0
    STATUS_REMAIN = 1
    STATUS_FOLLOW_UP = 2
    STATUS_FORWARD = 3
    STATUS_DONE = 10
    statuses = [STATUS_PENDING, STATUS_REMAIN, STATUS_FOLLOW_UP,
                STATUS_FORWARD, STATUS_DONE]

    PRIORITY_NORMAL = 0
    PRIORITY_IMPORTANT = 1
    PRIORITY_CRITICAL = 2
    PRIORITY_MOST_CRITICAL = 3
    priorities = [PRIORITY_NORMAL, PRIORITY_IMPORTANT, PRIORITY_CRITICAL,
                  PRIORITY_MOST_CRITICAL]

    USER_TYPE_MERCHANT = 1
    USER_TYPE_MARKETING = 2
    USER_TYPE_USER = 3
    USER_TYPE_OTHERS = 10
    user_types = [USER_TYPE_MERCHANT, USER_TYPE_MARKETING, USER_TYPE_USER,
                  USER_TYPE_OTHERS]

    SOURCE_PHONE = 1
    SOURCE_EMAIL = 2
    SOURCE_WEIBO = 3
    SOURCE_WECHAT = 4
    SOURCE_ONLINE_CS = 5
    SOURCE_FEEDBACK = 6
    SOURCE_OTHERS = 10
    sources = [SOURCE_PHONE, SOURCE_EMAIL, SOURCE_WEIBO, SOURCE_WECHAT,
               SOURCE_ONLINE_CS, SOURCE_FEEDBACK, SOURCE_OTHERS]

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    user_type = Column(SmallInteger)
    user_info = Column(String)
    phone = Column(String, nullable=False)
    priority = Column(SmallInteger)
    source = Column(SmallInteger)
    status = Column(SmallInteger)
    creater_id = Column(Integer)
    handler_id = Column(Integer)
    order_id = Column(BigInteger)
    compensation = Column(Integer, default=0)
    category_l1 = Column(Integer)
    category_l2 = Column(Integer)
    category_l3 = Column(Integer)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    @validates('status')
    def validate_status(self, key, status):
        if status is not None and status not in self.statuses:
            raise_server_exc(DATABASE_VALIDATION_ERROR, key=key, value=status)
        return status

    @validates('priority')
    def validate_priority(self, key, priority):
        if priority is not None and priority not in self.priorities:
            raise_server_exc(
                DATABASE_VALIDATION_ERROR, key=key, value=priority)
        return priority

    @validates('user_type')
    def validate_user_type(self, key, user_type):
        if user_type is not None and user_type not in self.user_types:
            raise_server_exc(
                DATABASE_VALIDATION_ERROR, key=key, value=user_type)
        return user_type

    @validates('source')
    def validate_source(self, key, source):
        if source is not None and source not in self.sources:
            raise_server_exc(DATABASE_VALIDATION_ERROR, key=key, value=source)
        return source

    @db_commit
    def update(self, compensation=None,  status=None, handler_id=None):
        if self.status == CSEvent.STATUS_DONE:
            return None

        if compensation is not None:
            self.compensation = compensation

        if status is not None:
            self.status = status
            if status == CSEvent.STATUS_FORWARD:
                self.handler_id = handler_id

        return self


class CSEventRecord(ModelBase, WalisModel):
    __tablename__ = 'cs_event_record'

    id = Column(Integer, primary_key=True)
    event_id = Column(Integer, nullable=False)
    user_id = Column(Integer)
    content = Column(Text, default='')
    status = Column(SmallInteger)
    created_at = Column(DateTime, default=datetime.now)


class CSEventCategory(ModelBase, WalisModel):
    __tablename__ = 'cs_event_category'

    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, nullable=True)
    name = Column(String, nullable=False)
    is_valid = Column(SmallInteger, default='')

    def update(self, new_name=None, is_valid=None):

        if new_name is not None:
            self.name = new_name

        if is_valid is not None:
            self.is_valid = is_valid

        return self


class CSProcessTypeChangeRecord(ModelBase, WalisModel):
    __tablename__ = 'cs_process_type_change_record'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    from_type = Column(SmallInteger, nullable=False)
    to_type = Column(SmallInteger, nullable=False)
