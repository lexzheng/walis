#!/usr/bin/env python2
# -*- coding: utf8 -*-

from __future__ import absolute_import, division, print_function

from walis.thirdparty import thrift_client, thirdparty_svc
from walis.utils.misc import any_to_raw

DEFAULT_LIMIT = thirdparty_svc.eus.MAX_LIST_SIZE


def get(pk_or_pks):
    with thrift_client('eus') as eus:
        if isinstance(pk_or_pks, (tuple, list)):
            pk_or_pks = list(set(pk_or_pks))
            result = eus.mget(pk_or_pks)
        else:
            result = eus.get(pk_or_pks)
    result = any_to_raw(result)
    return result


mget = get


def get_user(user_id):
    with thrift_client('eus') as eus:
        user = eus.get(user_id)
    return user


def mget_users(user_ids):
    with thrift_client('eus') as eus:
        users = eus.mget(user_ids)
    return users


def get_profile(user_id):
    '''
    :param user_id:int
    :return:TUserProfile
    '''
    with thrift_client('eus') as eus:
        profile = eus.get_profile(user_id)
    return profile


def mget_profile(user_ids):
    with thrift_client('eus') as eus:
        profiles = eus.mget_profile(user_ids)
    return profiles

def get_by_mobile(mobile):
    '''
    :param mobile:string
    :return:TUser
    '''
    with thrift_client('eus') as eus:
        try:
            user = eus.get_by_mobile(mobile.strip())
        except thirdparty_svc.eus.EUSUserException:
            user = None

    return user


def get_by_username(username):
    try:
        with thrift_client('eus') as eus:
            user = eus.get_by_username(username)
    except thirdparty_svc.eus.EUSUserException:
        user = {}
    return user


def is_username_available(username):
    '''
    :param username:string
    :return:True or False
    '''
    try:
        with thrift_client("eus") as eus:
            available = eus.is_username_available(username)
    except thirdparty_svc.eus.EUSUserException:
        available = False
    return available


def bind_mobile(user_id, mobile):
    with thrift_client('eus') as eus:
        eus.bind_mobile(user_id, mobile)


def unbind_mobile(user_id):
    with thrift_client('eus') as eus:
        eus.walle_unbind_mobile(user_id)


def bankcard_bind(user_id, card_id, bank_id, cardholder_name):
    with thrift_client('eus') as eus:
        eus.bankcard_bind(user_id, card_id, bank_id, cardholder_name)


def unbind_bankcard_by_user(user_id):
    BANKCARD_STATUS = thirdparty_svc.eus.UserBankcardStatus
    with thrift_client('eus') as eus:
        try:
            bankcard = eus.get_bankcard(user_id, BANKCARD_STATUS.VALID)
            eus.delete_bankcard(bankcard.id)
        except thirdparty_svc.eus.EUSUserException:
            pass


def is_superadmin(user_id):
    with thrift_client('eus') as eus:
        user = eus.get(user_id)
        return user.is_super_admin


def get_director_ids_by_area(region_ids=None, region_group_ids=None,
                             city_ids=None):
    with thrift_client('ers') as ers:
        user_ids = ers.get_director_ids_by_area(region_ids, region_group_ids,
                                                city_ids)
    return user_ids


def get_bankcard(user_id, status=None):
    with thrift_client("eus") as eus:
        try:
            bankcard = eus.get_bankcard(user_id, status)
            return bankcard
        except thirdparty_svc.eus.EUSUserException:
            return None


def has_groups(user_id, permission_groups, is_strict=False):
    if not permission_groups or type(permission_groups) not in (list, tuple):
        return False

    with thrift_client('eus') as eus:
        groups = eus.query_user_group(user_id)

    if not groups:
        return False

    group_names = [group.name for group in groups]

    if is_strict:
        return list(set(permission_groups) - set(group_names)) == []
    else:
        return list(set(permission_groups) & set(group_names)) != []
