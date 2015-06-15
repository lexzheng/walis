#!/usr/bin/env python2
# coding=utf8

from __future__ import absolute_import, division, print_function


RESTAURANT_PHONE_DIVIDER = ' '


def get_rst_lock_key(restaurant_id):
    return '.'.join(('rizzrack.voicecall.restaurant.', str(restaurant_id)))


def get_call_lock_key(call_id):
    return '.'.join(('rizzrack.voicecall.call.', str(call_id)))


#TODO 可改成正则
def get_rst_takeout_phone(restaurant):
    phone_list = restaurant.phone.split(RESTAURANT_PHONE_DIVIDER)
    mobile = restaurant.mobile

    phones = [phone for phone in phone_list if phone]

    if not phones:
        return mobile

    if len(phones) == 1:
        return phones[0]

    for phone in phones:
        if phone and phone != mobile:
            return phone

    return ''
