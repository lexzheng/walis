#!/usr/bin/env python2
# coding=utf8

""" CS: Customer Service
"""

from __future__ import absolute_import, division, print_function
from walis.api.base import BaseApi
from walis.core.api import api
from .handler.cs import (
    user,
    event,
)


class CSEventApi(BaseApi):

    route_base = 'cs/event'

    def gets(self):
        return event.query_events()

    def get(self, event_id):
        return event.get_event(int(event_id))

    def put(self, event_id):
        return event.update_event(int(event_id))

    def post(self):
        return event.add_event()

    @api('/<int:event_id>/process', methods=['PUT'])
    def process(self, event_id):
        return event.process_event(event_id)


class CSEventCategoryApi(BaseApi):

    route_base = 'cs/event/category'

    def gets(self):
        return event.get_category_trees()

    def put(self):
        return event.update_category_tree()


class CSUser(BaseApi):

    route_base = 'cs/user'

    def get(self):
        return user.get_user_by_phone()
