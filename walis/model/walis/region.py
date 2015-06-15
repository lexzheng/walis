#!/usr/bin/env python2
# -*- coding: utf8 -*-

from __future__ import absolute_import, division, print_function
from datetime import datetime

from sqlalchemy import Column, Integer, SmallInteger, DateTime, String, Text, Date

from walis.model.walis import ModelBase, DBSession
from walis.model import WalisModel

MAX_QUERY_LIMIT = 1000
DEFAULT_QUERY_LIMIT = 50


class RegionBrand(ModelBase):
    __tablename__ = 'region_brand'

    TYPE_CBD = 1
    TYPE_SCHOOL = 2

    # column definitions
    id = Column(Integer, primary_key=True)
    name = Column(String, default='')
    type_code = Column(SmallInteger, default=0)
    city_id = Column(Integer, default=0)
    area = Column(Text, default='')
    created_at = Column(DateTime, default=datetime.now)

    @classmethod
    def save(cls, name, type_code, city_id, area):
        DBSession().add(cls(
            name=name,
            type_code=type_code,
            city_id=city_id,
            area=area,
        ))

    @classmethod
    def update(cls, pk, name=None, type_code=None, city_id=None, area=None):
        rb = cls.get(pk)
        if name is not None:
            rb.name = name

        if type_code is not None:
            rb.type_code = type_code

        if city_id is not None:
            rb.city_id = city_id

        if area is not None:
            rb.area = area

    @classmethod
    def get(cls, pk):
        return DBSession().query(cls).get(pk)

    @classmethod
    def query(cls, city_id=None, offset=None, limit=DEFAULT_QUERY_LIMIT):
        rb = DBSession().query(cls)

        if city_id is not None:
            rb = rb.filter(cls.city_id == city_id)

        if offset is not None:
            rb = rb.offset(offset)

        if limit is not None:
            rb = rb.limit(min(limit, MAX_QUERY_LIMIT))

        return rb.all()

    @classmethod
    def delete(cls, id):
        DBSession().query(cls).filter(cls.id == id).delete()

class CityTransactionQueryConfig(WalisModel, ModelBase):
    __tablename__ = 'city_transaction_query_config'

    id = Column(Integer, primary_key=True)
    city_id = Column(Integer)
    date_from = Column(Date)
    date_end = Column(Date)

    def update(self, date_from, date_end):
        self.date_from = date_from
        self.date_end = date_end
