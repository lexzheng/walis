#!/usr/bin/env python2
# coding=utf8

from __future__ import absolute_import, division, print_function

from walis.service.cs import process_type as process_type_service


def add_process_type_change_record(user_id, from_type, to_type):
    return process_type_service.add_change_record(user_id, from_type, to_type)
