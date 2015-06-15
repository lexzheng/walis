#!/usr/bin/env python2
# coding=utf8

from __future__ import absolute_import, division, print_function

from walis.model.walis import DBSession, db_commit
from walis.model.walis.cs import CSProcessTypeChangeRecord


@db_commit
def add_change_record(user_id, from_type, to_type):
    session = DBSession()
    new_record = CSProcessTypeChangeRecord(
        user_id=user_id,
        from_type=from_type,
        to_type=to_type
    )

    session.add(new_record)
    session.flush()
    return new_record.id
