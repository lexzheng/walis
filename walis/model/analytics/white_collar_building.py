#! /usr/bin/env python2
# -*- coding:utf-8 -*-

from __future__ import division, absolute_import, print_function

import datetime

from sqlalchemy import Column, BigInteger, String, Numeric, DateTime
from sqlalchemy import and_

from walis.model.analytics import WDBSession as DBSession
from walis.model import ModelBase
from walis.utils.geo import is_in_region


class WhiteCollarBuilding(ModelBase):

    __tablename__ = "dim_gis_building_detail"

    building_id = Column(BigInteger, primary_key=True)
    region_id = Column(BigInteger)
    building_name = Column(String(256))
    city_name = Column(String(256))
    city_id = Column(Numeric(20))
    area_level = Column(String(20))
    building_area = Column(Numeric(20, 2))
    population = Column(Numeric(10))
    memo = Column(String(256))
    latitude = Column(Numeric(18, 10))
    longitude = Column(Numeric(18, 10))
    create_time = Column(DateTime, default=datetime.datetime.now)

    @classmethod
    def query_by_points(cls, points):
        q = DBSession().query(cls)
        polygon_point_dict = _get_polygon_from_points(points)
        q = q.filter(and_(cls.latitude <= polygon_point_dict['max_lat'],
                          cls.latitude >= polygon_point_dict['min_lat'],
                          cls.longitude >= polygon_point_dict['min_lng'],
                          cls.longitude <= polygon_point_dict['max_lng']))
        buildings = q.all()
        points = [(point['lat'], point['lng']) for point in points]
        buildings = [building for building in buildings
                     if is_in_region((float(building.latitude), float(building.longitude)), points)]
        return buildings


    @classmethod
    def query_by_region(cls, region_id):
        q = DBSession().query(cls)
        q = q.filter(cls.region_id == region_id)
        return q.all()


    @classmethod
    def update_by_region(cls, region_id, points):
        old_buildings = cls.query_by_region(region_id)
        new_buildings = cls.query_by_points(points)
        rm_list = set(old_buildings) - set(new_buildings)
        add_list = set(new_buildings) - set(old_buildings)
        for building in rm_list:
            building.region_id = None
        for building in add_list:
            building.region_id = region_id

    @classmethod
    def delete_by_region(cls, region_id):
        q = DBSession().query(cls)
        q = q.filter(cls.region_id == region_id)
        buildings = q.all()
        for building in buildings:
            building.region_id = None

def _get_polygon_from_points(points):
    max_lat = min_lat = points[0]['lat']
    max_lng = min_lng = points[0]['lng']

    for point in points:
        if max_lng <= point['lng']:
            max_lng = point['lng']

        if max_lat <= point['lat']:
            max_lat = point['lat']

        if min_lng >= point['lng']:
            min_lng = point['lng']

        if min_lat >= point['lat']:
            min_lat = point['lat']

    return {
        'max_lng': max_lng,
        'min_lng': min_lng,
        'max_lat': max_lat,
        'min_lat': min_lat
    }
