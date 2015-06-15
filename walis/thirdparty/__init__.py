#!/usr/bin/env python2
# coding=utf8

from __future__ import absolute_import, division, print_function
import thriftpy
from thriftpy.rpc import client_context
from walis import config

from walis.exception.util import raise_dev_exc
from walis.exception.error_code import DEV_THRIFT_ERR

class ThirdPartyService(object):

    def __init__(self):
        """ thrift service dict
        """
        self._services = {}
        for svc in config.THRIFT_SERVICE.keys():
            self._services[svc] = None

    def __getattr__(self, name):
        if name not in self._services.keys():
            raise_dev_exc(DEV_THRIFT_ERR, thrift_name=name)

        if not self._services.get(name):
            self._services[name] = _load_service(name)

        return self._services[name]

    def thrift_client(self, service_name):
        if not self._services.get(service_name):
            self._services[service_name] = _load_service(service_name)

        return client_context(
            self._services[service_name].t_service,
            config.THRIFT_SERVICE[service_name]['host'],
            config.THRIFT_SERVICE[service_name]['port']
        )


def _load_service(service_name):
    thrift_module = thriftpy.load_module(
        'walis.thirdparty.thrift.{}_thrift'.format(service_name))

    for key, value in thrift_module.__dict__.items():
        if key.lower().endswith('service'):
            thrift_module.t_service = value

    return thrift_module


thirdparty_svc = ThirdPartyService()
thrift_client = thirdparty_svc.thrift_client