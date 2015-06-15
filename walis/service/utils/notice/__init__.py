#!/usr/bin/env python2
# coding=utf8

from __future__ import absolute_import, division, print_function

from .eleme_hermes_sdk import HermesClient

from walis.config import HERMES

notifier = HermesClient(**HERMES)
