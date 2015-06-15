#!/usr/bin/env python2
# -*- coding: utf8 -*-

from __future__ import division, absolute_import, print_function

from walis.thirdparty import thirdparty_svc, thrift_client

BANK_NAME_ALIPAY = thirdparty_svc.eus.DRAWBACK_PROCESS_BANK_NAME_ALIPAY

ACCOUNT_TYPE_PERSONAL = thirdparty_svc.eus.BankDrawbackProcessRecordConst.ACCOUNT_TYPE_PERSONAL
ACCOUNT_TYPE_BUSINESS = thirdparty_svc.eus.BankDrawbackProcessRecordConst.ACCOUNT_TYPE_BUSINESS

REFUND_STATUS_RETRY = thirdparty_svc.eus.DrawbackProcessStatusConst.STATUS_RETRY

MAX_QUERY_LIMIT = 1000
DEFAULT_QUERY_LIMIT = 50


def query(status=None, order_id=None, pay_platform=None, offset=None, limit=DEFAULT_QUERY_LIMIT):
    condition = thirdparty_svc.eus.TDrawbackProcessRecordQuery()

    if status is not None:
        condition.status = status

    if order_id is not None:
        condition.order_id = order_id

    if pay_platform is not None:
        condition.pay_platform = pay_platform

    if offset is not None:
        condition.offset = offset

    if limit is not None:
        condition.limit = min(limit, MAX_QUERY_LIMIT)

    with thrift_client('eus') as eus:
        result = eus.query_drawback_process_record(condition)
    return result


def save_payment_account(pk, admin_id, bank_account, bank_name, account_type,
                         account_holder=None, bank_branch=None, city=None):
    with thrift_client('eus') as eus:
        return eus.retry_drawback_process(
            drawback_process_id=pk,
            process_user_id=admin_id,
            account_type=account_type,
            bank_account=bank_account,
            bank_name=bank_name,
            bank_branch=bank_branch,
            account_holder=account_holder,
            city=city
        )


def save_payment_proof(pk, image_hash):
    with thrift_client('eus') as eus:
        return eus.drawback_process_manually_success(pk, image_hash)


def ignore_drawback_process(pk, admin_id):
    with thrift_client('eus') as eus:
        return eus.ignore_drawback_process(
            drawback_process_id=pk,
            process_user_id=admin_id
        )


def revoke_drawback_process(pk):
    with thrift_client('eus') as eus:
        return eus.revoke_drawback_process(
            drawback_process_id=pk
        )
