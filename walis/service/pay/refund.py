#!/usr/bin/env python2
# -*- coding: utf8 -*-

from __future__ import division, absolute_import, print_function

from datetime import datetime

from walis.utils.misc import ttype2dict
from walis.service.utils import file as file_utils
from walis.service.user import user as user_service
from .inner import refund as refund_base


def query(status=None, order_id=None, pay_platform=None, offset=None, limit=None):
    resource = refund_base.query(status, order_id, pay_platform, offset, limit)
    for item in resource.drawback_process_records:
        # create opt log (only one row at now)
        item.optlog = []
        if item.process_user_id and item.bank_drawback_process_record:
            admin = user_service.get_user(item.process_user_id)
            item.optlog.append({
                'time': datetime.fromtimestamp(int(item.retry_at)).strftime('%Y-%m-%d %H:%M:%S'),
                'admin': admin.username,
                'detail': u'提交打款账号'
            })
        # process_user_id maybe changed in the future, don't expose it to front
        delattr(item, 'process_user_id')
        # complete img url
        if item.bank_drawback_process_record and item.bank_drawback_process_record.image_hash:
            item.image_url = file_utils.get_file_url(
                item.bank_drawback_process_record.image_hash
            )
        # convert order_id as string, that to prevent exceeding the maximum
        # integer in javascript
        item.order_id = str(item.order_id)
    return ttype2dict(resource)


def save_bank_account(pk, admin_id, bank_account, bank_name, account_type, account_holder, bank_branch, city):
    return refund_base.save_payment_account(pk, admin_id, bank_account, bank_name, account_type, account_holder, bank_branch, city)


def save_alipay_account(pk, admin_id, bank_account):
    bank_name = refund_base.BANK_NAME_ALIPAY
    account_type = refund_base.ACCOUNT_TYPE_PERSONAL
    return refund_base.save_payment_account(pk, admin_id, bank_account, bank_name, account_type)


def save_payment_proof(pk, image_hash):
    return refund_base.save_payment_proof(pk, image_hash)


def ignore_drawback_process(pk, admin_id):
    return refund_base.ignore_drawback_process(pk, admin_id)


def revoke_drawback_process(pk):
    return refund_base.revoke_drawback_process(pk)


def count():
    resource = refund_base.query(
        status=refund_base.REFUND_STATUS_RETRY,
        offset=None,
        limit=None
    )
    return {'retry': resource.count}
