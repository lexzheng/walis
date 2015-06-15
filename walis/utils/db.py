#!/usr/bin/env python2
# coding=utf8

from __future__ import absolute_import, division, print_function

from walis.core.db.redis import redis


def redis_sadd(key, *values):
    """ redis sadd for rizzrack """
    if not values:
        return

    if len(values) == 1:
        if type(values[0]) in (set, list, tuple):
            if values[0]:
                return redis.sadd(key, *values[0])
            else:
                return None

    return redis.sadd(key, *values)


def redis_srem(key, *values):
    """ redis srem for rizzrack """
    if not values:
        return

    if len(values) == 1:
        if type(values[0]) in (set, list, tuple):
            return redis.srem(key, *values[0])

    return redis.srem(key, *values)

