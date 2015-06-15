#! /usr/bin/env python2
# -*- coding:utf-8 -*-

from __future__ import absolute_import, print_function, division

from redis import Redis

from walis import config

redis = Redis(**config.REDIS)
