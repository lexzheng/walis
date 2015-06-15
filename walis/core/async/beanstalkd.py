# coding=utf8

from __future__ import absolute_import, division, print_function
import functools

from beanstalkc import Connection, SocketError
from walis.config import BEANSTALKD

import logging
log = logging.getLogger(__name__)


class Beanstalkd(object):

    def __init__(self):
        self._conn = None

    @property
    def conn(self):
        if self._conn is None:
            self._conn = create_bstalk_conn()
        return self._conn

    def reconnect(self):
        self.conn.reconnect()


def create_bstalk_conn():
    return Connection(
        host=BEANSTALKD['host'],
        port=BEANSTALKD['port'],
        connect_timeout=1,
    )


def reconnect(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except SocketError:
            try:
                bstalk.reconnect()
                return func(*args, **kwargs)
            except SocketError:
                log.error('could not connect to beanstalk.')
    return wrapper


bstalk = Beanstalkd()
