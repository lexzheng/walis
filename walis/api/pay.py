#!/usr/bin/env python2
# -*- coding: utf8 -*-

from walis.api.handler.pay import (
    refund as refund_handler,
    payment as payment_handler
)
from walis.core.api import api

from .base import BaseApi


class RefundApi(BaseApi):

    """
    用户退款失败处理（即：自动退款给用户失败了需要给他手动退款，然后这里就是手动退款给用户要走的一些处理流程）
    """
    route_base = 'refund'
    handler = refund_handler

    @api('/list')
    def get_list(self):
        """
        退款列表
        """
        return self.handler.get_list()

    @api('/count')
    def count(self):
        """
        获取退款记录的数量
        """
        return self.handler.count()

    @api('/retry/<int:pk>', methods=['PUT'])
    def retry(self, pk):
        """
        提交财务打款（即：重新尝试退款）
        """
        return self.handler.retry(pk)

    @api('/done/<int:pk>', methods=['PUT'])
    def done(self, pk):
        """
        退款完成
        """
        return self.handler.done(pk)

    @api('/ignore/<int:pk>', methods=['PUT'])
    def ignore(self, pk):
        """
        暂不处理
        """
        return self.handler.ignore(pk)

    @api('/revoke/<int:pk>', methods=['PUT'])
    def revoke(self, pk):
        """
        退回客服
        """
        return self.handler.revoke(pk)


class PaymentApi(BaseApi):
    route_base = 'alipay'

    handler = payment_handler

    @api('/unprocessed_batch')
    def get_unprocessed_batch(self):
        return self.handler.get_alipay_unprocessed_batch()

    @api('/get_alipay_url')
    def get_alipay_url(self):
        return self.handler.get_alipay_url()
