#!/usr/bin/env python2
# coding=utf8

from __future__ import absolute_import, division, print_function
import time
import datetime


def utc2datetime(t):
    """
    Sends a :class:`float` time value.
    Returns :class:`datetime.datetime` object.

    :param t: :class:`float` time value.
    """
    return datetime.datetime.fromtimestamp(t)


def datetime2utc(dt):
    """
    Sends a :class:`datetime.datetime` object.
    Returns :class:`int` time value.

    :param dt: :class:`datetime` object
    """
    return int(time.mktime(dt.timetuple()))


def get_today_begin_time(return_timestamp=False):
    today = datetime.date.today()
    _datetime = datetime.datetime(
        year=today.year,
        month=today.month,
        day=today.day,
        hour=0)

    if return_timestamp:
        return datetime2timestamp(_datetime)

    return _datetime


def get_today_end_time(return_timestamp=False):
    today = datetime.date.today()
    _datetime = datetime.datetime(
        year=today.year,
        month=today.month,
        day=today.day,
        hour=23,
        minute=59,
        second=59)

    if return_timestamp:
        return datetime2timestamp(_datetime)

    return _datetime


def get_today_date_str():
    return datetime.date.today().strftime('%Y-%m-%d')


def strptime_to_date(date_str):
    return datetime.datetime.strptime(date_str, '%Y-%m-%d').date()


def datetime2timestamp(date_time):
    return time.mktime(date_time.timetuple())


def get_today_string():
    return datetime.date.today().strftime('%Y-%m-%d')


def timestamp2datetime(timestamp):
    if timestamp:
        return datetime.datetime.fromtimestamp(timestamp)
    else:
        return None


def str2datetime(_str):
    return time.strptime(_str, '%Y-%m-%d')


def get_day_start_timestamp(date_str):
    _datetime = str2datetime(date_str)
    hour0_datetime = datetime.datetime(
        year=_datetime.tm_year,
        month=_datetime.tm_mon,
        day=_datetime.tm_mday,
        hour=0,
        minute=0,
        second=0)
    return hour0_datetime


def get_day_end_timestamp(date_str):
    _datetime = str2datetime(date_str)
    hour24_datetime = datetime.datetime(
        year=_datetime.tm_year,
        month=_datetime.tm_mon,
        day=_datetime.tm_mday,
        hour=23,
        minute=59,
        second=59)
    return hour24_datetime


def str2timestamp(date_str):
    return datetime2timestamp(datetime.datetime.strptime(date_str, "%Y-%m-%d"))


def get_timestamp_by_start_date(date_str):
    if date_str:
        return int(time.mktime(get_day_start_timestamp(date_str).timetuple()))
    else:
        return None


def get_timestamp_by_end_date(date_str):
    if date_str:
        return int(time.mktime(get_day_end_timestamp(date_str).timetuple()))
    else:
        return None


def datestr2datetime(_str):
    _time = time.strptime(_str, '%Y-%m-%d')
    return datetime.datetime(
        year=_time.tm_year,
        month=_time.tm_mon,
        day=_time.tm_mday
    )


def datetime2str(_time):
    return _time.strftime('%Y-%m-%d %H:%M:%S')
