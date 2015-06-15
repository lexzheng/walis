#!/usr/bin/env python2
# -*- coding: utf8 -*-

from __future__ import absolute_import, print_function, division

from walis.utils.http import Arg, args_parser
from walis.service.pay import payment as payment_handler

def get_alipay_unprocessed_batch():
    batch_infos = payment_handler.get_alipay_unprocessed_batch()
    return [{'batch_id': b.id, 'created_at': b.created_at}
            for b in batch_infos]


def get_alipay_html(batch_id):
    return payment_handler.get_alipay_refund_apply_info(batch_id)

def get_alipay_url():
    args_spec = {'batch_id': Arg(int), }
    batch_id = args_parser.parse(args_spec)['batch_id']
    url_info = get_alipay_html(batch_id)
    return {
        'url': url_info.url,
        'form_data': url_info.form_data
    }
