#!/usr/bin/env python2
# -*- coding: utf8 -*-

from __future__ import print_function, division, absolute_import

from flask.ext.login import current_user

from walis.model.walis.rst import CertificationProcessingRecord
from walis.model.walis import db_commit

def get(restaurant_id):
    return CertificationProcessingRecord.get_by_restaurant_id(
        restaurant_id)


def get_latest_record(restaurant_id):
    return CertificationProcessingRecord.get_latest_record(restaurant_id)


def mget_latest_record(rst_ids):
    results = []
    index = 0
    MAX_SIZE = 100
    while True:
        partial_ids = rst_ids[index*MAX_SIZE: (index+1)*MAX_SIZE]
        results.extend(
            CertificationProcessingRecord.mget_latest_record(partial_ids))
        if len(partial_ids) < MAX_SIZE:
            break
        index += 1

    return results


def get_processing_records(restaurant_id):
    return CertificationProcessingRecord.get_by_restaurant_id(
        restaurant_id)


@db_commit
def add(restaurant_id, cert_type,
        status_from, status_to, comment=None):
    CertificationProcessingRecord.add(
        current_user.id,
        restaurant_id,
        cert_type,
        status_from,
        status_to,
        comment)
