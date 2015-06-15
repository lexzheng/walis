#!/usr/bin/env python2
# -*- coding: utf8 -*-

from __future__ import print_function, division, absolute_import

from walis.service.sms import sms as sms_base
from walis.utils.http import Arg, args_parser

def query_receive_by_mobile():
    args_spec = {
        'mobile':Arg(int)
    }
    args = args_parser.parse(args_spec)
    result = sms_base.query_receive_by_mobile(args['mobile'])
    return result
