#!/usr/bin/env python2
# coding=utf8

from __future__ import absolute_import, division, print_function
import json

from webargs import Arg
from flask.ext.login import current_user
from walis.exception import UserExc

from walis.service.cs import event as event_service
from walis.utils.http import args_parser
from walis.utils.paging import get_paging_params


##########
# Event
#####
def get_event(event_id):
    args = args_parser.parse({
        'with_name': Arg(bool, allow_missing=True),
        'with_records': Arg(bool, allow_missing=True),
    })
    event = event_service.get_event(event_id, **args)
    _format_event(event)
    return event


def update_event(event_id):
    args = args_parser.parse({
        'compensation': Arg(int),
        'content': Arg(unicode),
        'status': Arg(int, required=True),
    })

    status = args.pop('status', None)
    if status is not None:
        event_service.process_event(event_id, status, current_user.id)

    if args.get('compensation') is not None:
        event_service.update_event(event_id, user_id=current_user.id, **args)


def process_event(event_id):
    args = args_parser.parse({
        'status': Arg(int, required=True),
        'handler_id': Arg(int, allow_missing=True)
    })
    event_service.process_event(event_id, **args)


def add_event():
    args = args_parser.parse({
        'user_id': Arg(int),
        'user_type': Arg(int, required=True),
        'user_info': Arg(unicode),
        'phone': Arg(str, required=True),
        'priority': Arg(int, required=True),
        'source': Arg(int, required=True),
        'order_id': Arg(long),
        'compensation': Arg(int),
        'category_l1': Arg(int),
        'category_l2': Arg(int),
        'category_l3': Arg(int),
        'status': Arg(int),
        'content': Arg(unicode, required=True),
    })
    args['creater_id'] = current_user.id
    event_id = event_service.add_event(**args)
    return {'id': event_id}


def query_events():
    args = args_parser.parse({
        'id': Arg(int),
        'status': Arg(int),
        'category_l1': Arg(int),
        'user_type': Arg(int),
        'priority': Arg(int),
        'source': Arg(int),
        'is_my_event': Arg(int, allow_missing=True),
        'is_to_compensate': Arg(int, allow_missing=True),
        'begin_date': Arg(str),
        'end_date': Arg(str),
        'phone': Arg(str),
        'with_name': Arg(int, allow_missing=True),
        'with_records': Arg(int, allow_missing=True),
    })
    event_id = args.pop('id', None)
    if event_id is not None:
        events = []
        try:
            event = event_service.get_event(event_id)
        except UserExc:
            event = None

        if event:
            events.append(event)
        return {
            'events': events,
            'count': len(events)
        }

    offset, limit = get_paging_params(db_style=True)
    args.update({'offset': offset, 'limit': limit})

    is_my_event = args.pop('is_my_event', None)
    if is_my_event is not None:
        if is_my_event:
            args.update(handler_id=current_user.id)
        else:
            args.update(not_handler_id=current_user.id)

    events = event_service.query_events(**args)
    count = event_service.count_events(**args)
    _format_event(events)
    return {
        'events': events,
        'count': count
    }


##########
# Category
#####
def get_category_trees():
    args = args_parser.parse({
        'category_l1': Arg(int),
    })
    return event_service.get_category_trees(args.get('category_l1'))


def update_categories():
    categories_json = args_parser.parse({
        'categories': Arg(required=True),
    })['categories']
    categories = json.loads(categories_json)
    return event_service.update_categories(categories)


def update_category_tree():
    categories = args_parser.parse({
        'categories': Arg(required=True),
    })['categories']
    category_l1_id = event_service.update_categories(categories)
    return {'id': category_l1_id}


def _format_event(event_or_events):
    """ format 'order_id' to string

    :param event_or_events:
    :return:
    """
    if isinstance(event_or_events, list):
        for event in event_or_events:
            _format_event(event)
    elif isinstance(event_or_events, dict):
        if event_or_events.get('order_id'):
            event_or_events.__setitem__(
                'order_id', str(event_or_events['order_id']))
    return event_or_events
