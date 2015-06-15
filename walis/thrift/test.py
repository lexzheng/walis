#! /usr/bin/env python2
# -*- coding:utf-8 -*-

from __future__ import absolute_import, print_function, division

from walis.thrift.server import jvs_client

if __name__ == "__main__":
    with jvs_client() as c:
        # print(c.ping())
        c.set_bd_restaurant_director(6, [51175,51174])