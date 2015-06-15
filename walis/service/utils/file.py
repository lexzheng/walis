#!/usr/bin/env python2
# coding=utf8

from __future__ import absolute_import, division, print_function

import os

from walis.thirdparty import thrift_client, thirdparty_svc
from walis.exception.util import raise_zeus_exc
from walis.exception.error_code import FILE_UPLOAD_ERR


FILE_SIZE = [(640, 480), (240, 180), (190, 142)]


def get_file_url(file_hash, file_size=None,isprivate=False):
    fusshost='fuss'
    if isprivate:
        fusshost='fuss2'
    with thrift_client(fusshost) as fuss:
        if file_size is None:
            file_url = fuss.file_get(file_hash)
        else:
            file_url = fuss.file_get_sized(file_hash, file_size)

    return file_url


def upload_file(file, sized=False, watermark=False, file_size=FILE_SIZE,isprivate=False):
    file_name = file.filename
    extension_name = os.path.splitext(file_name)[1].lstrip('.')
    file_hash = file_upload_raw(
        file.stream.read(),
        extension_name,
        sized,
        watermark,
        file_size,
        isprivate
    )

    if not file_hash:
        raise_zeus_exc(FILE_UPLOAD_ERR, file_name=file_name)

    return file_hash


def delete_file(file_hash, delete_all=False, file_size=None,isprivate=False):
    fusshost='fuss'
    if isprivate:
        fusshost='fuss2'
    with thrift_client(fusshost) as fuss:
        if delete_all:
            fuss.file_delete_all(file_hash)
        elif file_size:
            fuss.file_delete_sized(file_hash, file_size)
        else:
            fuss.file_delete(file_hash)


class UploadFileError(Exception):
    pass


def file_upload_raw(buf, extension, sized=False, watermark=False,
                    file_size=FILE_SIZE,isprivate=False):

    fusshost='fuss'
    if isprivate:
        fusshost='fuss2'
    if watermark:
        sized = True
    with thrift_client(fusshost) as fuss:
        fuss_file = thirdparty_svc.fuss.FussFile()
        fuss_file.content = buf
        fuss_file.extension = extension

        if watermark:
            file_hash = fuss.file_upload_sized_with_watermarker(
                fuss_file, file_size)
        elif sized:
            file_hash = fuss.file_upload_sized(fuss_file, file_size)
        else:
            file_hash = fuss.file_upload(fuss_file)

    return file_hash
