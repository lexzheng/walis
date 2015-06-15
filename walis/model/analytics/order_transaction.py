# coding=utf8

from __future__ import absolute_import, division, print_function
from geoalchemy2 import (
    Geography,
    Geometry,
    WKBElement,
)
from sqlalchemy import (
    Column,
    Integer,
    Numeric,
    BigInteger,
    DateTime)
from walis.model import ModelBase
from walis.utils.wkb import (
    SRID,
    WKBWriter,
)


class OrderTransaction(ModelBase):
    __tablename__ = "dw_trd_order_shanghai"

    order_id = Column(BigInteger, primary_key=True)
    status = Column(Integer)
    created_at = Column(DateTime(timezone=True))
    city_id = Column(Integer)
    total = Column(Numeric(38, 10))
    geohash = Column(Integer)
    # pylint: disable=E1123,E1120
    # loc = Column(Geography(geometry_type="POINT", srid=SRID))
    # pylint: enable=E1123,E1120
    loc = Column(Geometry("POINT", SRID))

    @property
    def location(self):
        return self.loc

    @location.setter
    def location(self, l):
        self.loc = WKBElement(WKBWriter(l).wkb, srid=SRID)
