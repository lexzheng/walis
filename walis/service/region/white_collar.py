#! /usr/bin/env python2
# -*- coding:utf-8 -*-

from __future__ import division, print_function, absolute_import

from walis.model.analytics.white_collar_building import WhiteCollarBuilding

from walis.model.analytics import walle_db_commit as db_commit


def get_building_by_region(region_id):
    return WhiteCollarBuilding.query_by_region(region_id)


def query_building_by_points(points):
    return WhiteCollarBuilding.query_by_points(points)


@db_commit
def update_building_region(region_id, points):
    return WhiteCollarBuilding.update_by_region(region_id, points)


@db_commit
def delete_by_region(region_id):
    return WhiteCollarBuilding.delete_by_region(region_id)
