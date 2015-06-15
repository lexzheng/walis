#!/usr/bin/env python2
# coding=utf8

from __future__ import absolute_import, division, print_function
import time

from walis.utils.geo import is_in_region, is_rst_in_region


def test_on_endpoint():
    points = [(10, 10), (12, 12), (15, 15), (20, 15)]
    polygon = [(10, 10), (15, 15), (20, 15), (5, 10)]
    for point in points:
        print('point is ({}, {})'.format(point[0], point[1]))
        assert is_in_region(point, polygon) is True


def test_inside():
    points = [(11, 19), (15.345345, 18.234890324), (15, 10), (11, 10),
              (17.34, 10), (11, 8)]
    polygon = [(10, 20), (20, 20), (20, 5), (15, 10), (10, 5)]
    for point in points:
        print('point is ({}, {})'.format(point[0], point[1]))
        assert is_in_region(point, polygon) is True


def test_outside():
    points = [(100, 0), (9, 20), (-10, -10), (15, 8), (14, 6), (15, 5)]
    polygon = [(10, 20), (20, 20), (20, 5), (15, 10), (10, 5)]
    for point in points:
        print('point is ({}, {})'.format(point[0], point[1]))
        assert is_in_region(point, polygon) is False

    points = [(100, 0), (9, 20), (-10, -10), (15, 8), (14, 6)]
    polygon = [(10, 20), (20, 20), (30, 25), (20, 5), (15, 10), (10, 5)]
    for point in points:
        print('point is ({}, {})'.format(point[0], point[1]))
        assert is_in_region(point, polygon) is False

    points = [(0, 5), (0, 20), (0, 25), (0, 40)]
    polygon = [(10, 20), (20, 25), (30, 40), (35, 5)]
    for point in points:
        print('point is ({}, {})'.format(point[0], point[1]))
        assert is_in_region(point, polygon) is False


def test_error():
    point = (31.246383, 121.482109)

    polygon = [
        (31.244826, 121.520048),
        (31.242845, 121.519855),
        (31.240478, 121.51992),
        (31.238845, 121.520606),
        (31.235451, 121.522366),
        (31.229928, 121.524876),
        (31.22602, 121.5267),
        (31.225837, 121.526657),
        (31.229176, 121.536549),

        (31.225139, 121.537923),
        (31.222827, 121.53891),
        (31.218386, 121.53582),
        (31.215762, 121.543727),
        (31.217863, 121.546237),
        (31.218579, 121.547836),
        (31.222341, 121.545036),
        (31.224736, 121.543276),
        (31.225947, 121.542364),
        (31.22813, 121.541667),

        (31.228678, 121.541495),
        (31.230715, 121.546838),
        (31.235072, 121.544768),
        (31.239971, 121.542246),
        (31.244695, 121.53965),
        (31.247896, 121.537858),
        (31.246383, 121.533631),
        (31.24519, 121.527473),
        (31.244851, 121.521851),
        (31.244897, 121.521465)]
    print(is_in_region(point, polygon, xy_reverse=True))
    print(is_rst_in_region(point, polygon))


# start = time.time()
# for i in xrange(1000):
test_on_endpoint()
test_inside()
test_outside()
# print('time: {}'.format(time.time() - start))

test_error()
