#!/usr/bin/env python2
# coding=utf8

from __future__ import absolute_import, division, print_function
from sqlalchemy import func
from walis.model.walis import DBSession
from walis.model.walis.cs import CSEvent
from walis.utils.model import make_query
from walis.utils.time import datestr2datetime


def query_events(status=None, category_l1=None, user_type=None, priority=None,
                 source=None, not_handler_id=None, handler_id=None,
                 is_to_compensate=None, begin_date=None, end_date=None, phone=None,
                 limit=None, offset=None):
    q = DBSession().query(CSEvent).order_by(CSEvent.updated_at.desc())

    if begin_date is not None:
        q = q.filter(CSEvent.created_at >= datestr2datetime(begin_date))

    if end_date is not None:
        q = q.filter(CSEvent.created_at <= datestr2datetime(end_date))

    if not_handler_id is not None:
        q = q.filter(CSEvent.handler_id != not_handler_id)

    if is_to_compensate is not None:
        if is_to_compensate:
            q = q.filter(CSEvent.compensation > 0)
        else:
            q = q.filter(CSEvent.compensation == 0)

    return make_query(q, CSEvent,
                      {'phone': phone, 'handler_id': handler_id, 'status': status,
                       'category_l1': category_l1, 'user_type': user_type,
                       'priority': priority, 'source': source, 'limit': limit,
                       'offset': offset})


def count_events(status=None, category_l1=None, user_type=None, priority=None,
                 source=None, not_handler_id=None, handler_id=None,
                 is_to_compensate=None, begin_date=None, end_date=None, phone=None):
    q = DBSession().query(func.count(CSEvent.id))

    if begin_date is not None:
        q = q.filter(CSEvent.created_at >= datestr2datetime(begin_date))

    if end_date is not None:
        q = q.filter(CSEvent.created_at <= datestr2datetime(end_date))

    if not_handler_id is not None:
        q = q.filter(CSEvent.handler_id != not_handler_id)

    if is_to_compensate is not None:
        if is_to_compensate:
            q = q.filter(CSEvent.compensation > 0)
        else:
            q = q.filter(CSEvent.compensation == 0)

    return make_query(q, CSEvent,
                      {'phone': phone, 'handler_id': handler_id, 'status': status,
                       'category_l1': category_l1, 'user_type': user_type,
                       'priority': priority, 'source': source}).scalar()
