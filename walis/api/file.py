#!/usr/bin/env python2
# coding=utf8

from __future__ import absolute_import, division, print_function

from walis.core.api import api

from .base import BaseApi
from .handler import file


class FileApi(BaseApi):

    def get(self, file_hash):
        return file.get(file_hash)

    def post(self):
        return file.upload()

    def delete(self):
        return file.delete()

    @api('/hash_image/<hash>')
    def hash2url(self, hash):
        return file.hash2url(hash)
