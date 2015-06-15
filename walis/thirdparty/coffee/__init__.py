# coding=utf8

from __future__ import absolute_import, division, print_function
from walis import config
from bluelake.client.sdk import BluelakeSDK
from walis.config import COFFEE_SERVICE
# from .sso import ISessionService

OUT_SYSTEM = {'principal': {
    "type": "out_system",
    "identification": "",
    "token": "",
}}


class Coffee(object):

    def __init__(self):
        self.server = config.COFFEE_SERVICE['server']
        self._service = {}

    @property
    def sso(self):
        if self._service.get('sso'):
            return self._service['sso']

        self._service['sso'] = BluelakeSDK('sessionService', self.server, sender='requests')
        # self._service['sso'] = ISessionService(self.server)
        return self._service['sso']

    @property
    def rst_manage_rst(self):
        if self._service.get('rst_manage_rst'):
            return self._service['rst_manage_rst']

        self._service['rst_manage_rst'] = BluelakeSDK('rstManageRstService',
                                                      COFFEE_SERVICE['bpm_mkt_utp'],
                                                      sender='requests')
        return self._service['rst_manage_rst']

    @property
    def hr_permission(self):
        if self._service.get('hr_permission'):
            return self._service['hr_permission']

        self._service['hr_permission'] = BluelakeSDK('permissionService',
                                                     self.server,
                                                     sender='requests')
        return self._service['hr_permission']

    @property
    def city_manage(self):
        if self._service.get('city_manage'):
            return self._service['city_manage']

        self._service['city_manage'] = BluelakeSDK('cityManageService',
                                                   COFFEE_SERVICE['bpm_mkt_utp'],
                                                   sender='requests')
        return self._service['city_manage']


# Usage: coffee.sso.checkToken('sdfsdfsdfsdf')
coffee = Coffee()
