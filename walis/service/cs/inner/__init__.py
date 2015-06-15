##!/usr/bin/env python2
# coding=utf8

from __future__ import absolute_import, division, print_function
from walis.model.walis import (
    db_commit,
)
from walis.model.walis.cs import (
    CSEventRecord,
    CSEventCategory,
)
from .query import *


##########
# Event
#####
@db_commit
def add_event(user_id, user_type, phone, priority, source, status, creater_id,
              handler_id, user_info=None, order_id=None, compensation=None,
              category_l1=None, category_l2=None, category_l3=None):
    session = DBSession()
    new_event = CSEvent(
        user_id=user_id,
        user_type=user_type,
        user_info=user_info,
        phone=phone,
        priority=priority,
        source=source,
        status=status,
        creater_id=creater_id,
        handler_id=handler_id,
        order_id=order_id,
        compensation=compensation,
        category_l1=category_l1,
        category_l2=category_l2,
        category_l3=category_l3,
    )

    session.add(new_event)
    session.flush()
    return new_event.id


def get_event(event_id):
    return DBSession().query(CSEvent).get(event_id)


###############
# Event-Record
##########
@db_commit
def add_record(event_id, user_id, content, status):
    session = DBSession()
    new_record = CSEventRecord(
        event_id=event_id,
        user_id=user_id,
        content=content,
        status=status,
    )
    session.add(new_record)
    session.flush()
    return new_record.id


def get_records(event_id):
    return DBSession().query(CSEventRecord).\
        filter(CSEventRecord.event_id == event_id).\
        order_by(CSEventRecord.created_at.desc())


def get_last_records(event_id):
    return DBSession().query(CSEventRecord).\
        filter(CSEventRecord.event_id == event_id).\
        order_by(CSEventRecord.id.desc()).first()


##########
# Category
#####
def get_category(category_id):
    return DBSession().query(CSEventCategory).get(category_id)


def query_category(ids=None, is_valid=None):
    q = DBSession().query(CSEventCategory)

    if ids is not None:
        q.filter(CSEventCategory.id.in_(ids))

    if is_valid is not None:
        q.filter(CSEventCategory.is_valid == is_valid)

    return q


@db_commit
def add_category(name, parent_id=None, is_valid=True):
    session = DBSession()
    new_category = CSEventCategory(
        parent_id=parent_id,
        name=name,
        is_valid=is_valid,
    )
    session.add(new_category)
    session.flush()
    return new_category.id


@db_commit
def update_category(category_id, new_name=None, is_valid=None):
    category = DBSession().query(CSEventCategory).get(category_id)

    if not category:
        return None

    return category.update(new_name, is_valid)


@db_commit
def update_categories(categories):
    if not categories:
        return True

    update_map = {c['id']: c for c in categories}
    db_categories = query_category(ids=update_map.keys())

    for category in db_categories:
        category.update(
            new_name=update_map[category.id]['name'],
            is_valid=update_map[category.id]['is_valid']
        )
    return True
