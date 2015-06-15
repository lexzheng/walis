#!/usr/bin/env python2
# -*- coding: utf8 -*-

from __future__ import print_function, division, absolute_import

from walis.thirdparty import thrift_client

def get_alipay_unprocessed_batch():
    with thrift_client('eus') as eus:
        return eus.query_alipay_unprocessed_batch()

def get_alipay_refund_apply_info(batch_id):
    with thrift_client('eus') as eus:
        return eus.get_alipay_refund_apply_info(batch_id)
