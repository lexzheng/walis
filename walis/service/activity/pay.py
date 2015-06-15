#!/usr/bin/env python2
# coding=utf8

from __future__ import absolute_import, division, print_function
import datetime

from flask.ext.login import current_user

from walis.service.activity import base as act_base
from walis.service.activity.utils import get_restaurant_activity_name
from .pay_notice.query import (
    query_paylog_by_rst,
    count_paylog_by_rst,
    query_process_records_by_ids,
    query_pay_records, query_paylog, get_max_subsidy_process_record_ids)
from walis.model.zeus.activity import ActivityStats, SubsidyProcessRecord
from walis.thirdparty import thirdparty_svc, thrift_client
from walis.utils.format import to_int, to_float, set_null
from walis.utils.paging import get_paging_params
from walis.utils.thrift import dict2ttype

from walis.exception.util import raise_user_exc
from walis.exception.error_code import ACTIVITY_PAYMENT_PROC_ILL_ERR


MONDAY = 0
TUESDAY = 1
WEDNESDAY = 2
THURSDAY = 3
SUNDAY = 6

# activity stats
STATUS_PENDING = 1
STATUS_NO_SUBSIDY = 2
STATUS_PAY_RECORD_GENERATED = 3
STATUS_PAY_SUCCESS = 4
STATUS_PAY_FAIL = 5

CONST_FROM_HOUR = 6
CONST_TO_HOUR = 24

audit_enabled_weekday = (MONDAY, TUESDAY, WEDNESDAY, THURSDAY, SUNDAY)

ACTIVITY_CATEGORY_MAP = {
    11: u'美食活动',
    12: u'餐厅活动',
}


def get_pending_activity_stats(args):
    """ get activity status which is pending """
    search_text = to_int(args.get('search_text'))
    query_city_id = to_int(args.get('city_id'))
    page_no, page_size = get_paging_params()
    user_city_ids, user_restaurant_ids = \
        get_city_ids_or_restaurant_ids_by_user()

    t_activity_status_query = thirdparty_svc.eos.TActivityStatsQuery()
    t_activity_status_query.statuses = [
        thirdparty_svc.eos.ActivityStatsConst.STATUS_PENDING, ]
    t_activity_status_query.with_subsidy = True
    t_activity_status_query.from_date = args.get('from_date')
    t_activity_status_query.to_date = args.get('to_date')
    t_activity_status_query.offset = (page_no - 1) * page_size
    t_activity_status_query.limit = page_size

    # if current_user is admin, restaurant_ids and user_city_ids are None.
    if current_user.is_super_admin():
        if query_city_id is not None:
            t_activity_status_query.city_ids = [query_city_id, ]
        if search_text is not None:
            t_activity_status_query.restaurant_ids = [search_text, ]
        with thrift_client('eos') as eos:
            activity_status_list = eos.query_auto_pay_activity_stats_result(
                t_activity_status_query)
        return [act.__dict__ for act in activity_status_list]

    if user_restaurant_ids or user_city_ids:
        city_ids = user_city_ids
        if query_city_id is not None:
            if user_city_ids is None or query_city_id in user_city_ids:
                city_ids = [query_city_id, ]
            else:
                return []
        t_activity_status_query.city_ids = city_ids

        # if user_city_ids is not None, user_restaurant_ids must be None
        restaurant_ids = user_restaurant_ids
        if search_text is not None:
            restaurant_ids = [search_text, ]
        t_activity_status_query.restaurant_ids = restaurant_ids

        with thrift_client('eos') as eos:
            activity_status_list = eos.query_auto_pay_activity_stats_result(
                t_activity_status_query)

        return [act.__dict__ for act in activity_status_list]

    else:
        return []


def create_act_stats_query(args):
    page_no, page_size = get_paging_params()
    t_query = dict2ttype(args, thirdparty_svc.eos.TActivityStatsQuery(),
                         keys=['activity_id', 'activity_category_id',
                               'from_date', 'to_date'])
    if t_query.activity_id:
        t_query.activity_id = int(t_query.activity_id)
    if t_query.activity_category_id:
        t_query.activity_category_id = int(t_query.activity_category_id)
    t_query.offset = (page_no - 1) * page_size
    t_query.limit = page_size

    status = args.get('status')
    city_id = args.get('city_id')
    restaurant_id = args.get('restaurant_id')

    city_ids, rest_ids = get_city_ids_or_restaurant_ids_by_user()
    t_query.city_ids = city_ids
    t_query.restaurant_ids = rest_ids

    if status:
        t_query.statuses = [int(status), ]

    if city_id:
        city_id = int(city_id)
        if city_ids is None or city_id in city_ids:
            t_query.city_ids = [city_id, ]
        else:
            return None

    if restaurant_id:
        restaurant_id = int(restaurant_id)
        if rest_ids is None or restaurant_id in rest_ids:
            t_query.restaurant_ids = [restaurant_id, ]
        else:
            return None
    return t_query


def get_all_activity_stats(args):
    t_query = create_act_stats_query(args)
    if not t_query:
        return []

    with thrift_client('eos') as eos:
        act_status_list = eos.query_auto_pay_activity_stats_result(t_query)

    return [act_status.__dict__ for act_status in act_status_list]


def set_activity_names(activity_payments):
    for payment in activity_payments:
        activity_id, category_id = payment['activity_id'], \
                                   payment['activity_category_id']

        payment['activity_name'] = get_activity_name(
            activity_id, category_id)
    return activity_payments


def get_activity_name(activity_id, category_id):
    activity_name = ''
    try:
        activity = act_base.get(activity_id, category_id)
    except:
        return u'活动不存在'

    ACTIVITY_CATEGORY = thirdparty_svc.ers.SubsidyConst()
    if category_id == ACTIVITY_CATEGORY.CATEGORY_RESTAURANT_ACTIVITY:
        activity_name = get_restaurant_activity_name(activity)
        if activity_name:
            try:
                activity_name = activity_name.decode('utf-8')
            except Exception:
                pass
        else:
            activity_name = ''
    elif category_id == ACTIVITY_CATEGORY.CATEGORY_FOOD_ACTIVITY:
        activity_name = activity.name

    return activity_name


def set_act_category_names(activity_payments):
    for payment in activity_payments:
        category_id = payment['activity_category_id']
        payment['activity_category_id'] = ACTIVITY_CATEGORY_MAP[category_id]
    return activity_payments


def set_user_bank_card(activity_payments):
    restaurant_ids = [payment['restaurant_id']
                      for payment in activity_payments]

    with thrift_client('eus') as eus:
        bank_card_map = eus.mget_bankcard_by_restaurant(restaurant_ids)

    with thrift_client('ers') as ers:
        bank_card_map2 = ers.mget_restaurant_bankcard(restaurant_ids)

    for payment in activity_payments:
        payment['have_bank_card'] = False
        card_id = cardholder_name = ''
        user_bank_card = bank_card_map.get(payment['restaurant_id'])
        if user_bank_card is not None:
            card_id = user_bank_card.card_id
            cardholder_name = user_bank_card.cardholder_name
        else:
            user_bank_card2 = bank_card_map2.get(payment['restaurant_id'])
            if user_bank_card2 is not None:
                card_id = user_bank_card2.card_id
                cardholder_name = user_bank_card2.cardholder_name

        payment['card_id'] = card_id
        payment['cardholder_name'] = cardholder_name

    return activity_payments


def set_bank_card_exist_or_not(activity_payments):
    restaurant_ids = [payment['restaurant_id']
                      for payment in activity_payments]

    with thrift_client('eus') as eus:
        bank_card_map = eus.mget_bankcard_by_restaurant(restaurant_ids)

    with thrift_client('ers') as ers:
        bank_card_map2 = ers.mget_restaurant_bankcard(restaurant_ids)

    for payment in activity_payments:
        restaurant_id = payment['restaurant_id']
        if bank_card_map.get(restaurant_id) or bank_card_map2.get(
                restaurant_id):
            payment['have_bank_card'] = True
        else:
            payment['have_bank_card'] = False

    return activity_payments


def approval_payment(payment_dict):
    restaurant_ids_set = set()
    [restaurant_ids_set.update(restaurant_ids) for restaurant_ids in
     payment_dict.values()]
    with thrift_client('eos') as eos:
        for restaurant_id in restaurant_ids_set:
            eos.generate_activity_subsidy_pay_record_new(restaurant_id)


def reject_payment(payment_dict):
    restaurant_ids_set = set()
    [restaurant_ids_set.update(restaurant_ids) for restaurant_ids in
     payment_dict.values()]
    with thrift_client('eos') as eos:
        for restaurant_id in restaurant_ids_set:
            eos.doubt_activity_subsidy_stats_new(restaurant_id)


def get_city_ids_or_restaurant_ids_by_user():
    """ return [city_ids,], [restaurant_ids] """
    user_id = current_user.id

    # if super admin
    if current_user.is_super_admin():
        return None, None

    with thrift_client('ers') as ers:
        user_struct = ers.get_direct_struct(user_id)

    # if city.admin
    if user_struct.city_ids:
        return user_struct.city_ids, None

    region_ids = []
    # if region_group.admin
    if user_struct.region_group_ids:
        with thrift_client('ers') as ers:
            regions = ers.get_regions_by_region_group_ids(
                user_struct.region_group_ids)
        region_ids = [region.id for region in regions]

    # if region.admin
    if user_struct.region_ids:
        region_ids.extend(user_struct.region_ids)
        region_ids = list(set(region_ids))

    with thrift_client('ers') as ers:
        restaurant_ids = ers.mget_restaurant_in_region(region_ids, True)

    return None, restaurant_ids


def get_failed_status_indication(args):
    """ get failed status indication """
    t_query = create_act_stats_query(args)
    if not t_query:
        return []

    with thrift_client('eos') as eos:
        # get no_subsidy
        no_subsidy_indication = len(eos.query_auto_pay_activity_stats_result(
            t_query))

        # get pay_fail
        t_query.statuses = [STATUS_PAY_FAIL, ]
        pay_fail_indication = len(eos.query_auto_pay_activity_stats_result(
            t_query))

    return no_subsidy_indication, pay_fail_indication


def get_audit_status():
    now = datetime.datetime.now()
    if now.weekday() in audit_enabled_weekday \
            and CONST_FROM_HOUR < now.hour < CONST_TO_HOUR:
        return True
    return False


def get_pay_records(rst_id, activity_id=None, activity_category_id=None,
                    offset=None, limit=None):
    records_paging = query_paylog_by_rst(rst_id, activity_id,
                                         activity_category_id, offset, limit)
    total_num = count_paylog_by_rst(rst_id, activity_id, activity_category_id)

    record_process_ids = [r[9] for r in records_paging if r[9]]
    record_process_logs = query_process_records_by_ids(record_process_ids)
    process_log_map = {r.id: r for r in record_process_logs}

    records = []
    for record in records_paging:
        new_record = {
            'record_id': record[0],
            'first_date': record[4],
            'last_date': record[5],
            'quantity': to_int(record[6]),
            'audit_time': record[8],
            'total_subsidy': to_float(record[7]),
            'activity_id': record[1],
            'activity_category_id': record[2],
        }
        process_log = process_log_map.get(record[9], None)

        new_record['card_id'] = process_log.card_id \
            if process_log else None
        new_record['cardholder_name'] = process_log.cardholder_name \
            if process_log else None

        if process_log:
            new_record['status'] = process_log.status
        elif record[3] == ActivityStats.STATUS_PAY_RECORD_GENERATED:
            new_record['status'] = 1
        else:
            raise_user_exc(ACTIVITY_PAYMENT_PROC_ILL_ERR)

        if new_record['status'] == SubsidyProcessRecord.STATUS_SUBMITTED:
            new_record['submit_time'] = process_log.processed_at
        elif new_record['status'] in [3, 4]:
            new_record['success_time'] = process_log.processed_at

        records.append(new_record)

    for record in records:
        # set activity name
        try:
            record['activity_name'] = act_base.get_name(
                record['activity_id'], record['activity_category_id'])
        except:
            # Fix history problem
            record['activity_name'] = ''

    record_results = set_null(records,
                              ['card_id', 'cardholder_name',
                               'audit_time', 'submit_time', 'success_time'])

    return record_results, total_num


def get_pay_records2(rst_id, activity_id=None, activity_category_id=None,
                     offset=None, limit=None):

    pay_records = query_pay_records(rst_id)
    pay_record_ids = [p.id for p in pay_records]
    pay_record_map = {p.id: p.created_at for p in pay_records}

    paylogs = query_paylog(pay_record_ids, activity_id, activity_category_id,
                           offset, limit)
    record_process_ids = get_max_subsidy_process_record_ids(pay_record_ids)

    total_num = count_paylog_by_rst(rst_id, activity_id, activity_category_id)

    record_process_logs = query_process_records_by_ids(
        [p[0] for p in record_process_ids])
    process_log_map = {r.pay_record_id: r for r in record_process_logs}

    records = []
    for record in paylogs:
        new_record = {
            'record_id': record[0],
            'first_date': record[4],
            'last_date': record[5],
            'quantity': to_int(record[6]),
            'audit_time': pay_record_map[record[0]],
            'total_subsidy': to_float(record[7]),
            'activity_id': record[1],
            'activity_category_id': record[2],
        }
        process_log = process_log_map.get(record[0], None)

        new_record['card_id'] = process_log.card_id \
            if process_log else None
        new_record['cardholder_name'] = process_log.cardholder_name \
            if process_log else None

        if process_log:
            new_record['status'] = process_log.status
        elif record[3] == ActivityStats.STATUS_PAY_RECORD_GENERATED:
            new_record['status'] = 1
        else:
            raise Exception('Invalid pay process record status.')

        if new_record['status'] == SubsidyProcessRecord.STATUS_SUBMITTED:
            new_record['submit_time'] = process_log.processed_at
        elif new_record['status'] in [3, 4]:
            new_record['success_time'] = process_log.processed_at

        records.append(new_record)

    for record in records:
        # set activity name
        try:
            record['activity_name'] = act_base.get_name(
                record['activity_id'], record['activity_category_id'])
        except:
            # Fix history problem
            record['activity_name'] = ''

    record_results = set_null(records,
                              ['card_id', 'cardholder_name',
                               'audit_time', 'submit_time', 'success_time'])

    return record_results, total_num

