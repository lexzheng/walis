#!/usr/bin/env python2
# -*- coding: utf8 -*-

from __future__ import print_function, division, absolute_import

from walis.thirdparty import thrift_client, thirdparty_svc


def save(rst_ids):
    with thrift_client('eos') as eos:
        return eos.generate_restaurant_coupon_batch(rst_ids)


def get_rst_ids(batch_sn):
    try:
        with thrift_client('eos') as eos:
            return eos.get_restaurant_ids_by_batch_sn(batch_sn)
    except thirdparty_svc.eos.EOSUserException:
        return []