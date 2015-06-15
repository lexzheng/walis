#!/usr/bin/env python2
# coding=utf8

from __future__ import absolute_import, division, print_function

import logging
from pickle import dumps

from .beanstalkd import (
    bstalk,
    reconnect,
)

# All the tubes should be defined here
BSTALK_TUBES = {
    'tube_vc': 'voice_call',
    'tube_vo': 'voice_order',
    'tube_order_auto_proc': 'order_auto_process',
}

log = logging.getLogger(__name__)


@reconnect
def enqueue(tube, func, *args, **kwargs):
    bstalk.conn.use(tube)
    bstalk.conn.put(dumps((func, args, kwargs)))


def send_task(func, *args, **kwargs):
    """
    Async task in Walis.

    :param func: Async task function.
    :param args: function parameters.
    :param kwargs: function parameters.
    :return: None
    """
    try:
        enqueue('async_task', func, *args, **kwargs)
    except BaseException as e:
        log.error("Async_task error at: function:<{0}> args:<{1} {2}> exc:<{3}>"
                  .format(func.__name__, args, kwargs, e))
