#!/usr/bin/env python2
# -*- coding: utf8 -*-

from __future__ import absolute_import, division, print_function

from flask.ext.login import current_user

from walis.thirdparty import thrift_client
from walis.utils.misc import getresult_to_raw


def edit_username_mobile(user_id, username=None, mobile=None):
    if not user_id:
        return

    with thrift_client('eus') as eus:
        user = eus.get_full(user_id)
        if username is not None and user.user.username != username:
            eus.update_username(user_id, current_user.id, username)
        if mobile is not None and user.profile.mobile != mobile:
            eus.walle_change_mobile(user_id, current_user.id, mobile)

def get_user(user_id):
    with thrift_client('eus') as eus_client:
        user_profile = eus_client.get_profile(user_id)
        user = eus_client.get(user_id)
        user_profile = getresult_to_raw(user_profile)
        user = getresult_to_raw(user)
        user.update(user_profile)
    return user
