#!/usr/bin/env python2
# coding=utf8

from __future__ import absolute_import, division, print_function

from walis.service.rst import restaurant as rst_base
from walis.service.user import user as user_base
from walis.model.walis.cs import CSEvent


def get_user_by_phone(mobile):
    user_type = None
    result = {'user_type': CSEvent.USER_TYPE_OTHERS}
    rst = rst_base.get_by_mobile(mobile)
    if rst:
        user_type = CSEvent.USER_TYPE_MERCHANT
        result = {
            'user_type': user_type,
            'restaurant_id': rst.id,
            'restaurant_name': rst.name,
            'phone': rst.phone
        }

    user = user_base.get_by_mobile(mobile)
    if not user:
        return result

    result.update({'user_id': user.id, 'user_name': user.username})
    if user_type == CSEvent.USER_TYPE_MERCHANT:
        return result

    is_marketing = user_base.has_groups(
        user.id,
        ['region_director', 'city_director', 'entry_director']
    )
    if is_marketing:
        result.update({'user_type': CSEvent.USER_TYPE_MARKETING})
    else:
        result.update({'user_type': CSEvent.USER_TYPE_USER})

    return result
