#!/usr/bin/python
# -*- coding:utf-8 -*-

import logging
from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, BigInteger, \
    SmallInteger

from walis.model.walis import ModelBase, DBSession
from walis.thrift.utils import jvs_thrift
from walis.utils.model import serialize_to_ttype


log = logging.getLogger(__name__)


class VoiceOrder(ModelBase):
    __tablename__ = 'voice_order'

    id = Column("id", BigInteger, primary_key=True)
    order_id = Column("order_id", BigInteger)
    sequence_number = Column("sequence_number", Integer)
    status_code = Column("status_code", SmallInteger)
    key_pressed = Column('key_pressed', SmallInteger, default=0)
    created_at = Column("created_at", DateTime)
    call_id = Column("call_id", BigInteger)

    def serialize(self):
        return serialize_to_ttype(self, jvs_thrift.TVoiceOrder)

    @classmethod
    def add(cls, order_id=None, sequence_number=None, status_code=None,
            key_pressed=None, created_at=datetime.now(), call_id=None):
        voice_order = cls(order_id=order_id,
                          sequence_number=sequence_number,
                          status_code=status_code,
                          key_pressed=key_pressed,
                          created_at=created_at,
                          call_id=call_id)
        DBSession().add(voice_order)
        return voice_order

    @classmethod
    def get_by_order_id(cls, order_id):
        return DBSession().query(cls).filter(cls.order_id == order_id).first()

    @classmethod
    def get_by_call_id(cls, call_id):
        return DBSession().query(cls).filter(cls.call_id == call_id).all()


class VoiceCall(ModelBase):
    __tablename__ = 'voice_call'

    STATUS_NOT_DIAL = 0
    STATUS_DIALING = 1
    STATUS_SUCCESS = 2
    STATUS_FAILED = 3  # Out-of-Serivce && Power-off && Disconnected
    STATUS_TTS_FAILED = 4  # TTS transformation failure
    STATUS_EXCEED_CALL_LIMIT = 5  # Failed.[exceed the max call limit]
    STATUS_BANNED = 9

    id = Column("id", BigInteger, primary_key=True)
    restaurant_id = Column("restaurant_id", Integer)
    call_status = Column("call_status", SmallInteger)
    created_at = Column("created_at", DateTime)
    phone = Column("phone", String)

    def update(self, call_status):
        self.call_status = call_status

    @classmethod
    def add(cls, restaurant_id=None, call_status=None,
            created_at=datetime.now(), phone=None, flush=False):
        session = DBSession()
        voice_call = cls(restaurant_id=restaurant_id,
                         call_status=call_status,
                         created_at=created_at,
                         phone=phone)
        session.add(voice_call)
        if flush:
            session.flush()
        return voice_call

    @classmethod
    def get(cls, call_id):
        return DBSession().query(cls).get(call_id)

    @classmethod
    def get_by_status(cls, call_status):
        return DBSession().query(cls).filter(cls.call_status == call_status).all()


class VoicecallBan(ModelBase):
    __tablename__ = 'voicecall_ban'

    BAN_TYPE_TODAY = 1
    BAN_TYPE_FOREVER = 2

    id = Column('id', BigInteger, primary_key=True)
    restaurant_id = Column("restaurant_id", Integer)
    ban_type = Column("ban_type", SmallInteger)
    created_at = Column("created_at", DateTime, default=datetime.now)

    @classmethod
    def add(cls, restaurant_id, ban_type, flush=False):
        session = DBSession()
        exist_ban = cls.get_by_restaurant(restaurant_id)

        if not exist_ban:
            ban = cls(restaurant_id=restaurant_id,
                      ban_type=ban_type)
            session.add(ban)
            if flush:
                session.flush()
            return ban

        return None

    @classmethod
    def get_by_restaurant(cls, restaurant_id):
        return DBSession().query(cls).filter(
            cls.restaurant_id == restaurant_id).first()

    @classmethod
    def mget_by_restaurant_ids(cls, restaurant_ids):
        return DBSession().query(cls).filter(
            cls.restaurant_id.in_(restaurant_ids)).all()

    @classmethod
    def clean_today_ban(cls):
        DBSession().query(cls).filter(
            cls.ban_type == VoicecallBan.BAN_TYPE_TODAY).delete()
