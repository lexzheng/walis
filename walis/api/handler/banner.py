#!/usr/bin/env python2
# coding=utf8

from __future__ import absolute_import, division, print_function

from walis.utils.time import strptime_to_date
import datetime

from flask import request
from flask.ext.login import current_user
from webargs import Arg

from walis.api.handler import BaseHandler
from walis.service.activity import rst_activity as rst_act_base
from walis.service.activity.utils import RestaurantActivityMixin
from walis.utils.http import args_parser
from walis.utils.model import obj_hash2url
from walis.utils.paging import paging
from walis.service import (
    banner as banner_client,
)
from walis.service.region import (
    city as city_base,
    region_group as rg_base,
    region as region_base,
)
from walis.service.activity import (
    food_activity as food_act_base,
)
from walis.utils.thrift import ttype2dict
from walis.utils.time import get_today_date_str

from walis.exception.util import raise_user_exc
from walis.exception.error_code import (
    BANNER_NOT_EXISTS_ERR,
    BANNER_TYPE_ERR,
    BANNER_ARGS_ERR
)


def get_args():
    args_spec = {
        'id': Arg(int, allow_missing=True),
        'name': Arg(unicode),
        'type': Arg(int),
        'is_valid': Arg(int),
        'image_hash': Arg(str),
        'priority': Arg(int),
        'start_date': Arg(str, allow_missing=True),
        'end_date': Arg(str, allow_missing=True),
        # TODO check
        'weekdays': Arg([], allow_missing=True),
        'cities': Arg([]),
        'region_groups': Arg([]),
        'regions': Arg([]),
        'url': Arg(str, allow_missing=True),
        'restaurant_type': Arg(int, allow_missing=True),
        'activity_id': Arg(int, allow_missing=True),
        'activity_category_id': Arg(int, allow_missing=True),
        'activity_name': Arg(unicode, allow_missing=True),
        'activity_image_hash': Arg(str, allow_missing=True),
        'description': Arg(unicode, allow_missing=True),
        'region_desc': Arg(unicode, allow_missing=True),
        'time_desc': Arg(unicode, allow_missing=True),
        'rule_desc': Arg(unicode, allow_missing=True),
        'tip': Arg(unicode, allow_missing=True),
    }
    args = args_parser.parse(args_spec)

    json = request.json
    try:
        activity_id = json['activity_id']
    except KeyError:
        pass
    else:
        if activity_id is None:
            args['activity_id'] = None
            args['activity_category_id'] = None
            args['activity_name'] = None
            args['restaurant_type'] = None

    return args


class BannerHandler(BaseHandler):

    @classmethod
    def get(cls, id):
        banner = banner_client.get(id)

        # assemble file url
        obj_hash2url(banner, 'image_hash', set_null=False)
        obj_hash2url(banner, 'activity_image_hash', set_null=False)

        cities, region_groups, regions = cls._region_map2list(banner.regions)
        setattr(banner, 'cities', cities)
        setattr(banner, 'region_groups', region_groups)
        setattr(banner, 'regions', regions)
        setattr(banner, 'modify_enabled', cls._get_modify_permission(id))

        return banner

    @classmethod
    def gets(cls):
        args_spec = {
            'city_id': Arg(int, allow_missing=True),
            'name': Arg(str, allow_missing=True),
            'is_valid': Arg(bool, allow_missing=True),
            'is_expire': Arg(int, allow_missing=True),
        }
        args = args_parser.parse(args_spec)

        is_expire=args.pop('is_expire',2)

        city_id = args.pop('city_id', None)
        if city_id:
            args['regions'] = {city_id: {}}

        banners, total_num = banner_client.query(args)
        newbanners=[]
        if is_expire!=2:
            today=datetime.date.today()
            for banner in banners:
                end_date=strptime_to_date(banner.end_date)
                if end_date=='':
                    newbanners.append(banner)
                elif is_expire==1 and end_date<today:
                    newbanners.append(banner)
                elif is_expire==0 and end_date>today:
                    newbanners.append(banner)
                else:
                    pass
        else:
            newbanners=banners
        total_num=len(newbanners)
        banners = paging(newbanners)
        return {
            'banners': banners,
            'total_num': total_num
        }

    @classmethod
    def put(cls, id):
        args = get_args()
        args.update({'id': int(id)})
        cls.update(args)

    @classmethod
    def update(cls, args):
        """ Update banner
        """
        banner = banner_client.get(args['id'])
        banner_dict = ttype2dict(banner)
        banner_dict.update(args)

        #is_valid is int,but update is ok

        if banner_dict.get('cities') \
                or banner_dict.get('region_groups'):
                # or banner_dict.get('regions'): TODO name conflict with keeper
            regions = cls._region_list2map(banner_dict.pop('cities'),
                                            banner_dict.pop('region_groups'),
                                            banner_dict.pop('regions'))
            banner_dict['regions'] = regions

        b_type = banner.type
        if b_type == banner_client.banner_type.NON_INTERACTIVE:
            banner_client.update_non_interactive_banner(banner_dict)
        if b_type == banner_client.banner_type.LINK:
            banner_client.update_link_banner(banner_dict)
        if b_type == banner_client.banner_type.ACTIVITY:
            banner_client.update_activity_banner(banner_dict)

        return ''

    @classmethod
    def post(cls):
        args = get_args()
        regions = cls._region_list2map(args.pop('cities'),
                                        args.pop('region_groups'),
                                        args.pop('regions'))
        args['regions'] = regions

        b_type = args.pop('type')
        if b_type == banner_client.banner_type.NON_INTERACTIVE:
            banner_id = banner_client.add_non_interactive_banner(args)
        elif b_type == banner_client.banner_type.LINK:
            banner_id = banner_client.add_link_banner(args)
        elif b_type == banner_client.banner_type.ACTIVITY:
            banner_id = banner_client.add_activity_banner(args)
        else:
            # TODO
            raise_user_exc(BANNER_TYPE_ERR)
        return {'id': banner_id}

    @classmethod
    def set_valid(cls):
        """ 设置banner是否有效
        """
        args_spec = {
            'id': Arg(int),
            'is_valid': Arg(int),
        }
        args = args_parser.parse(args_spec)

        if not len(args.values()) == 2 or args.get('is_valid') is None:
            # TODO raise incorrect args exception
            raise_user_exc(BANNER_ARGS_ERR)

        cls.update(args)
        return ''

    @classmethod
    def get_region_struct(cls):
        """ get City->RegionGroup->Region struct

        :return:
         [{'city_id': <city_id>,
           'city_name': <city_name>,
           'region_groups': {'region_group_id': <>,
                             'region_group_name': <>,
                             'regions': {'region_id': <>,
                                         'region_name': <>,
                                         'region_type': <>,
                                         }
                             }
          }
           ... ...
         ]
        """
        city_pairs = city_base.get_city_id_name_pairs(
            cls.get_user_city_ids())

        city_region_group_map = rg_base.\
            get_city_region_group_map(city_pairs.keys())

        region_ids = [r.id for r in region_base.get_all()]
        region_group_region_map = \
            region_base.get_region_group_region_map(region_ids)

        region_struct = []
        for city_id, city_name in city_pairs.items():
            region_groups = []

            for r_group in city_region_group_map.get(city_id, []):
                regions = []

                for region in region_group_region_map.get(r_group.id, []):
                    regions.append({'region_id': region.id,
                                    'region_name': region.name,
                                    'region_type': region.type_code})

                region_groups.append({'region_group_id': r_group.id,
                                      'region_group_name': r_group.name,
                                      'regions': regions})

            region_struct.append({'city_id': city_id,
                                  'city_name': city_name,
                                  'region_groups': region_groups})
        return region_struct

    @classmethod
    def get_activities(cls):
        args_spec = {
            'city_ids': Arg(int, multiple=True, allow_missing=True),
        }
        city_ids = args_parser.parse(args_spec).get('city_ids', [])
        if not city_ids:
            city_ids = cls.get_user_city_ids()

        today = get_today_date_str()
        rest_activities = rst_act_base.query(
            begin_date=today, end_date=today, city_ids=city_ids, is_valid=True)

        food_activities = food_act_base.query(
            begin_date=today, end_date=today, city_ids=city_ids, is_valid=True)

        rest_act_result = []
        for act in rest_activities:
            rest_act_result.append({
                'activity_id': act.id,
                'activity_name': RestaurantActivityMixin.get_name(act)
            })
        food_act_result = []
        for act in food_activities:
            food_act_result.append({
                'activity_id': act.id,
                'activity_name': act.name
            })

        return {
            'food_activities': food_act_result,
            'rest_activities': rest_act_result
        }

    @classmethod
    def get_user_city_ids(cls):

        if current_user.has_groups(['activity_manager', 'marketing_manager']):
            return {city.id: city.name for city in
                    city_base.get_all_cities()}

        elif current_user.has_groups(['city_director']):
            return city_base.get_city_id_name_pairs_by_user()

        return []

    @classmethod
    def _get_modify_permission(cls, banner_id):
        banner = banner_client.get(banner_id)
        if not banner:
            raise_user_exc(BANNER_NOT_EXISTS_ERR, banner_id=banner_id)

        banner_regions = banner.regions
        if not banner_regions or not banner_regions.keys():
            return True

        banner_city_ids = banner_regions.keys()

        if current_user.has_groups(['activity_manager', 'marketing_manager']):
            return True
        elif current_user.has_groups(['city_director']):
            user_city_ids = city_base.get_city_ids_by_user()
            return all([banner_city_id in user_city_ids
                        for banner_city_id in banner_city_ids])

        return False

    @classmethod
    def _region_map2list(cls, region_struct):
        if not region_struct:
            return [], [], []

        # get ids
        city_ids = region_struct.keys()
        region_group_ids = reduce(lambda l1, l2: l1 + l2,
                                  [x.keys() for x in region_struct.values()])
        region_ids = []
        for r_ids_list in region_struct.values():
            for r_ids in r_ids_list.values():
                region_ids.extend(r_ids)

        # get names
        cities = city_base.mget(city_ids)
        region_groups = rg_base.mget(region_group_ids)
        regions = region_base.mget(region_ids)

        return [{'city_id': city.id, 'city_name': city.name}
                for city in cities],\
               [{'region_group_id': rg.id, 'region_group_name': rg.name}
                for rg in region_groups],\
               [{'region_id': region.id, 'region_name': region.name}
                for region in regions]

    @classmethod
    def _region_list2map(cls, cities, region_groups, regions):
        city_ids = region_group_ids = region_ids = []
        if cities:
            city_ids = [int(city['city_id']) for city in cities]
        if region_groups:
            region_group_ids = [int(rg['region_group_id']) for rg in region_groups]
        if regions:
            region_ids = [int(region['region_id']) for region in regions]

        city_region_group_map = rg_base. \
            get_city_region_group_map_by_rg(region_group_ids)

        region_group_region_map = region_base. \
            get_region_group_region_map(region_ids)

        region_struct = {}
        for city_id in city_ids:
            r_g_map = {}

            for r_g_id in city_region_group_map.get(city_id, []):
                region_list = region_group_region_map.get(r_g_id, [])
                r_g_map[r_g_id] = [region.id for region in region_list]

            region_struct[city_id] = r_g_map

        return region_struct
