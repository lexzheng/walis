#!/usr/bin/env python2
# coding=utf8

from __future__ import absolute_import, division, unicode_literals
from . import (
    DevExc,
    SysExc, AuthExc, UserExc, ZeusExc)
from .error_code import (
    CODE_MSG,
    DEV_EXCEPTION_UNDEFINED_ERROR,
)


def gen_exception_raiser(exc_cls):

    def wrapper(error_code, *args, **kwargs):
        msg = CODE_MSG.get(error_code)
        if not msg:
            raise DevExc(error_code, CODE_MSG[DEV_EXCEPTION_UNDEFINED_ERROR])

        origin_exc = kwargs.pop('exc', None)
        if origin_exc:
            msg += ', <origin_exc: {exc!s}>'.format(exc=origin_exc)

        if args:
            raise exc_cls(error_code, msg.format(*args))
        elif kwargs:
            raise exc_cls(error_code, msg.format(**kwargs))

        raise exc_cls(error_code, msg)

    return wrapper


raise_server_exc = gen_exception_raiser(SysExc)

raise_zeus_exc = gen_exception_raiser(ZeusExc)

raise_user_exc = gen_exception_raiser(UserExc)

raise_auth_exc = gen_exception_raiser(AuthExc)

raise_dev_exc = gen_exception_raiser(DevExc)
