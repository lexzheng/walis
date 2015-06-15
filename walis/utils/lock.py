#!/usr/bin/env python2
# coding=utf8

from __future__ import absolute_import, division, print_function
import functools
import hashlib
from time import sleep, time
from walis.core.db.redis import redis

from walis.exception.util import raise_dev_exc
from walis.exception.error_code import DEV_REDIS_LOCKED_ERR

DEFAULT_LOCKED_TIMED_OUT = 120


##########################################
# Basic lock : using both lock and unlock
##########################################
def lock(keys, wait_time=0, time_out=DEFAULT_LOCKED_TIMED_OUT):
    """ lock certain resource with (MULTI)KEY """

    result = True
    end_time = time() + wait_time
    locked_keys = []

    if type(keys) in [list, tuple, set]:

        for key in keys:
            locked_keys.append(key)

            if not _lock(key, wait_time, time_out, end_time):
                # unlock all
                for locked_key in locked_keys:
                    _unlock(locked_key)
                result = False

    elif type(keys) in (str, int):
        result = _lock(str(keys), wait_time, time_out, end_time)

    else:
        raise_dev_exc(DEV_REDIS_LOCKED_ERR)

    return result


def unlock(keys):
    """ unlock certain resource with (MULTI)KEY """

    if type(keys) in [list, tuple, set]:
        for key in keys:
            _unlock(key)

    elif type(keys) in (str, int):
        _unlock(str(keys))

    else:
        raise_dev_exc(DEV_REDIS_LOCKED_ERR)


def _lock(key, wait_time=0, time_out=DEFAULT_LOCKED_TIMED_OUT, end_time=None):
    """ lock certain resource with KEY """
    if end_time is None:
        end_time = time() + wait_time

    while True:
        if redis.set(key, 1, ex=time_out, nx=True):
            return True

        if time() > end_time:
            return False
        sleep(0.1)


def _unlock(key):
    """ unlock certain resource with KEY """
    if redis.get(key):
        redis.delete(key)
        return True

    return False


##################################
# Lock decorator : used on methods
##################################
def locked(lock_key=None, pos=0, timeout=None, use_hash=False):
    """
    Lock decorator with `lock_key`.
    Used on methods.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args):

            entropy = str(args[pos])
            if use_hash:
                entropy = hashlib.md5(str(args[pos])).hexdigest()

            if lock_key is None:
                key = "lock:{0}:{1}".format(func.func_name, entropy)
            else:
                key = "lock:{0}:{1}".format(lock_key, entropy)

            try:
                with redis.lock(key, timeout):
                    return func(*args)
            except Exception:
                pass

        return wrapper

    return decorator


#############################
# Auto lock : used by `with`
#############################
# @contextlib.contextmanager
# def locking(lock_key, wait_time=0, time_out=DEFAULT_LOCKED_TIMED_OUT):
#     try:
#         yield lock(lock_key, wait_time, time_out)
#     finally:
#         unlock(lock_key)
