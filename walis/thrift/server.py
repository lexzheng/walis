#!/usr/bin/env python2
# -*- coding: utf8 -*-

from __future__ import absolute_import, division, print_function
from thriftpy.rpc import make_server

from walis import config
from walis.thrift.utils import jvs_thrift

from walis.thrift.dispatcher import JvsService

# TODO why monkey patch here
# patch_all()


def jvs_server():
    return make_server(
        jvs_thrift.JvsService, JvsService(),
        config.JVS_THRIFT_SERVICE['host'],
        config.JVS_THRIFT_SERVICE['port'],
    )


def main():
    server = jvs_server()
    # TODO make logs for here and dispatcher
    print('jvs {}:{}'.format(config.JVS_THRIFT_SERVICE['host'],
                             config.JVS_THRIFT_SERVICE['port']))
    server.serve()


if __name__ == '__main__':
    main()
