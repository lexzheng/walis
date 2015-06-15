# coding=utf8

from __future__ import absolute_import, division, print_function
import json
from walis.utils import geo


def get_dist(p1, p2):
    return (p1[0]-p2[0])*(p1[0]-p2[0]) + (p1[1]-p2[1])*(p1[1]-p2[1])


def get_centerpoint_of_region(polygons, only_one=False):
    if not polygons:
        return None

    center_points = []
    for polygon in polygons:
        center_point = [0, 0]
        for point in polygon:
            center_point[0] = center_point[0] + point[0]
            center_point[1] = center_point[1] + point[1]

        center_points.append((center_point[0]/len(polygon),
                              center_point[1]/len(polygon)))

    if only_one:
        length = len(center_points)
        lng = sum([c[1] for c in center_points]) / length
        lat = sum([c[0] for c in center_points]) / length
        return lat, lng

    return center_points


def get_radius_of_region(center_point, polygons):
    if not polygons:
        return None

    radius = 0
    points_num = 0
    for polygon in polygons:
        for point in polygon:
            radius += geo.distance(center_point, point)
            points_num += 1

    if points_num == 0:
        return 0

    return radius / points_num


def region_area_to_polygons(region_area, reverse=False):
    try:
        areas = json.loads(region_area)
    except:
        return []

    polygons = []
    for area in areas:
        points = area['point']
        polygon = []
        for point in points:
            lat = float(point.split(',')[0])
            lng = float(point.split(',')[1])
            if reverse:
                polygon.append((lng, lat))
            else:
                polygon.append((lat, lng))
        polygons.append(polygon)

    return polygons
