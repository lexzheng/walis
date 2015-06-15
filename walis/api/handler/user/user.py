#!/usr/bin/env python2
# -*- coding: utf8 -*-

from __future__ import absolute_import, division, print_function

from flask.ext.login import current_user

from walis.thirdparty import thrift_client
from walis.utils.http import Arg, args_parser
from walis.service.user import user as user_base

def current():
    _sf_guard_user = current_user.get()
    _sf_guard_user_fields = [
        'username','created_at','last_login','is_active','is_super_admin',
    ]
    user = {
        'id':current_user.id,
        'permissions':current_user.get_permissions(),
    }
    for _field in _sf_guard_user_fields:
        user[_field] = getattr(_sf_guard_user,_field,None)
    if _sf_guard_user.is_super_admin:
        with thrift_client('eus') as eus:
            permissions = eus.walle_get_all_permissions()
            permissions = [p.name for p in permissions]
            user['permissions'] = permissions
    return user

def is_username_available():
    args = {
        'username':Arg(),
    }
    args_spec = args_parser.parse(args)
    available = user_base.is_username_available(args_spec['username'])
    return {'available':available}

def get_user_by_mobile():
    args = {
        'mobile':Arg(),
    }
    arg_spec = args_parser.parse(args)
    user = user_base.get_by_mobile(arg_spec['mobile'])
    return user or {}
