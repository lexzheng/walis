#!/usr/bin/env python2
# -*- coding: utf8 -*-

from __future__ import absolute_import, print_function, division

from walis.thirdparty import thrift_client


def query_verify_code_by_mobile(mobile):
    with thrift_client('sms') as sms:
        result = sms.query_verify_code_by_mobile(mobile)
    for sms in result:
        sms.content = u'您在饿了么上的验证码{}，请在5分钟内输入。' \
                      u'如非本人操作请忽略本短信'.format(sms.code)
    return sorted(result, key=lambda r: r.created_at, reverse=True)


def query_receive_by_mobile(mobile):
    with thrift_client('sms') as sms:
        return sms.query_receive_by_mobile(mobile)
