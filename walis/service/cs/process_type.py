#!/usr/bin/env python2
# coding=utf8

from __future__ import absolute_import, division, print_function

from walis.service.cs.inner import process_type as base


def add_change_record(user_id, from_type, to_type):
    if from_type == to_type:
        return None
    return base.add_change_record(user_id, from_type, to_type)
