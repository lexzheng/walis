#! /usr/bin/env python2
# -*- coding:utf-8 -*-

from __future__ import absolute_import, division, print_function

import time
import json

from walis.model.walis import db_commit, DBSession
from walis.model.walis.rst import RstBankCard
from walis.thirdparty import thirdparty_svc, thrift_client
from walis.service.rst import inner as rst_inner
from walis.service.user import user as user_service
from walis.utils.misc import ttype2dict
from walis.utils.model import model2dict

MAX_LIMIT = 1000


"""
sync zeus bankcard and walis bankcard
"""


def main():
    begin_time = time.time()
    print('start to diff walis and zeus bankcard. start_at:{}'.format(time.ctime()))
    check_rst()
    print('finish. end_at:{}({})'.format(time.ctime(), time.time() - begin_time))


def check_rst():
    offset = 0
    limit = MAX_LIMIT
    while 1:
        rst_ids = _get_rst_ids(limit, offset)
        print('-'*30)
        print("rst between:{}-{}, rst_count:{}, ".format(rst_ids[0], rst_ids[-1], len(rst_ids)), end="")
        walis_bankcards = rst_inner.query_bankcard_by_rst_ids(rst_ids, status=RstBankCard.STATUS_VALID)
        walis_bankcard_dict = _get_bankcard_dict(walis_bankcards)

        zeus_bankcard_dict = rst_inner.query_zeus_bankcard_by_rst_ids(rst_ids)
        print("rst_bankcard_count:{}, ".format(len(zeus_bankcard_dict)))
        user_ids = [bankcard.user_id for bankcard in zeus_bankcard_dict.itervalues()]
        user_dict = _get_user_dict(user_ids)
        user_profile_dict = _get_user_profile(user_ids)

        _diff_bankcard(walis_bankcard_dict, zeus_bankcard_dict, user_dict, user_profile_dict)
        print('-'*30)
        offset += limit

        if len(rst_ids) < limit:
            break


@db_commit
def _diff_bankcard(walis_bankcard_dict, zeus_bankcard_dict, user_dict, user_profile_dict):
    add_num = 0
    change_num = 0
    same_num = 0
    not_admin_num = 0
    session = DBSession()
    for zb_rst_id, zb in zeus_bankcard_dict.iteritems():
        wb = walis_bankcard_dict.get(zb_rst_id)
        rst_admin = user_profile_dict.get(zb.user_id)
        if rst_admin is None:
            not_admin_num += 1
            continue
        if wb is not None:
            if zb.card_id.strip() == wb.card_id.strip():
                same_num += 1
                continue
            else:
                change_num += 1
                print('walis_bankcard({}) is not same with zeus({}):{}=>{}'
                      .format(wb.id, zb.id, model2dict(wb), ttype2dict(zb)))
                _current_to_history(wb)
                session.add(wb)
                new_wb = _force_add_rst_bankcard(rst_id=zb_rst_id, username=user_dict[zb.user_id]['username'],
                                                 cardholder_name=zb.cardholder_name, card_id=zb.card_id,
                                                 bank_id=zb.bank_id, mobile=rst_admin.mobile,
                                                 status=RstBankCard.STATUS_VALID)
                session.add(new_wb)
        else:
            add_num += 1
            print('zeus_bankcard({}) does not exist in walis:{}'.format(zb.id, ttype2dict(zb)))
            new_wb = _force_add_rst_bankcard(rst_id=zb_rst_id, username=user_dict[zb.user_id]['username'],
                                             cardholder_name=zb.cardholder_name, card_id=zb.card_id,
                                             bank_id=zb.bank_id, mobile=rst_admin.mobile,
                                             status=RstBankCard.STATUS_VALID)
            session.add(new_wb)

    print('(add_num:{add_num}, change_num:{change_num}, same_num:{same_num}, not_admin_num:{not_admin_num})'
          .format(add_num=add_num, change_num=change_num, same_num=same_num, not_admin_num=not_admin_num))


def _get_user_dict(user_ids):
    user_list = user_service.get(user_ids)

    return {user['id']: user for user in user_list}


def _get_rst_ids(limit=MAX_LIMIT, offset=0):
    with thrift_client('ers') as ers:
        query = thirdparty_svc.ers.TRestaurantQuery()
        query.is_valid = 1
        query.limit = limit
        query.offset = offset
        rst_list = ers.walle_query_restaurant(query)

    rst_ids = [rst.id for rst in rst_list]
    rst_ids.sort()
    return rst_ids


def _get_user_profile(user_ids):
    user_profiles = user_service.mget_profile(user_ids)
    return {user_profile.user_id: user_profile for user_profile in user_profiles}


def _get_bankcard_dict(bankcard_list):
    return {bankcard.rst_id: bankcard for bankcard in bankcard_list}


def _force_add_rst_bankcard(rst_id, username, cardholder_name, card_id, bank_id, mobile, status):
    new_wb = RstBankCard(rst_id=rst_id, username=username, cardholder_name=cardholder_name,
                         card_id=card_id, bank_id=bank_id, mobile=mobile, status=status)
    return new_wb


def _current_to_history(wb):
    wb.status = RstBankCard.STATUS_HISTORY


if "__main__" == __name__:
    main()
