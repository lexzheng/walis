#!/usr/bin/env python2
# coding=utf8

from __future__ import absolute_import, division, print_function

# enum BannerType {
#   NON_INTERACTIVE = 1,
#   LINK = 2,
#   ACTIVITY = 3,
# }
from walis.thirdparty import thrift_client, thirdparty_svc
from walis.utils.thrift import dict2ttype

banner_type = thirdparty_svc.keeper.BannerType()
RestaurantType = thirdparty_svc.keeper.RestaurantType
NonInteractiveBanner = thirdparty_svc.keeper.NonInteractiveBanner
LinkBanner = thirdparty_svc.keeper.LinkBanner
ActivityBanner = thirdparty_svc.keeper.ActivityBanner
BannerQuery = thirdparty_svc.keeper.BannerQuery


NON_INTERACTIVE_BANNER_ATTRIBUTES = [
    'name',
    'is_valid',
    'image_hash',
    'priority',
    'start_date',
    'end_date',
    'weekdays',
    'regions',
]

LINK_BANNER_ATTRIBUTES = NON_INTERACTIVE_BANNER_ATTRIBUTES + [
    'url',
]

ACTIVITY_BANNER_ATTRIBUTES = NON_INTERACTIVE_BANNER_ATTRIBUTES + [
    'restaurant_type',
    'activity_id',
    'activity_name',
    'activity_category_id',
    'activity_image_hash',
    'description',
    'time_desc',
    'rule_desc',
    'region_desc',
    'tip'
]


def _create_banner(b_type, args):
    if b_type == banner_type.NON_INTERACTIVE:
        return dict2ttype(args,
                          NonInteractiveBanner(),
                          NON_INTERACTIVE_BANNER_ATTRIBUTES)

    if b_type == banner_type.LINK:
        return dict2ttype(args,
                          LinkBanner(),
                          LINK_BANNER_ATTRIBUTES)

    if b_type == banner_type.ACTIVITY:
        return dict2ttype(args,
                          ActivityBanner(),
                          ACTIVITY_BANNER_ATTRIBUTES)


def get(id):
    with thrift_client('keeper') as keeper:
        return keeper.get_banner(id)


def add_non_interactive_banner(args):
    banner = _create_banner(banner_type.NON_INTERACTIVE, args)
    with thrift_client('keeper') as keeper:
        db_banner = keeper.add_non_interactive_banner(banner)

    return db_banner.id


def add_link_banner(args):
    banner = _create_banner(banner_type.LINK, args)
    with thrift_client('keeper') as keeper:
        db_banner = keeper.add_link_banner(banner)

    return db_banner.id


def add_activity_banner(args):
    banner = _create_banner(banner_type.ACTIVITY, args)
    with thrift_client('keeper') as keeper:
        db_banner = keeper.add_activity_banner(banner)

    return db_banner.id


def update_non_interactive_banner(args):
    banner = _create_banner(banner_type.NON_INTERACTIVE, args)
    with thrift_client('keeper') as keeper:
        keeper.update_non_interactive_banner(args['id'], banner)


def update_link_banner(args):
    banner = _create_banner(banner_type.LINK, args)
    with thrift_client('keeper') as keeper:
        keeper.update_link_banner(args['id'], banner)


def update_activity_banner(args):
    banner = _create_banner(banner_type.ACTIVITY, args)
    with thrift_client('keeper') as keeper:
        keeper.update_activity_banner(args['id'], banner)


def query(args):
    query_struct = dict2ttype(args, BannerQuery())
    query_struct.order_by = ['-created_at', ]
    with thrift_client('keeper') as keeper:
        results = keeper.javis_query_banners(query_struct)
    return results.banners, results.count
