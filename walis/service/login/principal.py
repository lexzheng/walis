# coding=utf8
#!/usr/bin/env python
from __future__ import division, print_function

import copy
from functools import wraps

from flask import current_app
from flask.ext.login import current_user

from walis.utils.http import jsonpickle_dumps

"""
*** DEPRECATED !!!
*** REMOVE THIS FILE IN NEAR FUTURE ***
"""


def no_permission():
    content = {
        'status': 0,
        'message': 'no permission',
    }
    return jsonpickle_dumps(content), 403


def zeus_group(*groups, **deco_kwargs):
    def wrapper(fn):
        check_type = deco_kwargs.get('check_type', 'accepted')
        if check_type == 'accepted':
            is_strict = False
        elif check_type == 'required':
            is_strict = True

        @wraps(fn)
        def decorated_view(*args, **kwargs):
            if not current_app.config['LOGIN_REQUIRED']:
                check_result = True
            else:
                check_result = current_user.has_groups(groups, is_strict)
            if check_result:
                return fn(*args, **kwargs)
            else:
                return no_permission()

        return decorated_view

    return wrapper


def func_permission(check_func, *deco_args, **deco_kwargs):
    def wrapper(fn):
        @wraps(fn)
        def decorated_view(*args, **kwargs):
            # return while_no_permission()
            _kwargs = copy.copy(kwargs)
            _kwargs.update(deco_kwargs)
            _args = deco_args + args
            if not current_app.config['LOGIN_REQUIRED']:
                check_result = True
            else:
                check_result = check_func(*_args, **_kwargs)
            if current_user.is_super_admin():
                check_result = True
            if check_result:
                return fn(*args, **kwargs)
            else:
                return no_permission()

        return decorated_view

    return wrapper


fp = func_permission
zg = zeus_group