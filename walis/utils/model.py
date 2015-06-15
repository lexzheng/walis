#!/usr/bin/env python2
# coding=utf8

from __future__ import absolute_import, division, print_function
import copy
import datetime
import decimal

from walis.utils.time import datetime2utc
from walis.service.utils import file

DEFAULT_OFFSET = 0
DEFAULT_QUERY_LIST_SIZE = 50
MAX_QUERY_LIST_SIZE = 1000


def serialize_to_ttype(obj, ttype, fields=None):
    tobj = ttype()

    fields = fields or tobj.__dict__
    for k in fields:
        attr = getattr(obj, k)

        if isinstance(attr, datetime.datetime):
            attr = datetime2utc(attr)
        elif isinstance(attr, decimal.Decimal):
            attr = float(attr)
        elif isinstance(attr, (datetime.date, datetime.time)):
            attr = unicode(attr)

        setattr(tobj, k, attr)

    return tobj


def ttype_to_obj(ttype, cls, include=None, exclude=None, **kwargs):
    if include:
        _kwargs = {k: v for k, v in ttype.__dict__.iteritems() if k in include}
    else:
        _kwargs = copy.copy(ttype.__dict__)

    if exclude:
        for _field in exclude:
            _kwargs.pop(_field, None)

    _kwargs.update(kwargs)
    return cls(**_kwargs)


def obj_hash2url(obj, hash_attr, set_null=True):
    hash_value = getattr(obj, hash_attr)
    try:
        url_value = file.get_file_url(hash_value)
    except:
        url_value = ''

    url_attr = hash_attr.replace('hash', 'url')
    setattr(obj, url_attr, url_value)

    if set_null:
        setattr(obj, hash_attr, None)


# old stuff
def t_timestamp_to_datetime(timestamp):
    if not timestamp:
        return datetime.datetime.now()
    return datetime.datetime.fromtimestamp(timestamp)


# old stuff
def t_time_to_time(_time):
    if not _time:
        return datetime.time(0, 0, 0)
    hour, minute, second = [int(x) for x in _time.split(':')]
    return datetime.time(hour, minute, second)


def model2dict(model, exclude=None):
    result = {}
    for k, v in model.__dict__.iteritems():
        if k.startswith('_'):
            continue
        if exclude and k in exclude:
            continue
        result[k] = v
    return result


def make_query(q, cls, attrs):
    if not attrs:
        return q

    offset = attrs.pop('offset', DEFAULT_OFFSET)
    limit = attrs.pop('limit', DEFAULT_QUERY_LIST_SIZE)

    for name, value in attrs.items():
        if value is not None:
            q = q.filter(getattr(cls, name) == value)

    q = q.offset(offset)
    q = q.limit(min(limit, MAX_QUERY_LIST_SIZE))

    return q
