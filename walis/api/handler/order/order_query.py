#!/usr/bin/env python2
# -*- coding: utf8 -*-

from __future__ import print_function, division, absolute_import

import arrow
import pymongo
import json

from flask.ext.login import current_user

from walis.utils.http import Arg, args_parser
from walis.utils.misc import getresult_to_raw
from walis.service.rst import restaurant as rst_base
from walis.thirdparty import thrift_client

from walis.api.handler.order import order_query_helper
from .utils import image_hash_to_url

from walis import config

def query():
    args_spec = {
        'query':Arg(unicode,default='{}'),
        'struct':Arg(unicode,default='{}'),
    }
    args = args_parser.parse(args_spec)
    result = order_query_helper.ess_search2(**args)
    return result

def struct():
    return order_query_helper.get_struct(current_user.id)

def query_suspicous():
    args_spec = {
        'start_datetime':Arg(unicode, default=arrow.now().replace(days=-1).__str__()),
        'end_datetime':Arg(unicode, default=arrow.now().__str__()),
        'restaurant_id':Arg(int),
        'offset':Arg(int,default=0),
        'limit':Arg(int,default=100),
    }
    args = args_parser.parse(args_spec)
    if not args['restaurant_id']:
        return {
            'total':0,
            'objects':[],
    }
    client = pymongo.MongoClient(config.EYES_MONGO)
    collection = client.evileye.suspicious_order
    # db.tickets.find({"date":{$lt:ISODate("2013-01-17T01:16:33.303Z")}}).limit (5);
    start_datetime = args['start_datetime'].split('+')[0]
    end_datetime = args['end_datetime'].split('+')[0]

    start_datetime = arrow.get(start_datetime).to('local').datetime
    end_datetime = arrow.get(end_datetime).to('local').datetime
    restaurant_id = args['restaurant_id']
    offset = args['offset']
    limit = args['limit']
    query = {
        'created_at':{'$lte':end_datetime,'$gte':start_datetime},
    }
    if restaurant_id:
        query.update({'restaurant_id':restaurant_id})
    docs = collection.find(query)
    total = docs.count()
    result_docs = list(docs.limit(limit).skip(offset))
    time_fields = ['deliver_time','settled_at']
    with thrift_client('eos') as eos:
        for doc in result_docs:
            order_id = doc['_id']
            order = eos.get(int(order_id))
            order = getresult_to_raw(order)
            for k,v in order.items():
                doc.setdefault(k,v)
            doc['detail_json'] = json.loads(doc['detail_json'])
            doc['_order_id'] = doc['_id']
            for field in time_fields:
                new_value = arrow.get(doc[field]).__str__()
                doc[field] = new_value
            doc['phone'] = [doc['phone']]
            with thrift_client('eus') as eus_client:
                chaos = eus_client.get_order_payment_constitution_map([int(order_id)])
                payment_constituion = chaos.get(order['id'],[])
                doc['payment_constituion'] = order_query_helper.whatzfvcksay(payment_constituion,doc['total'])
            doc['order_id'] = unicode(doc['_id'])
    order_ids = [doc['id'] for doc in result_docs]
    with thrift_client('eyes') as eyes_client:
        suspicious_orders = eyes_client.walle_get_suspicious_order_detail(order_ids)
        suspicious_orders = getresult_to_raw(suspicious_orders)
        suspicious_orders_map = {order.id:order for order in suspicious_orders}
    for _object in result_docs:
        suspicious = suspicious_orders_map.get(_object['id'],{})
        _object['_order_suspicious_reason'] = suspicious.get('reasons',[])
    restaurant_ids = list(set([o['restaurant_id'] for o in result_docs]))
    restaurants = rst_base.get(restaurant_ids)
    for r in restaurants:
        r['_image_url'] = image_hash_to_url(r['image_hash'])
    restaurant_map = {r.id:r for r in restaurants}
    for order in result_docs:
        order['_restaurant'] = restaurant_map[order['restaurant_id']]
    result = {
        'total':total,
        'objects':result_docs,
    }
    return result
