#!/usr/bin/env python2
# -*- coding: utf8 -*-

from __future__ import absolute_import, division, print_function

import os

from flask import request
from webargs import Arg
from werkzeug.exceptions import BadRequestKeyError

from walis.thirdparty import thirdparty_svc
from walis.api.handler.cert.watermark import watermark_raw
from walis.service.utils import file as file_base
from walis.service.user import user as user_base
from walis.service.cert import cert_record_process as record_base
from walis.service.cert import cert as cert_base
from walis.service.rst import restaurant as rst_base

from walis.utils.paging import paging, get_paging_params
from walis.utils.http import args_parser
from walis.utils.misc import dict2object, object2dict
from walis.utils.format import to_int
from walis.utils.time import datetime2timestamp

from walis.exception.util import raise_user_exc
from walis.exception.error_code import (
    CERT_NOT_EXISTS_ERR,
    CERT_NOT_PENDING_ERR,
    CERT_PROC_ILL_ERR,
    CERT_IMAGE_URL_ERR,
)

CERTIFICATION_TYPE_NONE = 0
RESTAURANT_NOT_EXIST_ID = -1
CERTIFICATION_NOT_EXIST = -2

TRestaurantCertification = thirdparty_svc.ers.TRestaurantCertification

CertType = thirdparty_svc.ers.CertificationConst
RESTAURANT_CONST = thirdparty_svc.ers.RestaurantConst
# certification status
CERTIFICATION_CONST = thirdparty_svc.ers.CertificationConst

STATUS_PENDING = CertType.STATUS_PENDING
STATUS_PASSED = CertType.STATUS_PASSED
STATUS_FAILED = CertType.STATUS_FAILED

TYPE_CERT_PERSONAL = thirdparty_svc.ers.RestaurantConst.CERTIFICATION_TYPE_PERSONAL
TYPE_CERT_CORP = thirdparty_svc.ers.RestaurantConst.CERTIFICATION_TYPE_CORP



def get(restaurant_id):
    certification=''
    try:
        certification = cert_base.get(int(restaurant_id))
    except BaseException as e:
        raise_user_exc(CERT_NOT_EXISTS_ERR, restaurant_id=restaurant_id)
    return {'certification': certification}


def add():
    args = args_parser.parse_all()
    _set_files_into_args(args)
    cert = dict2object(args, TRestaurantCertification())
    _format_certification(cert)
    return cert_base.add(cert)


def update():
    args = args_parser.parse_all()
    _set_files_into_args(args)
    cert = dict2object(args, TRestaurantCertification())
    _format_certification(cert)
    return cert_base.update(cert)

def get_by_uploader(restaurant_id):
    certification=''
    try:
        certification = _get_certification_with_url(restaurant_id)
    except Exception as e:
        return None
    comment, cert_status = cert_base.get_latest_record(restaurant_id)
    return {'comment': comment,
                             'status': cert_status,
                             'certification': certification}


def get_by_admin(restaurant_id):
    certification=''
    try:
        certification = _get_certification_with_url(restaurant_id)
    except Exception as e:
        return None

    response_map = {'certification': certification}

    pre_rest_id, next_rest_id = _get_pre_next_restaurant_ids(
        restaurant_id)

    response_map['pre_restaurant_id'] = pre_rest_id
    response_map['next_restaurant_id'] = next_rest_id

    return response_map


def get_list_from_mm():
    args_spec = {
        'cert_type': Arg(int, allow_missing=True),
        'cert_status': Arg(int, allow_missing=True),
        'time_from': Arg(str, allow_missing=True),
        'time_to': Arg(str, allow_missing=True),
        'restaurant_id_or_name': Arg(unicode, allow_missing=True),
    }
    args = args_parser.parse(args_spec)
    cert_type = args.get('cert_type', None)
    status = args.get('cert_status')
    time_from = args.get('time_from', None)
    time_to = args.get('time_to', None)
    restaurant_id_or_name = args.get('restaurant_id_or_name', None)

    page_no, page_size = get_paging_params()
    offset = (page_no-1)*page_size

    certs = cert_base.get_by_status(status)

    if not certs:
        return {'cert_list': [], 'total_num': 0}

    response_certs = _assemble_cert_response(certs)

    if cert_type:
        response_certs = filter(lambda res: res['type'] == cert_type,
                                response_certs)

    if time_from:
        response_certs = filter(lambda res: time_from <
                                res['application_time'], response_certs)

    if time_to:
        response_certs = filter(lambda res: res['application_time'] <
                                time_to, response_certs)

    if restaurant_id_or_name is not None:
        response_certs = filter(
            lambda res: restaurant_id_or_name in
            str(res['restaurant_id']) + res['restaurant_name'],
            response_certs)

    return {'total_num': len(response_certs),
                             'cert_list': paging(response_certs)}


def get_processing_record(restaurant_id):
    processing_records = record_base\
        .get_processing_records(restaurant_id)
    users = user_base.mget_users(
        [record.process_user_id for record in processing_records]
    )

    response_pack = []
    attrs_to_pack = ['process_user_id', 'status_to', 'comment',
                     'created_at']
    for index, record in enumerate(processing_records):
        record_pack = {'process_user_name': users[index].username}
        for name in attrs_to_pack:
            record_pack[name] = getattr(record, name)
        response_pack.append(record_pack)

    return response_pack


def processing():
    args = args_parser.parse_all()
    status_to = int(args.get('status'))
    comment = args.get('comment', '')
    restaurant_id = int(args.get('restaurant_id'))
    cert = cert_base.get(restaurant_id)

    if status_to != CERTIFICATION_CONST.STATUS_PASSED and \
       status_to != CERTIFICATION_CONST.STATUS_FAILED:
        raise_user_exc(CERT_PROC_ILL_ERR)

    if cert.status != CERTIFICATION_CONST.STATUS_PENDING:
        raise_user_exc(CERT_NOT_PENDING_ERR)

    cert_base.process_certification(restaurant_id, status_to)

    record_base.add(restaurant_id, cert.type,
                        cert.status, status_to, comment)
    return ''


def _set_files_into_args(args):
    file_names = [
        'identity_card_image_front',
        'identity_card_image_back',
        'health_card_image_front',
        'health_card_image_back',
        'license_image',
        'restaurant_service_license_copy'
    ]

    for file_name in file_names:
        try:
            file = request.files[file_name]
        except BadRequestKeyError as error:
            continue
        ext = os.path.splitext(file.filename)[1].lstrip('.')
        buf = file.stream.read()#有可能产生问题，file可能获取但无法读取

        args[file_name] = file_base.file_upload_raw(buf, ext,isprivate=True)
        args[file_name + '_wm'] = file_base.file_upload_raw(watermark_raw(buf, ext), ext,isprivate=True)


def _get_pre_next_restaurant_ids(restaurant_id):
    certs = cert_base.get_by_status(STATUS_PENDING)

    restaurant_ids = [cert.restaurant_id for cert in certs]

    pre_id = next_id = RESTAURANT_NOT_EXIST_ID
    try:
        index = restaurant_ids.index(restaurant_id)
    except ValueError:
        return pre_id, next_id

    if index != 0:
        pre_id = restaurant_ids[index - 1]
    if index != len(restaurant_ids) - 1:
        next_id = restaurant_ids[index + 1]
    return pre_id, next_id


def _assemble_cert_response(certs):
    if not certs:
        return []

    response_map = object2dict(certs)
    restaurant_ids = [r['restaurant_id'] for r in response_map]
    restaurants = rst_base.mget(restaurant_ids)
    restaurant_map = {r.id: r.name for r in restaurants}

    for index, rest in enumerate(restaurants):
        response_map[index]['restaurant_name'] = rest.name

    # process_records = record_base.mget_latest_record(restaurant_ids)
    # process_records = {"{0}".format(record.restaurant_id):record for record in process_records}

    for cert_dict in response_map:

        application_time = cert_dict['created_at']
        process_record = record_base.get_latest_record(
            cert_dict['restaurant_id'])
        # process_record = process_records.get(
        #     cert_dict['restaurant_id'])

        if process_record:
            application_time = \
                datetime2timestamp(process_record.created_at)

        cert_dict['application_time'] = application_time

        cert_dict['restaurant_name'] = \
            restaurant_map.get(cert_dict['restaurant_id'], '')

    return response_map


def _get_certification_with_url(restaurant_id):
    cert = cert_base.get(restaurant_id)

    file_names = ['identity_card_image_front',
               'identity_card_image_back',
               'health_card_image_front',
               'health_card_image_back',
               'license_image',
               'restaurant_service_license_copy']
    for file_name in file_names:
        obj = getattr(cert, file_name, None)
        if obj:
            try:
                url=file_base.get_file_url(obj, isprivate=True)
                if url:
                    setattr(
                        cert, file_name, url)
            except Exception as e:
                continue
    return cert


def _format_certification(cert):
    cert.restaurant_id = to_int(cert.restaurant_id)
    cert.type = to_int(cert.type)
    cert.status = to_int(cert.status)

