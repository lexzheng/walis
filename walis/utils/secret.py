#!/usr/bin/env python2
# coding=utf8

from __future__ import absolute_import, division, print_function


def md5(pwd):
    """
    args:
        pwd - string
    return:
        md5 result of pwd - string
    """
    import hashlib
    m = hashlib.md5()
    m.update(pwd)
    return m.hexdigest()
