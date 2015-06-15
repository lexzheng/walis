#!/usr/bin/env python2
# coding=utf8

from __future__ import absolute_import, division, print_function
from thriftpy.rpc import client_context
from walis import config
from walis.thrift.utils import jvs_thrift


def jvs_client():
    return client_context(
        jvs_thrift.JvsService,
        config.JVS_THRIFT_SERVICE['host'],
        config.JVS_THRIFT_SERVICE['port']
    )


def jvs_test():

    with jvs_client() as c:
        c.ping()
        import IPython
        IPython.embed()
