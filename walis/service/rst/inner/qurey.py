#! /usr/bin/env python2
# -*- coding:utf-8 -*-

from __future__ import absolute_import, division, print_function

from walis.model.walis.rst import RstBankCard
from walis.model.walis import DBSession


def query_bankcard_by_rst_ids(rst_ids, status=None):
    query = DBSession().query(RstBankCard)

    query = query.filter(RstBankCard.rst_id.in_(rst_ids))

    if status is not None:
        query = query.filter(RstBankCard.status == status)

    return query.all()
