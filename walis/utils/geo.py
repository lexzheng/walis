#!/usr/bin/env python2
# coding=utf8

from __future__ import absolute_import, division, print_function
from itertools import imap
import sys
import math


def is_in_region(point, region, xy_reverse=False):
    """ 判断是否在一个点point是否在多边形区域region内（包括在边上）

    判断条件为左开右闭 (point1, point2], 只考虑向右的射线交点count

    :param point: A couple of data. e.g. (19.23, 30.22)
    :param region: List of ordered points. e.g. [(12.2, 17.5), (13.5, 19.4) ...]
    :return: True or False
    """

    if type(point) not in (tuple, list) or len(point) != 2 \
            or type(region) not in (tuple, list):
        return False

    if xy_reverse:
        point = (point[1], point[0])
        new_region = [(p[1], p[0]) for p in region]
        region = new_region

    count = 0
    length = len(region)
    for i, p2 in enumerate(region):
        p1 = region[i - 1]

        # on the line's endpoint
        if (p1[0] == point[0] and p1[1] == point[1]) \
                or (p2[0] == point[0] and p2[1] == point[1]):
            return True

        # on the line (vertical)
        if p1[0] == p2[0]:
            if point[0] == p1[0] and _between(point[1], p1[1], p2[1]):
                return True

        # parallel with x-axis
        if is_parallel(p1, p2):
            continue

        # on the line (normal)
        if (p1[0] - point[0]) != 0 and (point[0] - p2[0]) != 0:
            if slope(p1, point) == slope(point, p2):
                return True

        if max(p1[0], p2[0]) <= point[0]:
            continue
        else:
            x_inter = (point[1] - p1[1]) * (p2[0] - p1[0]) / (p2[1] - p1[1]) + \
                      p1[0]
            if x_inter < point[0]:
                continue

        if p1[1] < point[1] < p2[1] or p2[1] < point[1] < p1[1]:
            count += 1
        else:
            if point[1] == p1[1]:
                p0 = region[i - 2]
                if is_parallel(p0, p1):
                    p0 = region[i - 3]

                if (p2[1] - p1[1]) * (p0[1] - p1[1]) < 0:
                    count += 1

    if count % 2 == 1:
        return True
    return False


def slope(p1, p2):
    try:
        rv = (p1[1] - p2[1]) / (p1[0] - p2[0])
    except ZeroDivisionError:
        rv = sys.maxint

    return rv


def is_parallel(p1, p2):
    return p1[1] == p2[1]


def _between(p, p1, p2):
    if p1 < p2:
        return p1 < p < p2
    else:
        return p2 < p < p1


def is_rst_in_region(point, polygons):
    """ Sharply版本，可能会更准确，但耗时多15倍

    :param point:
    :param polygons:
    :return:
    """
    return any(imap(lambda p: point_in_polygon(point, p), [polygons]))


def point_in_polygon(point, region):
    from shapely.geometry import (
        Polygon,
        LinearRing,
        Point,
    )
    point = Point(point)
    polygon_boundary = LinearRing(region)
    polygon = Polygon(region)
    return polygon.contains(point) or polygon_boundary.contains(point)


def distance(point1, point2):
    """

    :param point1: (lat, lng)
    :param point2: (lat, lng)
    :return: dist (meters)
    """
    radlat1 = math.radians(point1[0])
    radlat2 = math.radians(point2[0])
    lat_div = radlat1 - radlat2
    lng_div = math.radians(point1[1]) - math.radians(point2[1])
    s = 2 * math.asin(math.sqrt(
        math.pow(math.sin(lat_div / 2), 2) + math.cos(radlat1) * math.cos(
            radlat2) * math.pow(math.sin(lng_div / 2), 2)))
    earth_radius = 6378.137
    return math.fabs(s * earth_radius)


if __name__ == '__main__':
    print(distance((121.391373,31.173356), (121.382103,31.232766)))