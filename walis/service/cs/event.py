##!/usr/bin/env python2
# coding=utf8

from __future__ import absolute_import, division, print_function
from collections import defaultdict

from walis.exception.error_code import (
    CS_EVENT_NOT_EXIST,
    CS_EVENT_PROCESS_STATUS_INVALID,
    DEV_BAD_REQUEST_ERROR)
from walis.exception.util import (
    raise_dev_exc,
    raise_user_exc,
)
from walis.service.cs import inner
from walis.service.user import user as user_service
from walis.service.cs import user as cs_user_service
from walis.model.walis.cs import (
    CSEvent,
)
from walis.utils.time import datetime2str


##########
# Event
#####
def add_event(user_type, phone, priority, source, status, creater_id,
              user_id=None, user_info=None, order_id=None, compensation=None,
              content=None, category_l1=None, category_l2=None,
              category_l3=None):
    if user_id is None:
        user_id = cs_user_service.get_user_by_phone(phone).get('user_id', None)

    event_id = inner.add_event(
        user_id=user_id,
        user_type=user_type,
        user_info=user_info,
        phone=phone,
        priority=priority,
        source=source,
        status=status,
        creater_id=creater_id,
        handler_id=creater_id,
        order_id=order_id,
        compensation=compensation,
        category_l1=category_l1,
        category_l2=category_l2,
        category_l3=category_l3,
    )
    inner.add_record(event_id, creater_id, content, status)
    return event_id


def get_event(event_id, with_records=True, with_name=True):
    event = inner.get_event(event_id)

    if not event:
        raise_user_exc(CS_EVENT_NOT_EXIST, event_id=event_id)

    event = event.to_dict()
    if with_records:
        records = get_records(event['id'], with_name=with_name)
        event['records'] = records

    return event


def update_event(event_id, compensation=None, user_id=None, content=None):
    event = inner.get_event(event_id)

    if not event:
        raise_user_exc(CS_EVENT_NOT_EXIST, event_id=event_id)

    if compensation is not None:
        event.update(compensation=compensation)

    if user_id and content:
        inner.add_record(event_id, user_id, content, event.status)

    return True


def process_event(event_id, status, handler_id=None):
    if status is None:
        return False

    if status == CSEvent.STATUS_FORWARD and handler_id is None:
        raise_dev_exc(DEV_BAD_REQUEST_ERROR, arg='handler_id')

    event = inner.get_event(event_id)

    if not event:
        raise_user_exc(CS_EVENT_NOT_EXIST, event_id=event_id)

    if event.status == CSEvent.STATUS_DONE:
        raise_dev_exc(CS_EVENT_PROCESS_STATUS_INVALID, event_id=event_id,
                      status=event.status)

    event.update(status=status, handler_id=handler_id)
    return True


def query_events(status=None, category_l1=None, user_type=None, priority=None,
                 source=None, not_handler_id=None, handler_id=None,
                 is_to_compensate=None, begin_date=None, end_date=None, phone=None,
                 with_name=True, with_records=True, limit=None, offset=None):

    events = inner.query_events(status, category_l1, user_type, priority, source,
                                not_handler_id, handler_id, is_to_compensate,
                                begin_date, end_date, phone, limit, offset)
    if not events:
        return []

    results = [event.to_dict() for event in events]
    for result in results:
        result['created_at'] = datetime2str(result['created_at'])
        result['updated_at'] = datetime2str(result['updated_at'])

        if with_records:
            # TODO 如遇性能问题可调整为mget
            records = get_records(result['id'], with_name=with_name)
            result['records'] = records

        if with_name:
            # TODO 如遇性能问题可调整为mget
            if result.get('user_id'):
                result['user_name'] = user_service.get_user(
                    result['user_id']).username
            result['creater_name'] = user_service.get_user(
                result['creater_id']).username
            result['handler_name'] = user_service.get_user(
                result['handler_id']).username

    return results


def count_events(status=None, category_l1=None, user_type=None, priority=None,
                 source=None, not_handler_id=None, handler_id=None,
                 is_to_compensate=None, begin_date=None, end_date=None,
                 phone=None, **kwargs):

    count = inner.count_events(status, category_l1, user_type, priority,
                               source, not_handler_id, handler_id,
                               is_to_compensate, begin_date, end_date, phone)
    return count or 0


###############
# Event-Record
##########
def add_record(event_id, user_id, content, status=None):
    if not status:
        status = get_event(event_id)

    return inner.add_record(event_id, user_id, content, status)


def get_records(event_id, with_name=True):
    records = inner.get_records(event_id)
    for record in records:
        setattr(record, 'created_at', record.created_at)
        if with_name:
            setattr(record, 'user_name', user_service.get_user(
                record.user_id).username)

    return [r.to_dict() for r in records]


##########
# Category
#####
def get_category_trees(l1_id=None):
    categories = inner.query_category()

    if l1_id:
        l1s = filter(lambda c: c.id == l1_id, categories)
    else:
        l1s = filter(lambda c: c.parent_id is None, categories)
    l1_set = set([l.id for l in l1s])

    l2s = filter(lambda c: c.parent_id in l1_set, categories)
    l2_set = set([l.id for l in l2s])

    l3s = filter(lambda c: c.parent_id in l2_set, categories)

    l2_map = defaultdict(list)
    for l2 in l2s:
        l2_map[l2.parent_id].append(l2)

    l3_map = defaultdict(list)
    for l3 in l3s:
        l3_map[l3.parent_id].append(l3)

    result = []
    for l1 in l1s:
        tree_l1 = {'id': l1.id, 'parent_id': l1.parent_id, 'name': l1.name,
                   'is_valid': l1.is_valid, 'l2': []}

        for l2 in l2_map.get(l1.id, []):
            tree_l2 = {'id': l2.id, 'parent_id': l2.parent_id, 'name': l2.name,
                       'is_valid': l2.is_valid, 'l3': []}

            for l3 in l3_map.get(l2.id, []):
                tree_l3 = {'id': l3.id, 'parent_id': l3.parent_id,
                           'name': l3.name, 'is_valid': l3.is_valid}
                tree_l2['l3'].append(tree_l3)

            tree_l1['l2'].append(tree_l2)

        result.append(tree_l1)

    if l1_id and result:
        return result[0]

    return result


def update_categories(categories):
    l1_id = None

    for l1 in categories:
        l1_id = _save_category(category_id=l1.get('id'),
                               name=l1['name'],
                               is_valid=l1['is_valid'])
        l2s = l1.pop('l2', [])
        for l2 in l2s:
            l2_id = _save_category(category_id=l2.get('id'),
                                   name=l2['name'],
                                   parent_id=l1_id,
                                   is_valid=l2['is_valid'])
            l3s = l2.pop('l3', [])
            for l3 in l3s:
                _save_category(category_id=l3.get('id'),
                               name=l3['name'],
                               parent_id=l2_id,
                               is_valid=l3['is_valid'])
    return l1_id


def _save_category(category_id=None, name=None, parent_id=None, is_valid=None):
    """ Add or update.

    :return: category id
    """
    if category_id is not None:
        category = inner.get_category(category_id)

        if not category:
            return None

        inner.update_category(category_id, name, is_valid)
        return category_id

    return inner.add_category(name, parent_id, is_valid)
