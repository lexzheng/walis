#!/usr/bin/env python2
# coding=utf8

from __future__ import absolute_import, division, print_function
from webargs import Arg
from walis.utils.http import args_parser
from walis.service.cs import user as cs_user_base


def get_user_by_phone():
    mobile = args_parser.parse({'phone': Arg(str, required=True)})['phone']
    return cs_user_base.get_user_by_phone(mobile)
