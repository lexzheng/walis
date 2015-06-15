#!/usr/bin/env python2
# coding=utf8

from __future__ import absolute_import, division, print_function
from walis.service.activity import food_activity


def get(act_id):
    return food_activity.get(int(act_id))

