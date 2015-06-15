#!/usr/bin/env python2
# coding=utf8

from __future__ import absolute_import, division, print_function
from collections import defaultdict

import sys
import logging
from walis.service.rst import inner
from walis.service.rst.utils import (
    get_dist,
    region_area_to_polygons,
    get_centerpoint_of_region,
    get_radius_of_region)
from walis.utils import geo
from walis.service.region import (
    region as region_base,
    inner as region_inner,
)
from walis.thirdparty import (
    thrift_client,
    thirdparty_svc,
)

log = logging.getLogger('all.restaurant.group')


REGION_TYPE_CBD = region_base.REGION_TYPE_CBD
REGION_TYPE_SCHOOL = region_base.REGION_TYPE_SCHOOL


def get_ungrouped_rst(city_id):
    q = thirdparty_svc.ers.TRestaurantInRegionQuery()
    q.region_ids = [-10 * city_id]
    q.is_valid = 1
    q.offset = 0
    q.limit = thirdparty_svc.ers.MAX_LIST_SIZE
    with thrift_client('ers') as ers:
        rsts = ers.query_restaurant_in_region(q)

    results = filter(lambda rst: rst.city_id == city_id, rsts)
    return results


def group_ungrouped_rsts(city_id):
    """ Group all ungrouped restaurants into their nearly regions

    :param city_id:
    :return:
    """
    ungrouped_rsts = get_ungrouped_rst(city_id)
    regions = region_base.get_regions_by_city_id(city_id)
    region_infos = [[r['id'], region_area_to_polygons(r['area'])]
                    for r in regions]
    for region_info in region_infos:
        region_info.append(get_centerpoint_of_region(region_info[1]))

    if not ungrouped_rsts:
        return 0

    for rst in ungrouped_rsts:
        point = (float(rst.latitude), float(rst.longitude))
        region_id = None
        for region in regions:
            if not region['area']:
                continue

            polygons = region_area_to_polygons(region['area'])
            for polygon in polygons:
                if geo.is_in_region(point, polygon, xy_reverse=True):
                    region_id = region['id']
                    break
                    
            if region_id:
                break

        if not region_id:
            region_id = region_infos[0]
            min_distance = sys.maxint
            for info in region_infos:
                center_points = info[2]
                cur_distance = min([get_dist(p, point) for p in center_points])
                if cur_distance < min_distance:
                    min_distance = cur_distance
                    region_id = info[0]
            log.info('Restaurant {} does not have matched regions. Find closest'
                     ' one with region_id {}, distance {}'.format(
                     rst.id, region_id, min_distance))

        log.info('update rst {} with region {}'.format(rst.id, region_id))
        inner.update_restaurant_region(rst.id, region_id)

    return len(ungrouped_rsts)


def group_all_restaurants(city_id, center_point, max_distance_to_center,
                          max_region_rsts_num):
    # for logging
    rst_in_region_num = 0
    rst_near_region_num = 0
    rst_far_from_region_num = 0
    exc_num = 0

    # 1. get all valid and not BOD restaurants
    rsts = inner.query_all_rsts(city_ids=[city_id], is_valid=1, is_premium=0,
                                region_type=region_base.REGION_TYPE_CBD)
    rsts_info = [{'id': r['id'],
                  'lng': r['longitude'],
                  'lat': r['latitude']} for r in rsts]
    rst_len = len(rsts)
    log.info('Step 1: query. all rsts to group count is {}'.format(rst_len))

    # 2. sort restaurants by their distance to center of the city
    for rst in rsts_info:
        rst['center_dist'] = geo.distance(center_point,
                                          (rst['lng'], rst['lat']))
        rst['min_region_dist'] = rst['region_id'] = None

    sorted_rsts = sorted(rsts_info, key=lambda rest: rest['center_dist'])
    log.info('Step 2: sorted complete, farest dist is {}'.
             format(sorted_rsts[-1]['center_dist']))

    # 3. calculate each region's center point and radius
    regions = region_inner.query_regions(city_ids=[city_id],
                                         type_codes=[REGION_TYPE_CBD])
    regions_info = {r['id']:
                    {'area': region_area_to_polygons(r['area'], reverse=True)}
                    for r in regions}
    region_id_to_del = []
    for region_id, region in regions_info.iteritems():
        region['center'] = get_centerpoint_of_region(region['area'], only_one=True)
        region['radius'] = get_radius_of_region(region['center'], region['area'])
        # info['rst_ids'] = []
        region['rst_num'] = 0
        if not (region['center'] and region['radius']):
            region_id_to_del.append(region_id)
    for r_id in region_id_to_del:
        regions_info.__delitem__(r_id)
    log.info('Step 3: calculate center and radius')

    # 4. main loop for restaurants, there are three kinds of results
    #  for each restaurant:
    #       a. in certain region
    #       b. near certain region (no more than `max_distance_to_center`)
    #       c. others (drop into ungrouped region)
    for index, rst in enumerate(sorted_rsts):
        try:
            if index % 100 == 0:
                log.info('grouping rate {}%'.format(float(index) / rst_len * 100))

            rst_point = (rst['lng'], rst['lat'])
            final_region_id = None

            # a. if in certain region
            in_region_flag = False
            for region_id, region in regions_info.iteritems():
                if not region['area']:
                    continue
                polygons = region['area']
                for polygon in polygons:
                    if geo.is_in_region(rst_point, polygon, xy_reverse=True):
                        in_region_flag = True
                        if region['rst_num'] < max_region_rsts_num:
                            rst['region_id'] = region_id
                            region['rst_num'] += 1
                            rst_in_region_num += 1  # for logging
                        break

                if in_region_flag:
                    break

            if rst.get('region_id'):
                continue

            # b. if near some region
            min_dist = sys.maxint
            for region_id, region in regions_info.iteritems():
                current_dist = geo.distance(rst_point, region['center'])
                if current_dist < min_dist and \
                        region['rst_num'] < max_region_rsts_num:
                    min_dist = current_dist

                    if min_dist < max_distance_to_center + region['radius']:
                        rst['min_region_dist'] = min_dist
                        region['rst_num'] += 1
                        final_region_id = region_id
                        rst_near_region_num += 1  # for logging
                        break

            if not final_region_id:
                rst['region_id'] = None
                rst_far_from_region_num += 1  # for logging
        except Exception as e:
            exc_num += 1
            print(e)

    rst_total_num = len(sorted_rsts)
    average_rst_region_dist = 0
    rst_count = 0
    for rst in sorted_rsts:
        if rst['min_region_dist'] is not None:
            rst_count += 1
            average_rst_region_dist += rst['min_region_dist']
    average_rst_region_dist /= rst_count

    region_average_rst_num = 0
    region_rst_num_count = 0
    region_average_radius = 0
    region_radius_count = 0
    for region_id, region in regions_info.iteritems():
        if region['rst_num'] is not None:
            region_rst_num_count += 1
            region_average_rst_num += region['rst_num']
        if region['radius'] is not None:
            region_radius_count += 1
            region_average_radius += region['radius']
    region_average_rst_num /= region_rst_num_count
    region_average_radius /= region_radius_count

    log.info('Step 4: Main grouping. total_rst_num: {}, total_region_num: {}, '
             'rst_in_region: {}, rst_near_region: {}, other_rsts: {};'
             'ave rst region dist: {}, ave region rst num: {},'
             ' ave region radius {}. total exc {}.'.
             format(rst_total_num, len(regions_info), rst_in_region_num,
                    rst_near_region_num, rst_far_from_region_num,
                    average_rst_region_dist, region_average_rst_num,
                    region_average_radius, exc_num))

    # 5. update restaurant region
    for index, rst in enumerate(sorted_rsts):
        try:
            if index % 200 == 0:
                log.info('updating rate {}%'.format(float(index) / rst_len * 100))
            # log.info('update rst {} with region {}'.format(rst.id, region_id))
            # inner.update_restaurant_region(rst['id'], rst['region_id'])
            log.info('rst_id: {}, region_id: {}'.format(rst['id'], rst['region_id']))

        except Exception as e:
            exc_num += 1
            print(e)
    for region_id, region in regions_info.iteritems():
        log.info('{}: {}'.format(region_id, region['rst_num']))

    log.info('done.')
    return True


def drop_bod_invalid_rsts(city_id, sea_region_id):
    rsts = []
    rsts.extend(inner.query_all_rsts(city_ids=[city_id], is_valid=0))
    rsts.extend(inner.query_all_rsts(city_ids=[city_id], is_premium=1))
    log.info('total_num: {}'.format(len(rsts)))
    log.info('重复的：{}'.format(len(inner.query_all_rsts(city_ids=[city_id], is_premium=1, is_valid=0))))
    for rst in rsts:
        # inner.update_restaurant_region(rst['id'], sea_region_id)
        log.info('rst_id: {}, region_id: {}'.format(rst['id'], sea_region_id))
