#! /usr/bin/env python2
# -*- coding:utf-8 -*-

from __future__ import absolute_import, print_function, division

from flask.ext.login import current_user

from walis.service.rst import (
    bankcard as bankcard_base,
    restaurant as rst_base,
)
from walis.service.user import user as user_base
from walis.model.walis.rst import RstBankCard, DEFAULT_RECORD_LIMIT
from walis.model.walis import db_commit
from walis.utils.http import Arg, args_parser
from walis.utils.model import model2dict
from walis.utils.paging import get_paging_params
from walis.core.auth.map import customer_service, directors
from walis.api.handler.rst.notice.bankcard_approve_sms import (
    send_bankcard_approve_sms
)
from walis.thirdparty import thirdparty_svc
from walis.thirdparty.coffee import coffee

from walis.exception.util import raise_user_exc
from walis.exception.error_code import (
    BANKCARD_APPROVE_ERR
)
from walis.core import async
from walis.core.auth.map import auth_map_admin

CARD_ID_MIN_LENGTH = 9
RST_INVALID = 0


def get_rst_admin(rst_id):
    rst_admin = bankcard_base.get_rst_admin(rst_id)
    if not rst_admin:
        return rst_admin
    rst_admin = user_base.get(rst_admin.user_id)  # return as dict
    rst_admin_profile = user_base.get_profile(rst_admin['id'])
    return {'user_id': rst_admin['id'],
            'username': rst_admin['username'],
            'mobile': rst_admin_profile.mobile,
            'is_mobile_valid': rst_admin_profile.is_mobile_valid}


def get_rst_bankcard_list(rst_id):
    arg_spec = {
        'status': Arg(int, allow_missing=True),
        'type_code': Arg(int, allow_missing=True),
        'page_size': Arg(int, allow_missing=True),
        'page_no': Arg(int, allow_missing=True)
    }
    args = args_parser.parse(arg_spec)
    status = args.get('status')
    type_code = args.get('type_code')
    page_no, page_size = get_paging_params()
    offset = (page_no - 1) * page_size
    limit = page_size
    rst_bankcard_list = bankcard_base \
        .query_bankcard(rst_id, status=status, limit=limit, offset=offset)
    rst_bankcard_list_new = [model2dict(m) for m in rst_bankcard_list]
    return {
        'bankcard_list': rst_bankcard_list_new,
        'total_num':
            bankcard_base.get_bankcard_count([rst_id, ],
                                             status=status,
                                             type_code=type_code)
    }


def get_rst_bankcard(rst_id, bankcard_id):
    rst_bankcard = bankcard_base.get_bankcard(rst_id, bankcard_id)
    if not rst_bankcard:
        return {}
    return model2dict(rst_bankcard)


def get_rst_bankcard_pre_next(bankcard_id):
    pre, next = bankcard_base.get_pre_next(bankcard_id)
    if pre:
        pre_bankcard_id = pre.id
        pre_rst_id = pre.rst_id
        pre = {'bankcard_id': pre_bankcard_id, "rst_id": pre_rst_id}
    if next:
        next_bankcard_id = next.id
        next_rst_id = next.rst_id
        next = {'bankcard_id': next_bankcard_id, 'rst_id': next_rst_id}
    return {
        'pre': pre,
        'next': next,
    }


def _get_bankcard_args():
    arg_spec = {
        'type_code': Arg(int),
        'status': Arg(int, allow_missing=True),
        'username': Arg(),
        'mobile': Arg(str),
        'card_id': Arg(str),
        'bank_id': Arg(int),
        'cardholder_name': Arg(),
        'bankcard_image_front': Arg(allow_missing=True),
        'identity_card_image_front': Arg(allow_missing=True),
        'identity_card_image_back': Arg(allow_missing=True),
        'ol_pay_contract_image': Arg(allow_missing=True),
        'misc_image': Arg(allow_missing=True),
        'comment': Arg(allow_missing=True),
    }
    return args_parser.parse(arg_spec)


@db_commit
def add_rst_bankcard(rst_id):
    rst_id = int(rst_id)
    args = _get_bankcard_args()
    args.update({'rst_id': rst_id})
    rst_bankcard = _add_rst_bankcard(**args)
    bankcard_base.add_bankcard_processing_record(
        rst_id=rst_id,
        bankcard_id=rst_bankcard.id,
        process_user_id=current_user.id,
        messages=u'添加银行卡信息',
        status_to=RstBankCard.STATUS_PENDING, )
    return {"bankcard_id": rst_bankcard.id}


@db_commit
def _add_rst_bankcard(**kwargs):
    return bankcard_base.add_bankcard(**kwargs)


@db_commit
def update_rst_bankcard(rst_id, bankcard_id):
    args = _get_bankcard_args()
    args.update({'id': bankcard_id, "status": RstBankCard.STATUS_PENDING,
                 "comment": ""})
    bankcard_base.update_bankcard(**args)
    bankcard_base.add_bankcard_processing_record(
        rst_id=rst_id,
        bankcard_id=bankcard_id,
        process_user_id=current_user.id,
        messages=u'修改银行卡信息',
        status_to=RstBankCard.STATUS_PENDING,
    )
    return ''


@db_commit
def bankcard_reject(rst_id, bankcard_id):
    arg_spec = {
        "comment": Arg()
    }
    args = args_parser.parse(arg_spec)
    args.update({"status": RstBankCard.STATUS_INVALID})
    bankcard_base.update_bankcard(bankcard_id, **args)
    bankcard_base.add_bankcard_processing_record(
        rst_id=rst_id,
        bankcard_id=bankcard_id,
        process_user_id=current_user.id,
        messages=u'退回该银行卡信息',
        status_to=RstBankCard.STATUS_INVALID,
    )


@db_commit
def bankcard_approve(rst_id, bankcard_id):
    args = _get_bankcard_args()
    args.update({'id': bankcard_id,
                 "status": RstBankCard.STATUS_VALID,
                 "rst_id": rst_id})

    rst_admin = get_rst_admin(rst_id)

    current_zeus_bankcard = None
    mobile = None
    if rst_admin:
        current_zeus_bankcard = \
            user_base.get_bankcard(rst_admin.get('user_id'))
        mobile = rst_admin.get("mobile")
    try:
        if rst_admin:
            _unbind_admin_mobile(rst_admin.get('user_id'))
            _unbind_admin_bankcard(rst_admin.get('user_id'))

        bankcard_base.super_user_bind(
            username=args['username'],
            mobile=args['mobile'],
            restaurant_id=rst_id,
            bank_id=args['bank_id'],
            card_id=args['card_id'],
            cardholder_name=args['cardholder_name'],
            process_user_id=current_user.id)

        _current_to_history(rst_id)
        bankcard_base.update_bankcard(**args)
        bankcard_base.add_bankcard_processing_record(
            rst_id=rst_id,
            bankcard_id=bankcard_id,
            process_user_id=current_user.id,
            messages=u'审核通过该银行卡信息',
            status_to=RstBankCard.STATUS_VALID,
        )
        rst = rst_base.get(rst_id)
        bank = bankcard_base.get_bank(int(args['bank_id']))
        async.send_task(send_bankcard_approve_sms, phone=args['mobile'],
                        params={"restaurant_name": rst.get('name'),
                                "card_holder": args["cardholder_name"],
                                "bank": bank.bank_name,
                                "card_tail_number": args["card_id"][-4:]})
    except thirdparty_svc.eus.EUSUserException as e:
        # rollback bankcard and mobile
        if mobile and rst_admin.get("is_mobile_valid") == 1:
            user_base.bind_mobile(rst_admin.get("user_id"), mobile)
        if current_zeus_bankcard:
            user_base.bankcard_bind(user_id=current_zeus_bankcard.user_id,
                                    cardholder_name=current_zeus_bankcard.cardholder_name,
                                    bank_id=current_zeus_bankcard.bank_id,
                                    card_id=current_zeus_bankcard.card_id)

        raise_user_exc(BANKCARD_APPROVE_ERR, error_msg=e.message)


@db_commit
def unbind_bankcard(rst_id):
    rst_admin = get_rst_admin(rst_id)
    _unbind_admin_bankcard(rst_admin['user_id'])
    _current_to_history(rst_id)


def _unbind_admin_mobile(user_id):
    user_base.unbind_mobile(user_id)


def _unbind_admin_bankcard(user_id):
    user_base.unbind_bankcard_by_user(user_id)


def _current_to_history(rst_id):
    current_bankcard = bankcard_base \
        .query_bankcard(rst_id, status=RstBankCard.STATUS_VALID)
    for bankcard in current_bankcard:
        bankcard_base.update_bankcard(bankcard.id,
                                      status=RstBankCard.STATUS_HISTORY)
        bankcard_base.add_bankcard_processing_record(
            rst_id=rst_id,
            bankcard_id=bankcard.id,
            messages=u'弃用该银行卡信息',
            process_user_id=current_user.id,
            status_to=RstBankCard.STATUS_INVALID
        )


def get_processing_record(rst_id, bankcard_id):
    arg_spec = {
        "limit": Arg(int, allow_missing=True),
    }
    args = args_parser.parse(arg_spec)
    limit = args.get("limit", DEFAULT_RECORD_LIMIT)
    processing_record_list = bankcard_base \
        .query_processing_record(rst_id, bankcard_id, limit)
    if not processing_record_list:
        return []
    process_user_ids = []
    for m in processing_record_list:
        process_user_ids.append(m.process_user_id)
    process_user_list = user_base.mget_users(process_user_ids)
    process_user_dict = {user.id: user.username for user in process_user_list}
    processing_record_list_new = []
    for processing_record in processing_record_list:
        pr_dict = model2dict(processing_record)
        pr_dict['process_user_username'] = \
            process_user_dict.get(pr_dict['process_user_id'])
        processing_record_list_new.append(pr_dict)
    return processing_record_list_new


def get_all_bankcard_list():
    arg_spec = {
        'search_text': Arg(),
        'status': Arg(int, allow_missing=True),
        'type_code': Arg(int, allow_missing=True),
    }
    args = args_parser.parse(arg_spec)
    search_text = args.pop('search_text')

    rst_ids = _filter_ids(search_text)

    args['rst_ids'] = rst_ids
    page_no, page_size = get_paging_params(paging_size=50)
    offset = (page_no - 1) * page_size
    limit = page_size
    args.update({"offset": offset, "limit": limit})
    bankcard_list = bankcard_base.query_by_status(**args)

    if not bankcard_list:
        return {
            'bankcard_list': [],
            'total_num': 0,
        }

    bankcard_list_new = []
    rst_set_ids = set()
    for bankcard in bankcard_list:
        bankcard_list_new.append(model2dict(bankcard))
        rst_set_ids.add(bankcard.rst_id)

    rst_map = rst_base.get_map(rst_set_ids)
    for bankcard in bankcard_list_new:
        bankcard.update({
            "restaurant_name": rst_map[bankcard['rst_id']].name,
        })

    return {
        'bankcard_list': bankcard_list_new,
        'total_num':
            bankcard_base.get_bankcard_count(
                rst_ids=rst_ids,
                status=args.get("status"),
                type_code=args.get("type_code")),
    }


def _filter_ids(search_text=None):
    '''
    :param search_text:
    :return: customer_service and admin return None or [search_text,]
            directors return restaurant_ids in region or [search_text,]
    '''
    rst_ids = []
    if coffee.hr_permission.isPermittedToThis(context=current_user.auth_context,
                                           permission=auth_map_admin['RST_ADMIN']):
        if search_text:
            rst_ids = [int(search_text), ]
        else:
            rst_ids = None
    else:
        city_ids = current_user.utp_city_ids or None
        # region_group_ids = current_user.region_group_ids or None
        # region_ids = current_user.region_ids or None

        if search_text:
            rst_ids = [int(search_text), ]
        else:
            rst_ids = None
        rst_list = 1
        offset = 0
        limit = 2000
        all_rst_ids = []
        while rst_list:
            rst_list = rst_base.search_filter_restaurant(restaurant_ids=rst_ids,
                                                         city_ids=city_ids,
                                                         offset=offset,
                                                         size=limit)
            offset += limit
            all_rst_ids.extend([int(rst.get('_id')) for rst in rst_list])
            if len(rst_list) < limit:
                break
        rst_ids = all_rst_ids
    return rst_ids
