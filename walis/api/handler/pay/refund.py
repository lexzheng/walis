#!/usr/bin/env python2
# -*- coding: utf8 -*-

from __future__ import division, print_function, absolute_import

from flask.ext.login import current_user

from walis.service.pay import refund as refund_service
from walis.utils.http import Arg, args_parser
from walis.utils.paging import get_paging_params


def get_list():
    user_args = {
        'status': Arg(int),
        'order_id': Arg(int),
        'pay_platform': Arg(int),
    }
    page_no, page_size = get_paging_params()
    args = args_parser.parse(user_args)
    args.update(offset=(page_no - 1) * page_size, limit=page_size)
    result = refund_service.query(**args)
    return result


def count():
    return refund_service.count()


def retry(pk):
    user_args = {
        'pay_type': Arg(int, required=True),
        'bank_account': Arg(str, required=True),
        'bank_name': Arg(unicode, allow_missing=True),
        'account_type': Arg(int, allow_missing=True),
        'account_holder': Arg(unicode, allow_missing=True),
        'bank_branch': Arg(unicode, allow_missing=True),
        'city': Arg(unicode, allow_missing=True),
    }
    args = args_parser.parse(user_args)
    if args.get('pay_type') == 1:
        result = refund_service.save_bank_account(
            pk=pk,
            admin_id=current_user.id,
            bank_account=args.get('bank_account'),
            bank_name=args.get('bank_name'),
            account_type=args.get('account_type'),
            account_holder=args.get('account_holder'),
            bank_branch=args.get('bank_branch'),
            city=args.get('city')
        )
    else:
        result = refund_service.save_alipay_account(
            pk=pk,
            admin_id=current_user.id,
            bank_account=args.get('bank_account')
        )
    return result


def done(pk):
    user_args = {
        'image_hash': Arg(str, required=True)
    }
    args = args_parser.parse(user_args)
    return refund_service.save_payment_proof(pk=pk, **args)


def ignore(pk):
    admin_id = current_user.id
    return refund_service.ignore_drawback_process(pk, admin_id)


def revoke(pk):
    return refund_service.revoke_drawback_process(pk)
