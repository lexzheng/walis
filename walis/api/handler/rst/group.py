#!/usr/bin/env python2
# coding=utf8

from __future__ import absolute_import, division, print_function
from walis.service.rst import group as group_base


def group_rsts(city_id):
    count = group_base.group_ungrouped_rsts(int(city_id))
    return {'msg': 'Successfully group {} restaurants!'.format(count)}
