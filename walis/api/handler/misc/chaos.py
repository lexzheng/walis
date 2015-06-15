#!/usr/bin/env python2
# -*- coding: utf8 -*-

from __future__ import division, print_function, absolute_import

from walis.utils.http import Arg, args_parser
from walis.service.misc import chaos as chaos_base

def edit_username_mobile():
    args_spec = {
        'user_id':Arg(int),
        'username':Arg(unicode),
        'mobile':Arg(unicode),
    }
    args = args_parser.parse(args_spec)
    chaos_base.edit_username_mobile(**args)
    return '{"success": true}'

def get_user(user_id):
    user_id = int(user_id)
    result = chaos_base.get_user(user_id)
    return result
