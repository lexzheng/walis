#! /usr/bin/env python2
# -*- coding:utf-8 -*-

from __future__ import absolute_import, division, print_function

from datetime import date, timedelta
import json
import logging
from walis.service.analytics import trs_query_config as trs_cfg_service, inner
from walis.service.region import region as region_service
from walis.service.rst import restaurant as rst_service
from walis.utils.wkb import geojson_to_wkbelement
from walis.service.region import region as region_svc


MONTH_LIST = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
DEFAULT_MONTH_DURING = 3

log = logging.getLogger('service.transaction')


def count_daily_trs_by_area(city_id, area):
    city_trs_cfg = _get_city_trs_cfg(city_id)

    date_from = city_trs_cfg['date_from']
    date_end = city_trs_cfg['date_end']

    rst_list = rst_service.query_rst_by_area(area)

    rst_ids = [rst.id for rst in rst_list]

    daily_trs = inner.count_daily_trs(rst_ids, date_from, date_end)
    amount = float(daily_trs.amount) if daily_trs.amount else 0.0
    daily_amount = amount / ((date_end - date_from).total_seconds()/86400 + 1)
    return {'daily_amount': daily_amount,
            'date_from': date_from,
            'date_end': date_end}


def get_order_trs_by_area(city_id, area):
    city_trs_cfg = _get_city_trs_cfg(city_id)

    date_from = city_trs_cfg['date_from']
    date_end = city_trs_cfg['date_end']

    points = [[float(p.split(',')[0]), float(p.split(',')[1])]
              for p in area]
    points.append(points[0])

    polygon = {'type': 'Polygon', 'coordinates': [points]}

    area_json = geojson_to_wkbelement(json.dumps(polygon))
    daily_trs = inner.get_order_transaction(city_id, area_json)
    if not daily_trs:
        daily_trs = 0.0
    daily_amount = float(daily_trs) / 7.0

    log.info('daily_amount: {}'.format(daily_amount))
    return {'daily_amount': daily_amount,
            'date_from': date_from,
            'date_end': date_end}


def get_trs_by_region_id(region_id):
    region = region_svc.get(region_id)
    area = json.loads(region['area'])[0]['point']
    points = [[float(p.split(',')[1]), float(p.split(',')[0])]
              for p in area]
    points.append(points[0])

    polygon = {'type': 'Polygon', 'coordinates': [points]}

    area_json = geojson_to_wkbelement(json.dumps(polygon))
    log.info('area_json: {}'.format(area_json))
    daily_trs = inner.get_order_transaction(region['city_id'], area_json)
    if not daily_trs:
        daily_trs = 0.0
    daily_amount = float(daily_trs) / 7.0

    return {
        'id': region_id,
        'name': region['name'],
        'trs': round(daily_amount, 2),
    }


def _int(something):

    try:
        return int(something)
    except Exception:
        return 0



def count_all_daily_trs_by_city(city_id):
    city_trs_list = []
    regions = region_service.get_regions_by_city_id(city_id, type_code=1, show_all=False)
    for region in regions:
        region_info = get_trs_by_region_id(region['id'])
        city_trs_list.append(region_info)
    results = sorted(city_trs_list, key=lambda t: _int(t['name'].split('\xe2\x80\x94')[-1]))
    results.insert(0, {u'区域平均交易额': sum([r['trs'] for r in results]) / len(results)})
    return results


def _get_city_trs_cfg(city_id):
    city_trs_cfg = trs_cfg_service.get_by_city(city_id) or {}
    city_trs_cfg.setdefault('date_from', _default_date_from())
    city_trs_cfg.setdefault('date_end', _default_date_end())
    return city_trs_cfg


def _default_date_from():
    today = date.today()
    current_month = today.month
    year = today.year
    if current_month - DEFAULT_MONTH_DURING - 1 < 0:
        year = year - 1
    return today.replace(year=year, month=MONTH_LIST[current_month - DEFAULT_MONTH_DURING - 1], day=1)


def _default_date_end():
    today = date.today()
    return today.replace(day=1) - timedelta(days=1)


def _get_rst_in_regions(regions):
    for region in regions:
        rst_ids = rst_service.mget_restaurant_in_region([region['id'], ])
        yield region['id'], rst_ids
