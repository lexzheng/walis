#!/usr/bin/env python2
# -*- coding: utf8 -*-

from __future__ import division, print_function, absolute_import

import json
import random
from collections import defaultdict

from flask.ext.login import current_user

from walis.thirdparty import thrift_client, thirdparty_svc
from walis.utils.misc import getresult_to_raw
from walis.service.region import city as city_base
from walis.service.rst import restaurant as rst_base
from walis.utils.misc import any_to_raw

from .utils import image_hash_to_url, region_area_to_es_points, ess_search2 as _ess_search2, extract_ess_search_result

PAY_TYPE_BALANCE = 1
PAY_TYPE_DIRECTLY = 2
PAY_TYPE_ECREDIT = 3
PAY_TYPE_HONGBAO = 4
PAY_TYPE_PAYMENT_DISCOUNT = 5

kv_dic = {
    PAY_TYPE_BALANCE:u'余额支付',
    PAY_TYPE_DIRECTLY:u'直接在线支付',
    PAY_TYPE_ECREDIT:u'在线支付立减',
    PAY_TYPE_HONGBAO:u'红包'
    #PAY_TYPE_PAYMENT_DISCOUNT
}

def whatzfvcksay(fvck,total):
    results = []
    total_amount = 0
    for x in fvck:
        results.append(u'{}:{}'.format(kv_dic[x.pay_type],x.amount))
        total_amount+=x.amount
    rest = total - total_amount
    if rest > 0:
        results.append(u'{}:{}'.format(u'现金',rest))
    return results


def regions_from_struct(input_struct,his_struct):
    city_ids = input_struct.get('city_ids',[])
    region_group_ids = input_struct.get('region_group_ids',[])
    region_ids = input_struct.get('region_ids',[])
    all_region_ids = []
    for city_id in city_ids:
        for city in his_struct:
            if city_id == city.id:
                for region_group in city._region_groups:
                    for region in region_group._regions:
                        all_region_ids.append(region.id)
    for region_group_id in region_group_ids:
        for city in his_struct:
            for region_group in city._region_groups:
                if region_group.id == region_group_id:
                    for region in region_group._regions:
                        all_region_ids.append(region.id)
    for region_id in region_ids:
        all_region_ids.append(region_id)
    all_region_ids = list(set(all_region_ids))
    with thrift_client('ers') as ers:
        result = ers.mget_region(all_region_ids)
        result = getresult_to_raw(result)
        return result.values()

'''
{"filter": {"geo_polygon": {"eleme_order.location": {"points": [{"lat": "31.014028", "lon": "121.42107"}, {"lat": "31.010424", "lon": "121.422358"}, {"lat": "31.007408", "lon": "121.413002"}, {"lat": "31.023076", "lon": "121.406479"}, {"lat": "31.035138", "lon": "121.446047"}, {"lat": "31.023297", "lon": "121.451347"}, {"lat": "31.018938", "lon": "121.436369"}, {"lat": "31.012392", "lon": "121.439652"}, {"lat": "31.008143", "lon": "121.42843"}, {"lat": "31.014985", "lon": "121.42446"}]}}}}
'''

def ess_search2(**args):
    def calc_index(query):
        return 'order'
    doc_type = 'eleme_order'
    query = args['query']
    index = calc_index(query)
    q = json.loads(query)
    if 'filter' not in q:
        q['filter'] = {}
    if 'bool' not in q['filter']:
        q['filter']['bool'] = {}
    struct = args['struct']
    struct = json.loads(struct)
    regions = []
    current_user_struct = get_struct(current_user.id)
    if not current_user_struct:
        return {'total':0,'objects':[]}

    #处理未分组
    is_ungroup = False
    _region_groups_ids = struct.get('region_group_ids',[])
    with thrift_client('ers') as ers:
        _result = ers.mget_region_group(_region_groups_ids)
        _result = getresult_to_raw(_result)
    for _region_group in _result.values():
        if _region_group.name.find(u'未分组') >= 0:
            is_ungroup = True
            with thrift_client('ers') as ers:
                region_query = thirdparty_svc.ers.TRegionQuery()
                region_query.city_ids = [_region_group.city_id]
                regions = ers.query_region(region_query)
                regions = any_to_raw(regions)
                regions = getresult_to_raw(regions)
            should = []
            for region in regions:
                should.append(
                    {
                        'geo_polygon':{
                            'eleme_order.location':{
                                'points':region_area_to_es_points(region.area)
                            }
                        }
                    }
                )
            q['filter']['bool']['must_not'] = [
                #{'filter':{
                {
                    'bool':{
                        'should':should,
                        #'mininum_should_match':1,
                    }
                }
                #}
            ]
            restaurant_q = {
                "fields" : [],
                "filter" : {
                    "term" : { "city_id" : _region_group.city_id}
                },
                "from" : 0,
                "size" : random.randint(100000,500000),
            }
            restaurant_q = json.dumps(restaurant_q)
            result1 = _ess_search2('restaurant','restaurant',restaurant_q)
            result1 = result1['hits']
            city_restaurant_ids = [r['_id'] for r in result1]
            q['filter']['bool']['must'].append(
                {
                    'terms':{'restaurant_id':city_restaurant_ids}
                }
            )
            break
    if not is_ungroup:
        city_ids = struct.get('city_ids',[])
        region_group_ids = struct.get('region_group_ids',[])
        region_ids = struct.get('region_ids',[])
        if struct:
            regions = regions_from_struct(input_struct=struct,his_struct=current_user_struct)
        if not city_ids and not region_group_ids and not region_ids:
            regions = []
            for city in current_user_struct:
                for region_groups in city._region_groups:
                    for region in region_groups._regions:
                        regions.append(region)
        if regions:
            should = []
            for region in regions:
                points = region_area_to_es_points(region.area)
                if points:
                    should.append(
                        {
                            'geo_polygon':{
                                'eleme_order.location':{
                                    'points':region_area_to_es_points(region.area)
                                }
                            }
                        }
                    )
            q['filter']['bool']['should'] = should

    query = json.dumps(q)

    result = _ess_search2(index,doc_type,query)
    result = extract_ess_search_result(result)

    order_ids = [order['id'] for order in result['objects']]
    with thrift_client('eos') as eos:
        orders_info = eos.mget_order_info(order_ids)
        orders_info = getresult_to_raw(orders_info)
    orders_info = {info['order_id']:info for info in orders_info}
    for order in result['objects']:
        order.update(orders_info[order['id']])
    for order in result['objects']:
        if order['phone_rating'] == 1:
            order['is_new_user'] = True
        else:
            order['is_new_user'] = False
    with thrift_client('eus') as eus_client:
        chaos = eus_client.get_order_payment_constitution_map(order_ids)
    for order in result['objects']:
        payment_constituion = chaos.get(order['id'],[])
        order['payment_constituion'] = whatzfvcksay(payment_constituion,order['total'])
    restaurant_ids = list(set([o['restaurant_id'] for o in result['objects']]))
    restaurants = rst_base.get(restaurant_ids)
    for r in restaurants:
        r['_image_url'] = image_hash_to_url(r['image_hash'])
    restaurant_map = {r.id:r for r in restaurants}
    for order in result['objects']:
        order['_restaurant'] = restaurant_map[order['restaurant_id']]
    for _object in result['objects']:
        _object['order_id'] = unicode(_object['id'])
    with thrift_client('eyes') as eyes_client:
        suspicious_orders = eyes_client.walle_get_suspicious_order_detail(order_ids)
        suspicious_orders = getresult_to_raw(suspicious_orders)
        suspicious_orders_map = {order.id:order for order in suspicious_orders}
    for _object in result['objects']:
        suspicious = suspicious_orders_map.get(_object['id'],{})
        _object['_order_suspicious_reason'] = suspicious.get('reasons',[])
    return result


def geo_struct(user_id):
    with thrift_client('ers') as ers_client:
        user_struct = ers_client.get_direct_struct(user_id)
        #{city_ids:[], region_group_ids:[], region_ids:[5,6]}
        city_ids = user_struct['city_ids']
        cities = []
        if city_ids:
            cities = ers_client.mget_city(city_ids)
        region_group_ids = user_struct['region_group_ids']
        region_groups = []
        if region_group_ids:
            region_groups = ers_client.mget_region_group(region_group_ids)
        region_ids = user_struct['region_ids']
        regions = []
        if region_ids:
            regions = ers_client.mget_region(region_group_ids)
        result = {
            'cities':cities,
            'region_groups':region_groups,
            'regions':regions,
        }
        return result


def get_struct(user_id):
    with thrift_client('ers') as ers:
        result = ers.get_direct_struct(user_id)
        result = getresult_to_raw(result)

        region_group_query = thirdparty_svc.ers.TRegionGroupQuery()
        region_group_query.city_ids = result.city_ids
        region_group_query.show_all = True

        region_groups_of_city = ers.query_region_group(region_group_query)
        region_groups_of_city = any_to_raw(region_groups_of_city)

        region_group_ids = result.region_group_ids
        region_group_ids.extend([obj['id'] for obj in region_groups_of_city])
        region_groups = ers.mget_region_group(region_group_ids).values()
        for region_group in region_groups:
            regions = ers.get_regions_by_region_group_ids([region_group.id])
            setattr(region_group,'_regions',regions)
        regions = ers.mget_region(result.region_ids).values()
        for region in regions:
            region_group_of_alone_region = ers.get_region_group_by_region(region.id)
            for region_group in region_groups:
                if region_group_of_alone_region.id == region_group.id:
                    region_group._regions.append(region)
            else:
                setattr(region_group_of_alone_region,'_regions',[region])
                region_groups.append(region_group_of_alone_region)
        region_group_group_by_city_id = defaultdict(list)
        for region_group in region_groups:
            region_group_group_by_city_id[region_group.city_id].append(region_group)
        city_ids = list(set(result.city_ids+region_group_group_by_city_id.keys()))
        cities = city_base.get(city_ids)
        for city in cities:
            setattr(city,'_region_groups',region_group_group_by_city_id.get(city.id,[]))
        cities = getresult_to_raw(cities)
        result = cities
        return result
