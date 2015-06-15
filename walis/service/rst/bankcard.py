#! /usr/bin/env python2
# -*- coding:utf-8 -*-

from __future__ import print_function, division, absolute_import

from walis.model.walis.rst import RstBankCard, RstBankCardProcessingRecord

from walis.thirdparty import thrift_client, thirdparty_svc


def get_bank_list():
    with thrift_client("eus") as eus:
        bank_list = eus.get_bank_list()
    return bank_list


def get_bank(bank_id):
    with thrift_client("eus") as eus:
        bank = eus.get_bank(bank_id)
    return bank


def get_rst_admin(rst_id):
    '''
    :param restaurant_id:int
    :return:TRestaurantAdmin
    '''
    try:
        with thrift_client('eus') as eus:
            admin = eus.get_restaurant_admin(rst_id)
    except thirdparty_svc.eus.EUSUserException:
        admin = {}
    return admin


def super_user_bind(username, mobile, restaurant_id, bank_id,
                    card_id, cardholder_name, process_user_id):
    with thrift_client('eus') as eus:
        eus.temp_super_user_bind(username, mobile, restaurant_id, bank_id,
                                 card_id, cardholder_name, process_user_id)


# ##############################################
# ################ from javis db
# ##############################################


def add_bankcard(**kwargs):
    return RstBankCard.add(**kwargs)


def update_bankcard(id, **bankcard_dict):
    return RstBankCard.update(id, **bankcard_dict)


def get_bankcard(rst_id, bankcard_id):
    return RstBankCard.get(rst_id, bankcard_id)


def query_bankcard(rst_id, status=None, limit=None, offset=None):
    return RstBankCard.query_by_rst(rst_id, status=status, limit=limit, offset=offset)


def query_by_status(rst_ids=None, status=None, type_code=None,
                    offset=0, limit=None):
    return RstBankCard.query_by_status(rst_ids=rst_ids,
                                       status=status, type_code=type_code, offset=offset, limit=limit)


def add_bankcard_processing_record(rst_id, bankcard_id,
                                   messages, process_user_id, status_to):
    return RstBankCardProcessingRecord.add(rst_id=rst_id,
                                           bankcard_id=bankcard_id,
                                           messages=messages,
                                           process_user_id=process_user_id,
                                           status_to=status_to,)


def get_pre_next(bankcard_id, status=RstBankCard.STATUS_PENDING):
    return RstBankCard.get_pre(bankcard_id, status),\
        RstBankCard.get_next(bankcard_id, status)


def get_bankcard_count(rst_ids=None, status=None, type_code=None):
    return RstBankCard.count(rst_ids, status, type_code)


def query_processing_record(rst_id, bankcard_id, limit=None):
    return RstBankCardProcessingRecord.query(rst_id, bankcard_id, limit)


def mget_processing_last_record(bankcard_ids):
    return RstBankCardProcessingRecord.mget_last_record(bankcard_ids)
