#!/usr/bin/env python2
# coding=utf8

from __future__ import absolute_import, division, print_function
from walis.core.api import WalisView
from walis.core.response import json_header


class BaseApi(WalisView):
    decorators = [json_header, ]
