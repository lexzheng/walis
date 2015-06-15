#!/usr/bin/env python2
# -*- coding: utf8 -*-

from __future__ import print_function, division, absolute_import

from flask.ext.login import current_user

from . import cert_record_process as record_process_base
from walis.thirdparty import thrift_client, thirdparty_svc
from walis.exception.util import raise_user_exc
from walis.exception.error_code import CERT_UPDATE_ERR

TRestaurantCertification = thirdparty_svc.ers.TRestaurantCertification

CERTIFICATION_TYPE_NONE = 0
RESTAURANT_NOT_EXIST_ID = -1
CERTIFICATION_NOT_EXIST = -2

CertType = thirdparty_svc.ers.CertificationConst
STATUS_PENDING = CertType.STATUS_PENDING
STATUS_PASSED = CertType.STATUS_PASSED
STATUS_FAILED = CertType.STATUS_FAILED

TYPE_CERT_PERSONAL = thirdparty_svc.ers.RestaurantConst.CERTIFICATION_TYPE_PERSONAL
TYPE_CERT_CORP = thirdparty_svc.ers.RestaurantConst.CERTIFICATION_TYPE_CORP


def get(restaurant_id):
    with thrift_client('ers') as ers:
        cert = ers.get_restaurant_certification(restaurant_id)
    cert.comment = cert.comment.encode('utf-8')
    return cert


def get_by_status(status, offset=0, limit=thirdparty_svc.ers.MAX_LIST_SIZE):
    limit = 250
    with thrift_client('ers') as ers:
        return ers.query_restaurant_certification_by_status(
            status, offset, limit)


def add(cert):
    with thrift_client('ers') as ers:
        ers.add_restaurant_certification(cert)
    record_process_base.add(
        cert.restaurant_id,
        cert.type,
        CERTIFICATION_NOT_EXIST,
        STATUS_PENDING,
        comment='上传个人认证信息' if cert.type ==
                TYPE_CERT_PERSONAL else '上传企业认证信息')
    return ''


def update(cert):
    with thrift_client('ers') as ers:
        db_cert = ers.get_restaurant_certification(cert.restaurant_id)

    if not db_cert:
        raise_user_exc(CERT_UPDATE_ERR, restaurant_id=cert.restaurant_id)

    with thrift_client('ers') as ers:
        ers.update_restaurant_certification(cert)

    record_process_base.add(
        cert.restaurant_id,
        cert.type,
        cert.status,
        STATUS_PENDING,
        comment='修改认证信息')
    return ''


def process_certification(restaurant_id, status_to):
    with thrift_client('ers') as ers:
        ers.process_certification(current_user.id,
                                  restaurant_id, status_to)


def get_latest_record(restaurant_id):
    nopass_record = record_process_base.get_latest_record(
        restaurant_id)

    comment = ''
    cert_status = CERTIFICATION_NOT_EXIST
    if nopass_record:
        comment = nopass_record.comment
        cert_status = nopass_record.status_to

    return comment, cert_status
