#! /usr/bin/env python2
# -*- coding:utf-8 -*-

from __future__ import absolute_import, division, print_function

__author__ = 'Linktime'

from walis.thirdparty.coffee import coffee
from walis.thirdparty.coffee import OUT_SYSTEM


def check_rst_permission(rst_id, sso_user_id):
    return coffee.rst_manage_rst.isRstOwner(context=OUT_SYSTEM, rstId=rst_id, userId=sso_user_id)
