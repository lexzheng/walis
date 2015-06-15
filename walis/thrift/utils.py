#!/usr/bin/env python2
# coding=utf8

from __future__ import absolute_import, division, print_function
import os
import thriftpy
from walis import config


jvs_thrift = thriftpy.load(
    os.path.join(config.SOURCE_DIR, 'walis/thrift/jvs.thrift'))
