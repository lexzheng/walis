#!/usr/bin/env python2
# -*- coding: utf8 -*-

from __future__ import print_function, division, absolute_import

import json
from walis.thirdparty import thrift_client

def region_area_to_es_points(area):
    try:
        area = json.loads(area)
        point = area[0]['point']
        points = []
        for p in point:
            lat,lon = p.split(',')
            points.append({'lat':lat,'lon':lon})
    except:
        points = []
    return points

import os
def image_hash_to_url(image_hash):
    if not image_hash:
        return ''
    try:
        paths = ['http://fuss10.elemecdn.com/', image_hash[0:1], image_hash[1:3], image_hash[3:]]
        path = os.path.join(*paths)
        path += '.{}'.format(image_hash[32:])
        return path
    except Exception as e:
        return ''

def ess_search2(index,doc_type, query):
    with thrift_client('ess') as ess_client:
        result = ess_client.search2(index, doc_type, query)
    result = json.loads(result)
    return result

def extract_ess_search_result(ess_search_result):
    hits = ess_search_result['hits']
    objects = []
    for entity in hits:
        source = entity['_source']
        entity.pop('_source')
        source.update(entity)
        objects.append(source)
    total = ess_search_result['total']
    result = {
        'objects':objects,
        'total':total,
    }
    return result
