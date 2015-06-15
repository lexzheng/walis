#!/usr/bin/env python2
# coding=utf8

from __future__ import absolute_import, division, print_function

from flask import request, redirect
from webargs import Arg

from walis.service import (
    get_file_url,
    upload_file,
    delete_file,
)
from walis.utils.http import args_parser, jsonpickle_dumps


def get(file_hash):
    args = args_parser.parse_all()
    isprivate=args.get('isprivate',False)
    file_url = get_file_url(file_hash,isprivate=isprivate)
    return {'file_url': file_url}


def upload():
    # TODO try to parse file in webargs **********
    image_file = request.files['file']
    args = args_parser.parse_all()
    isprivate=args.get('isprivate',False)
    file_hash = upload_file(image_file,isprivate=isprivate)
    return {'file_hash': file_hash}


def delete():
    args = args_parser.parse_all()
    isprivate=args.get('isprivate',False)
    file_hash = args_parser.parse(
        {'file_hash': Arg(str), }).get('file_hash')

    delete_file(file_hash,isprivate=isprivate)
    return ''

def hash2url(hash):
    '''
    :return: redirect to real image url via hash
    '''
    args = args_parser.parse_all()
    isprivate=args.get('isprivate',False)
    return redirect(get_file_url(hash,isprivate=isprivate))
