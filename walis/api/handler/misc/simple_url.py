#!/usr/bin/env python2
# -*- coding: utf8 -*-

from __future__ import division, absolute_import, print_function

from walis.model.walis.misc import Restaurant

def get_empty_image_hash_restaurant():
    restaurants = Restaurant.get_empty_image_hash_restaurant()
    content = ''
    for r in restaurants:
        content = '<br>'.join((content,
                               ', '.join((str(r.id), r.name))))
    return content
