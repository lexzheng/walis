# coding=utf8
#!/usr/bin/env python

from __future__ import division, print_function

import json

from flask import request
from flask.ext.login import UserMixin


# from zeus.eus
from walis.thirdparty import thrift_client
from walis.thirdparty.coffee import coffee

APP_INTRA_WALLE_JAVIS = 301


class UserZeusMixin(object):

    @classmethod
    def get_walle_id_by_sso_token(cls, sso_token):
        # with thrift_client('eus') as eus_client:
        #     useragent = request.headers.get('User-Agent', '')
        #     info_raw = {
        #         'useragent': useragent,
        #     }
        #     info_raw = json.dumps(info_raw)
        #     ip_addr = get_real_remote_addr()
        #     user_id = eus_client.sso_check(
        #         sso_id, APP_INTRA_WALLE_JAVIS, info_raw, ip_addr)
        #     return user_id
        sso_info = coffee.sso.checkToken(access_token=sso_token)
        return sso_info['user']['walle_id']

    @classmethod
    def get_sso_user_id_by_sso_token(cls, sso_token):
        sso_info = coffee.sso.checkToken(access_token=sso_token)
        return sso_info['user']['id']

    @classmethod
    def get_user(cls, sso_token):
        if not sso_token:
            return None

        user_id = cls.get_walle_id_by_sso_token(sso_token)
        sso_id = cls.get_sso_user_id_by_sso_token(sso_token)
        if user_id:
            user = cls(user_id)
            user.sso_token = sso_token
            user.sso_id = sso_id
            user.auth_context['principal']['token'] = sso_token
            return user

    def is_super_admin(self):
        with thrift_client('eus') as eus:
            user = eus.get(self.id)
            return user.is_super_admin

    def get(self):
        with thrift_client('eus') as eus:
            return eus.get(self.id)

    def has_permissions(self, permissions, is_strict):
        with thrift_client('eus') as eus_client:
            return eus_client.has_permissions(self.id, permissions, is_strict)

    def get_permissions(self):
        with thrift_client('eus') as eus_client:
            return eus_client.get_user_permission(self.id)

    def has_groups(self, groups, is_strict=False):
        if not groups:
            return True

        if self.is_super_admin():
            return True

        if is_strict:
            return list(set(groups) - set(self.user_groups)) == []
        else:
            return list(set(groups) & set(self.user_groups)) != []

    def get_groups(self):
        with thrift_client('eus') as eus:
            return [group.name for group in eus.query_user_group(self.id)]

    def get_restaurant_ids_in_charge(self):
        # if super admin
        if self.is_super_admin():
            return None

        with thrift_client('ers') as ers:
            user_struct = ers.get_direct_struct(self.id)

        # if city.admin
        if user_struct.city_ids:
            return None

        region_ids = []
        # if region_group.admin
        if user_struct.region_group_ids:
            with thrift_client('ers') as ers:
                regions = ers.get_regions_by_region_group_ids(
                    user_struct.region_group_ids)
            region_ids = [region.id for region in regions]

        # if region.admin
        if user_struct.region_ids:
            region_ids.extend(user_struct.region_ids)
            region_ids = list(set(region_ids))

        with thrift_client('ers') as ers:
            restaurant_ids = ers.mget_restaurant_in_region(region_ids, True)

        return restaurant_ids

    def get_user_struct(self):
        if self._user_struct is None:
            with thrift_client('ers') as ers:
                self._user_struct = ers.get_direct_struct(self.id)

        region_ids = []
        if self._user_struct.region_group_ids:
            with thrift_client('ers') as ers:
                regions = ers.get_regions_by_region_group_ids(
                    self._user_struct.region_group_ids)
            region_ids = [region.id for region in regions]
        if region_ids:
            self._user_struct.region_ids.extend(region_ids)
        return self._user_struct

    def get_all_city_ids(self):
        if self._all_city_ids is None:
            if self._user_struct is None:
                self._user_struct = self.get_user_struct()
                # if city.admin
            user_city_ids = self._user_struct.city_ids
            if user_city_ids:
                self._all_city_ids = user_city_ids
                return user_city_ids
            # if region_group.admin
            if self._user_struct.region_group_ids:
                with thrift_client('ers') as ers:
                    region_groups = ers.mget_region_group(self._user_struct.region_group_ids)
                user_city_ids = list(set([region_group.city_id
                                          for region_group in region_groups]))
            # if region.admin
            if self._user_struct.region_ids:
                with thrift_client('ers') as ers:
                    regions = ers.mget_region(self._user_struct.region_ids)

                user_city_ids_by_region = [v.city_id for k,v in regions.iteritems()]
                user_city_ids = list(set(user_city_ids_by_region + user_city_ids))

            if user_city_ids:
                self._all_city_ids = user_city_ids
                return user_city_ids
        return self._all_city_ids


class WalisUser(UserMixin, UserZeusMixin):
    def __init__(self, id):
        self.id = id
        self.sso_token = None
        self.sso_id = None

        self._user_groups = None
        # get user name
        self._name = ''
        # get city ids
        self.cities = []
        # specially for market director
        self._restaurant_ids = None
        # get user struct
        self._user_struct = None
        # get all city ids
        self._all_city_ids = None
        # get user
        self._user = None
        self._utp_restaurant_ids = None
        self._utp_city_ids = None
        self.auth_context = {
            'principal': {
                'type': 'user_type',
                'identification': '',
                'token': ''
            }
        }

    @property
    def city_ids(self):
        if self._user_struct is None:
            self._user_struct = self.get_user_struct()
        return self._user_struct.city_ids

    @property
    def region_group_ids(self):
        if self._user_struct is None:
            self._user_struct = self.get_user_struct()
        return self._user_struct.region_group_ids

    @property
    def region_ids(self):
        if self._user_struct is None:
            self._user_struct = self.get_user_struct()
        return self._user_struct.region_ids

    # TODO
    @property
    def all_city_ids(self):
        if self._all_city_ids is None:
            self._all_city_ids = self.get_all_city_ids()
        return self._all_city_ids

    @property
    def user_groups(self):
        """ User's permission groups
        """
        if self._user_groups is None:
            self._user_groups = self.get_groups()
        return self._user_groups

    @property
    def restaurant_ids(self):
        """ User's restaurant ids in charge
        if SuperAdmin or CityDirector, return None
        if RegionGroup Market Director or Region Market Director, return ids

        """
        if self._restaurant_ids is None:
            self._restaurant_ids = self.get_restaurant_ids_in_charge()
        return self._restaurant_ids

    @property
    def name(self):
        """ User's account name
        """
        if self._user is None:
            self._user = self.get()
        return self._user.username

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    def get_auth_token(self):
        sso_token = request.cookies.get('SSO_TOKEN', None)
        return sso_token

    def utp_is_restaurant_owner(self,restaurant_id):
        res=coffee.rst_manage_rst.isRstOwner(context=self.auth_context,userId=self.sso_id,rstId=restaurant_id)
        return res

    @property
    def utp_restaurant_ids(self):
        if self._utp_restaurant_ids is None:
            self._utp_restaurant_ids = coffee.rst_manage_rst.searchRstUnderUser(context=self.auth_context)
        return self._utp_restaurant_ids

    @property
    def utp_city_ids(self):
        if self._utp_city_ids is None:
            self._utp_city_ids = coffee.city_manage.searchCitiesUnderUser(context=self.auth_context)
        return self._utp_city_ids
