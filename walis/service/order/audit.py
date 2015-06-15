#!/usr/bin/env python2
# -*- coding: utf8 -*-
from __future__ import absolute_import, division, print_function
from compiler.ast import flatten
import json
import datetime

from flask.ext.login import current_user

from walis.core.db.mongo import mongo
from walis.thirdparty import (
    thrift_client,
    thirdparty_svc,
)
from walis.utils.dirty import zeus_query
from walis.utils.misc import any_to_raw, getresult_to_raw


class CustomerServiceUserBase():
    @classmethod
    def get(self, pk=None):
        result = None
        with thrift_client('eus') as eus:
            if pk is None:
                # 2 是客服人员-.-
                all_permissions = current_user.has_permissions(
                    'walle_all_user_manage', True)
                parial_permissions = current_user.has_permissions(
                    'walle_partial_user_manage', True)
                user_ids = None
                if not all_permissions:
                    user_ids = eus.get_managed_user_ids(current_user.id)
                    if parial_permissions and len(user_ids):
                        pass
                    else:
                        user_ids = [current_user.id]
                query_kwargs = {
                    'limit': 1000,
                    'offset': 0,
                    'keyword': None,

                    'is_active': None,
                    'is_super_admin': None,
                    'group_ids': None,
                    'category': 2,
                    'mobile': None,
                    'email': None,
                    'name': None,

                    'region_ids': None,
                    'region_group_ids': None,
                    'city_ids': None,
                    'user_ids': user_ids,
                }
                _result = zeus_query('eus', 'walle_get_user_list',
                                     thirdparty_svc.eus.TUserQuery, **query_kwargs)
                _result = json.loads(_result)
                users = _result['list']

                dop_users = eus.mget_dop_user([user['id'] for user in users])

                # dop_users = eus.mget_dop_user(range(0,500))
                dop_users = any_to_raw(dop_users)

                # user_ids = [dop_user['user_id'] for dop_user in dop_users]
                # _result = zeus_query('eus','walle_get_user_list',eus_thrift.TUserQuery,user_ids=user_ids)
                # _result = json.loads(_result)
                # users = _result['list']

                user_id_name_map = {user['id']: user['username'] for user in
                                    users}
                for dop_user in dop_users:
                    dop_user['username'] = user_id_name_map[dop_user['user_id']]
                result = dop_users
                # mongo update allow_order_audit
                _dop_users = mongo.dop_user.find()
                _dop_users_map = {doc['user_id']: doc for doc in _dop_users}
                for dop_user in dop_users:
                    _dop_user = _dop_users_map.get(dop_user['user_id'], {})
                    dop_user['allow_order_audit'] = _dop_user.get(
                        'allow_order_audit', False)
        return result

    @classmethod
    def post_or_put(cls, pk=None, dic=None):
        if pk is None:
            return
        else:
            spec = {
                '_id': pk,
            }
            dic.pop('_id', None)
            mongo.dop_user.update(spec, dic, upsert=True)

    @classmethod
    def get_auditor_amount(cls):
        spec = {
            'allow_order_audit': True,
        }
        return mongo.dop_user.find(spec).count()


class OrderAuditBase():
    @classmethod
    def get_suspicious_orders(cls, restaurant_id, date, **kwargs):
        query_kwargs = {
            'restaurant_id': restaurant_id,
            'date': date
        }
        result = zeus_query('eyes', 'walle_get_suspicious_orders',
                            thirdparty_svc.eyes.TWalleSuspiciousOrderQuery,
                            **query_kwargs)
        # for order in result:
        # order['id'] = order['_id']
        order_ids = [order['id'] for order in result]
        orders = OrderBase.mget(order_ids)
        orders = {order['id']: order for order in orders}
        with thrift_client('eos') as eos:
            orders_info = eos.mget_order_info(order_ids)
            orders_info = getresult_to_raw(orders_info)
        orders_info = {info['order_id']: info for info in orders_info}
        for order in result:
            order.update(orders[order['id']])
            order.update(orders_info[order['id']])
        for order in result:
            if order['phone_rating'] == 1:
                order['is_new_user'] = True
            else:
                order['is_new_user'] = False
        phones = [order['phone'] for order in orders.values()]
        phones_ban_status_map = {phone: PhoneBanBase.get_phone_ban_status(phone)
                                 for phone in phones}
        user_ids = [order['user_id'] for order in orders.values()]
        with thrift_client('eus') as eus_client:
            users = eus_client.mget(user_ids)
            users = any_to_raw(users)
        users_map = {user['id']: user for user in users}
        for order in result:
            order['phone_ban_status'] = phones_ban_status_map[order['phone']]
            order['user_is_active'] = users_map[order['user_id']]['is_active']
        for order in result:
            try:
                better_json = json.loads(order['better_json'])
                better_json = flatten(better_json)
                subsidy = 0
                for _better_what in better_json:
                    price = _better_what.get('price', 0)
                    if price < 0:
                        subsidy += price
                order['subsidy'] = abs(subsidy)
                order['id'] = unicode(order['id'])
            except:
                continue
        return result

    @classmethod
    def finish_suspicious_group_auditing(cls, restaurant_id, date):
        with thrift_client('eyes') as eyes_client:
            result = eyes_client.walle_finish_suspicious_group_auditing(
                restaurant_id, date)
        return result

    @classmethod
    def assign_suspicious_orders(cls, auditor_id, auditor_amount, date):
        with thrift_client('eyes') as eyes_client:
            result = eyes_client.walle_distribute_suspicious_orders(auditor_id,
                                                                    auditor_amount,
                                                                    date)
        return result

    @classmethod
    def filter_suspicious_orders_amount(cls, auditor_id, status, date,
                                        **kwargs):
        query_kwargs = {
            'auditor_id': auditor_id,
            'status': status,
            'date': date,
        }
        result = zeus_query('eyes', 'walle_filter_suspicious_orders_amount',
                            thirdparty_svc.eyes.TWalleSuspiciousOrderAmountQuery,
                            **query_kwargs)
        # temp fix-.-
        result = json.loads(result)
        return result

    @classmethod
    def set_restaurant_suspicious(cls, restaurant_id, is_suspicious,
                                  suspicious_description):
        spec = {
            'restaurant_id': restaurant_id,
        }
        doc = {
            '$set': {'is_suspicious': is_suspicious,
                     'suspicious_description': suspicious_description}
        }
        mongo.restaurant.update(spec, doc, upsert=True)


class OrderBase():
    @classmethod
    def get(cls, pk_or_pks):
        with thrift_client('eos') as eos:
            if isinstance(pk_or_pks, (tuple, list)):
                result = eos.mget(pk_or_pks)
            else:
                result = eos.get_entry(pk_or_pks)
        result = any_to_raw(result)
        return result

    mget = get

    @classmethod
    def set_invalid(cls, order_id, reason_type, remark):
        order_id = int(order_id)
        with thrift_client('eos') as eos:
            result = eos.eleme_process_order(order_id,
                                             thirdparty_svc.eos.ElemeOrderConst.STATUS_INVALID,
                                             current_user.id,
                                             thirdparty_svc.eos.OrderRecordConst.PROCESS_GROUP_ADMIN,
                                             remark,
                                             reason_type)
            result = any_to_raw(result)
        return result

    @classmethod
    def set_valid(cls, order_id, ):
        order_id = int(order_id)
        with thrift_client('eos') as eos:
            result = eos.eleme_process_order(
                order_id,
                thirdparty_svc.eos.ElemeOrderConst.STATUS_PROCESSED_AND_VALID,
                current_user.id,
                thirdparty_svc.eos.OrderRecordConst.PROCESS_GROUP_ADMIN,
                "",
                thirdparty_svc.eos.OrderInvalidDescConst.TYPE_OTHERS,
            )
            result = any_to_raw(result)
        return result

    @classmethod
    def set_phone_confirmed(cls, order_id, confirmed):
        order_id = int(order_id)
        with thrift_client('eos') as eos:
            result = eos.set_order_phone_confirmed(order_id, confirmed)
            result = any_to_raw(result)
        return result


class PhoneBanBase():
    WHITE = 0
    BLACK = 1
    GREY = 2

    @classmethod
    def get_phone_ban_status(cls, phone):
        spec = {
            'phone': phone,
            'status': 'unprocessed',
        }
        if mongo.phone_unban_log.find(spec).count():
            return cls.GREY
        return cls.is_banned(phone)

    @classmethod
    def is_banned(cls, phone):
        with thrift_client('eos') as eos_client:
            result = eos_client.check_phones_in_blacklist([phone, ])
            if result:
                return cls.BLACK
            else:
                return cls.WHITE

    @classmethod
    def set_banned(cls, phone, admin_user_id, is_banned, description):
        if is_banned:
            with thrift_client('eos') as eos:
                eos.add_phone_to_blacklist(phone, description)
        else:
            doc = {
                'phone': phone,
                'admin_user_id': admin_user_id,
                'is_banned': is_banned,
                'description': description,
                'created_at': datetime.datetime.utcnow()
            }
            mongo.phone_unban_log.insert(doc)


class UserBanBase():
    @classmethod
    def set_active(cls, user_id, admin_user_id, is_active, description):
        with thrift_client('eus') as eus_client:
            result = eus_client.walle_set_user_active(user_id, admin_user_id,
                                                      is_active, description)
        return result
