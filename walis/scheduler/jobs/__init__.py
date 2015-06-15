#!/usr/bin/env python2
# coding=utf8

from __future__ import absolute_import, division, print_function
import time
import logging
from functools import wraps


def job_deco(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        log = logging.getLogger('scheduler.{}'.format(func.__name__))
        start = time.time()
        log.info('Job {} starts.'.format(func.__name__))

        rv = func(*args, **kwargs)

        end = time.time()
        log.info('Job {} ends. {}s'.format(func.__name__, end-start))
        return rv

    return wrapper
