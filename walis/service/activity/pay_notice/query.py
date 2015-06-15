#!/usr/bin/env python2
# coding=utf8

from __future__ import absolute_import, division, print_function

from sqlalchemy import func

from walis.model.walis import walis_session
from walis.model.zeus import zeus_session, zeus_db_handler
from walis.model.zeus.activity import (
    SubsidyProcessRecord,
    SubsidyPayRecord,
    ActivityStats,
)
from walis.model.walis.activity import PaymentNoticeRecord as NoticeRecord
from walis.utils.time import get_today_begin_time, get_today_end_time


MAX_LIST_SIZE = 1000
DEFAULT_LIST_SIZE = 200


def get_new_pay_records(process_at, limit=200):
    with zeus_session() as session:
        result = session.query(SubsidyPayRecord.id,
                               SubsidyPayRecord.restaurant_id,
                               SubsidyProcessRecord.card_id,
                               SubsidyProcessRecord.processed_at,
                               SubsidyPayRecord.status). \
            outerjoin(SubsidyProcessRecord,
                      SubsidyProcessRecord.pay_record_id == SubsidyPayRecord.id). \
            filter(SubsidyPayRecord.id > process_at). \
            filter(SubsidyProcessRecord.status != SubsidyProcessRecord.STATUS_FAIL). \
            order_by(SubsidyPayRecord.id.asc()).limit(limit).all()

        return result


def get_success_pay_records(record_ids):
    with zeus_session() as session:
        result = session.query(SubsidyPayRecord.id,
                               SubsidyPayRecord.restaurant_id,
                               SubsidyProcessRecord.card_id,
                               SubsidyProcessRecord.processed_at,). \
            outerjoin(SubsidyProcessRecord,
                      SubsidyProcessRecord.pay_record_id == SubsidyPayRecord.id). \
            filter(SubsidyPayRecord.status == SubsidyPayRecord.STATUS_SUCCESS). \
            filter(SubsidyProcessRecord.status != SubsidyProcessRecord.STATUS_FAIL). \
            filter(SubsidyPayRecord.id.in_(record_ids)).all()

        return result


def get_activity_stats(pay_record_id):
    with zeus_session() as session:
        results = session.query(ActivityStats.activity_id,
                                ActivityStats.activity_category_id,
                                func.sum(ActivityStats.total_subsidy),
                                func.min(ActivityStats.date),
                                func.max(ActivityStats.date),
                                func.sum(ActivityStats.quantity), ).group_by(
            ActivityStats.restaurant_id, ActivityStats.activity_id,
            ActivityStats.activity_category_id). \
            filter(ActivityStats.pay_record_id == pay_record_id). \
            filter(ActivityStats.status == ActivityStats.STATUS_PAY_SUCCESS).all()

        return results


def get_success_record_ids_by_restaurant(
        restaurant_id, activity_id=None, activity_category_id=None):
    with zeus_session() as session:
        query = session.query(SubsidyPayRecord.id). \
            filter(SubsidyPayRecord.restaurant_id == restaurant_id). \
            filter(SubsidyPayRecord.status == SubsidyPayRecord.STATUS_SUCCESS)

        if activity_id is not None:
            query.filter(SubsidyPayRecord.activity_id == activity_id)

        if activity_category_id is not None:
            query.filter(
                SubsidyPayRecord.activity_category_id == activity_category_id)
        record_ids = query.all()

        return [r[0] for r in record_ids]


PAYLOG_STATUS_LIST = {
    ActivityStats.STATUS_PAY_RECORD_GENERATED,
    ActivityStats.STATUS_PAY_SUCCESS,
    ActivityStats.STATUS_PAY_FAIL,
}


@zeus_db_handler
def query_paylog_by_rst(restaurant_id, activity_id=None,
                        activity_category_id=None, offset=None, limit=None):
    """ Except ActivityStats.STATUS_PENDING （未审核状态）
    """
    q = session.query(
        ActivityStats.pay_record_id,
        ActivityStats.activity_id,
        ActivityStats.activity_category_id,
        ActivityStats.status,
        func.min(ActivityStats.date),
        func.max(ActivityStats.date),
        func.sum(ActivityStats.quantity),
        func.sum(ActivityStats.total_subsidy),
        SubsidyPayRecord.created_at,
        func.max(SubsidyProcessRecord.id)). \
        group_by(ActivityStats.pay_record_id,
                 ActivityStats.activity_id,
                 ActivityStats.activity_category_id). \
        outerjoin(SubsidyPayRecord,
                  SubsidyPayRecord.id == ActivityStats.pay_record_id). \
        outerjoin(SubsidyProcessRecord,
                  SubsidyProcessRecord.pay_record_id == SubsidyPayRecord.id). \
        filter(ActivityStats.restaurant_id == restaurant_id).\
        filter(ActivityStats.status.in_(PAYLOG_STATUS_LIST)).\
        order_by(SubsidyPayRecord.created_at.desc())

    if activity_id is not None:
        q = q.filter(ActivityStats.activity_id == activity_id)

    if activity_category_id is not None:
        q = q.filter(ActivityStats.activity_category_id == activity_category_id)

    if limit is not None:
        q = q.limit(min(limit, MAX_LIST_SIZE))
    else:
        q = q.limit(DEFAULT_LIST_SIZE)

    if offset is not None:
        q = q.offset(offset)

    return q


@zeus_db_handler
def query_pay_records(restaurant_id, offset=None, limit=None):
    q = session.query(SubsidyPayRecord).\
        filter(SubsidyPayRecord.restaurant_id == restaurant_id).\
        order_by(SubsidyPayRecord.created_at.desc())

    if limit is not None:
        q = q.limit(min(limit, MAX_LIST_SIZE))
    else:
        q = q.limit(DEFAULT_LIST_SIZE)

    if offset is not None:
        q = q.offset(offset)

    return q.all()


@zeus_db_handler
def query_paylog(pay_record_ids, activity_id=None, activity_category_id=None,
                 offset=None, limit=None):
    q = session.query(
        ActivityStats.pay_record_id,
        ActivityStats.activity_id,
        ActivityStats.activity_category_id,
        ActivityStats.status,
        func.min(ActivityStats.date),
        func.max(ActivityStats.date),
        func.sum(ActivityStats.quantity),
        func.sum(ActivityStats.total_subsidy)).\
        group_by(ActivityStats.pay_record_id,
                 ActivityStats.activity_id,
                 ActivityStats.activity_category_id). \
        filter(ActivityStats.pay_record_id.in_(pay_record_ids)).\
        filter(ActivityStats.status.in_(PAYLOG_STATUS_LIST)).\
        order_by(ActivityStats.created_at.desc())

    if activity_id is not None:
        q = q.filter(ActivityStats.activity_id == activity_id)

    if activity_category_id is not None:
        q = q.filter(ActivityStats.activity_category_id == activity_category_id)

    if limit is not None:
        q = q.limit(min(limit, MAX_LIST_SIZE))
    else:
        q = q.limit(DEFAULT_LIST_SIZE)

    if offset is not None:
        q = q.offset(offset)

    return q


@zeus_db_handler
def get_max_subsidy_process_record_ids(pay_record_ids):
    q = session.query(func.max(SubsidyProcessRecord.id)).\
        group_by(SubsidyProcessRecord.pay_record_id).\
        filter(SubsidyProcessRecord.pay_record_id.in_(pay_record_ids))

    return q


@zeus_db_handler
def count_paylog_by_rst(restaurant_id, activity_id=None,
                        activity_category_id=None):
    """ Except ActivityStats.STATUS_PENDING （未审核状态）
    """
    q = session.query(ActivityStats.id). \
        group_by(ActivityStats.pay_record_id,
                 ActivityStats.activity_id,
                 ActivityStats.activity_category_id). \
        filter(ActivityStats.restaurant_id == restaurant_id).\
        filter(ActivityStats.status.in_(PAYLOG_STATUS_LIST))

    if activity_id is not None:
        q = q.filter(ActivityStats.activity_id == activity_id)

    if activity_category_id is not None:
        q = q.filter(ActivityStats.activity_category_id == activity_category_id)

    return len(q.all())


@zeus_db_handler
def query_process_records_by_ids(process_ids):
    query = session.query(SubsidyProcessRecord).\
        filter(SubsidyProcessRecord.id.in_(process_ids))
    return query.all()


@zeus_db_handler
def get_subsidy_record_process_time(record_ids, status):
    return session.query(
        SubsidyProcessRecord.pay_record_id,
        SubsidyProcessRecord.processed_at).\
        filter(SubsidyProcessRecord.pay_record_id.in_(record_ids)).\
        filter(SubsidyProcessRecord.status == status).all()


def get_pay_activities_by_restaurant(rst_id):
    with zeus_session() as session:
        query = session.query(
            ActivityStats.activity_id,
            ActivityStats.activity_category_id,). \
            group_by(ActivityStats.activity_id,
                     ActivityStats.activity_category_id). \
            filter(ActivityStats.restaurant_id == rst_id)

        return query.all()


# javis model begins
def query_sms_send_info(start_time=None, end_time=None, phone=None,
                        restaurant_id=None, card_num_tail=None, status=None):

    with walis_session() as session:
        query = session.query(NoticeRecord)

        if phone:
            query = query.filter(NoticeRecord.phone == phone)

        if restaurant_id:
            query = query.filter(NoticeRecord.restaurant_id == restaurant_id)

        if card_num_tail:
            query = query.filter(NoticeRecord.card_num_tail == card_num_tail)

        if status:
            query = query.filter(NoticeRecord.status == status)

        if not start_time:
            start_time = get_today_begin_time()

        if not end_time:
            end_time = get_today_end_time()

        query = query.filter(NoticeRecord.created_at > start_time).\
            filter(NoticeRecord.created_at < end_time)

        return query.all()


def query_sms_send_count(start_time=None, end_time=None, status=None):
    with walis_session() as session:

        if not start_time:
            start_time = get_today_begin_time()

        if not end_time:
            end_time = get_today_end_time()

        query = session.query(func.count(NoticeRecord.record_id)).\
            filter(NoticeRecord.created_at > start_time).\
            filter(NoticeRecord.created_at < end_time)

        if status is not None:
            query = query.filter(NoticeRecord.status == status)

        return query.scalar()


@zeus_db_handler
def query_auto_pay_activity_stats_result(
        city_ids=None, restaurant_ids=None, activity_id=None,
        activity_category_id=None, from_date=None, to_date=None, statuses=None,
        offset=None, limit=None, with_subsidy=None):
    q = session.query(ActivityStats.restaurant_id,
                      ActivityStats.activity_id,
                      ActivityStats.activity_category_id,
                      func.sum(ActivityStats.quantity),
                      func.sum(ActivityStats.total_subsidy),
                      func.min(ActivityStats.date),
                      func.max(ActivityStats.date)).\
        group_by(ActivityStats.restaurant_id,
                 ActivityStats.activity_id,
                 ActivityStats.activity_category_id).\
        order_by(ActivityStats.restaurant_id.desc())

    return _query_activity_stats(
        q, city_ids, restaurant_ids, activity_id,
        activity_category_id, from_date, to_date, statuses,
        with_subsidy, offset, limit)


def _query_activity_stats(
        q, city_ids=None, restaurant_ids=None, activity_id=None,
        activity_category_id=None, from_date=None, to_date=None, statuses=None,
        with_subsidy=None, offset=None, limit=None):
    if activity_id is not None:
        q = q.filter(ActivityStats.activity_id == activity_id)

    if activity_category_id is not None:
        q = q.filter(ActivityStats.activity_category_id == activity_category_id)  # noqa

    if city_ids is not None:
        q = q.filter(ActivityStats.city_id.in_(city_ids))

    if restaurant_ids is not None:
        q = q.filter(ActivityStats.restaurant_id.in_(restaurant_ids))

    if from_date is not None:
        q = q.filter(ActivityStats.date >= from_date)

    if to_date is not None:
        q = q.filter(ActivityStats.date <= to_date)

    if statuses is not None:
        q = q.filter(ActivityStats.status.in_(statuses))

    if with_subsidy is not None:
        if with_subsidy:
            q = q.filter(ActivityStats.total_subsidy > 0)
        else:
            q = q.filter(ActivityStats.total_subsidy == 0)

    if offset is not None:
        q = q.offset(offset)

    q = q.limit(1000)

    return q
