#!/usr/bin/env python2
# -*- coding: utf8 -*-

from walis.core.api import api
from walis.api.handler.user import user as user_handler, \
    hongbao as hongbao_handler

from .base import BaseApi


class UserApi(BaseApi):
    route_base = 'user'

    # user
    @api('/current', methods=['GET', ])
    def current(self):
        return user_handler.current()

    @api('/username_available')
    def is_username_available(self):
        return user_handler.is_username_available()

    @api('/mobile_ref_user')
    def get_user_by_mobile(self):
        return user_handler.get_user_by_mobile()

    # hongbao
    @api('/hongbao')
    def gets_hongbao(self):
        return hongbao_handler.gets_hongbao()

    @api('/hongbao_exchange')
    def gets_hongbao_exchange(self):
        return hongbao_handler.gets_hongbao_exchange()

    @api('/hongbao_share')
    def gets_hongbao_share(self):
        return hongbao_handler.gets_hongbao_share()

    @api('/hongbao_grab')
    def gets_hongbao_grab(self):
        return hongbao_handler.gets_hongbao_grab()

    @api('/hongbao/<hongbao_sn>', methods=['DELETE',])
    def delete(self, hongbao_sn):
        return hongbao_handler.delete(hongbao_sn)

    @api('/<int:user_id>/hongbao')
    def gets_by_userid(self, user_id):
        return hongbao_handler.gets_by_userid(user_id)

