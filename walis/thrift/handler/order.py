#!/usr/bin/env python2
# coding=utf8

from __future__ import absolute_import, division, print_function
from walis.core.db.mongo import mongo


def is_suspicious_order_auditor(auditor_id):
    spec = {
        'user_id': auditor_id,
    }
    doc = mongo.dop_user.find_one(spec)
    if doc is None:
        return False
    else:
        return doc['allow_order_audit']
