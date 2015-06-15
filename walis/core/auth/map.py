#!/usr/bin/env python2
# coding=utf8

from __future__ import absolute_import, division, print_function
from .util import (
    union,
    customer_service,
    contract_customer,
    activity_manager,
    directors,
    finance,
    file_auth,
    risk_service_manager,
    superadmin
)

""" Auth map for flask view functions
KEY: <endpoint>
VALUE: <permission groups>
"""

AUTH_MAP = {
    # File
    # 'FileApi:get': file_auth,
    # 'FileApi:post': file_auth,
    # 'FileApi:delete': file_auth,

    # User
    'HongbaoApi:get_list': customer_service,
    'HongbaoApi:delete': customer_service,

    # Restaurant
    'RestaurantDirector': union(directors, ['business_development']),

    # Pay
    'RefundApi:retry': customer_service,
    'RefundApi:ignore': customer_service,
    'RefundApi:revoke': finance,
    'RefundApi:done': finance,
    'PaymentApi:get_alipay_url': ['finance_mananger', 'finance_teller'],
    'PaymentApi:get_unprocessed_batch': ['finance_mananger', 'finance_teller'],

    # Misc
    'ChaosApi:edit_username_mobile': customer_service,
    'ChaosApi:get_user': customer_service,
    'SimpleURLApi:get_empty_image_hash_restaurant': superadmin,

    # Login
    'LoginApi:switch_user': superadmin,
    'LoginApi:switch_user_off': superadmin,

}

AUTH_MAP_HR = {

    # Restaurant
    'RestaurantApi:get': 'JAVIS.RST.RST.INFO.GET',
    'RestaurantApi:put': 'JAVIS.RST.RST.INFO.UPDATE',
    'RestaurantApi:payment_log': 'JAVIS.RST.RST.PAYLOG',

    # Certification
    'CertificationApi:get': 'JAVIS.CERT.INFO.GET',
    'CertificationApi:post': 'JAVIS.CERT.INFO.NEW',
    'CertificationApi:put': 'JAVIS.CERT.INFO.UPDATE',
    'CertificationApi:get_by_uploader': 'JAVIS.CERT.INFO.UPLOADER.GET',
    'CertificationApi:get_by_admin': 'JAVIS.CERT.INFO.ADMIN.GET',
    'CertificationApi:get_certification_list_from_mm': 'JAVIS.CERT.LIST.GET',
    'CertificationApi:get_processing_record': 'JAVIS.CERT.PROCESS.GET',
    'CertificationApi:process': 'JAVIS.CERT.PROCESS.APPROVE',

    # Activity
    'RstActivityApi:post': 'JAVIS.ACT.RST.POST',
    'RstActivityApi:put': 'JAVIS.ACT.RST.PUT',
    'RstActivityApi:get': 'JAVIS.ACT.RST.GET',
    'RstActivityApi:get_by_city_and_period': 'JAVIS.ACT.RST.GET_BYREGION',
    'RstActivityApi:query_restaurant_activity_for_admin': 'JAVIS.ACT.RST.GET_ALL',

    # RstBankCardApi
    'RstBankCardApi:get_pre_next': 'JAVIS.RST.RST_BANKCARD.GET_PRE_NEXT',
    'RstBankCardApi:bankcard_approve': 'JAVIS.RST.RST_BANKCARD.APPROVE',
    'RstBankCardApi:bankcard_reject': 'JAVIS.RST.RST_BANKCARD.REJECT',
    'RstBankCardApi:unbind_bankcard': 'JAVIS.RST.RST_BANKCARD.UNBIND',
    'RstBankCardApi:add_rst_bankcard': 'JAVIS.RST.RST_BANKCARD.CREATE',
    'RstBankCardApi:update_rst_bankcard': 'JAVIS.RST.RST_BANKCARD.UPDATE',
    'RstBankCardApi:get_bankcard': 'JAVIS.RST.RST_BANKCARD.GET',
    'RstBankCardApi:gets_by_rst': 'JAVIS.RST.RST_BANKCARDLIST.GET',
    'RstBankCardApi:gets': 'JAVIS.RST.RST_BANKCARD.GETS',  #isall

    # Coupon
    'CouponApi:get': 'JAVIS.RST.COUPON.GET',
    'CouponApi:post': 'JAVIS.RST.COUPON.NEW',
    'CouponApi:put': 'JAVIS.RST.COUPON.UPDATE',
    'CouponApi:gets': 'JAVIS.RST.COUPON.LIST.GET',
    'CouponApi:validate_sn': 'JAVIS.RST.COUPON.VALIDSN',

    # Restaurant Coupon Batch
    'CouponBatchApi:post': 'JAVIS.RST.COUPON.BATCH',
}

auth_map_admin = {
    'ACT_RST_ADMIN': 'JAVIS.ACT.ACT_RST.GET_BY_REGION.ADMIN',
    'RST_ADMIN': 'JAVIS.RST.RST_BANKCARD.GETS.ADMIN',
}

# TODO to be deprecated
permission_map = {

    'superadmin': 'superadmin',

    'ActivityPaymentApi:get_all_status': directors,

    'FileApi:delete_fuss': union(activity_manager,
                                 customer_service),

    'ActivityPaymentApi:_get_operation_time': ['eleme_ask_admin'],

    'BannerApi': ['city_director',
                  'activity_manager',
                  'marketing_manager'],

}

# File access auth
file_auth = [
    'city_director',
    'region_director',
    'entry_director',
    'customer_service_director',
    'customer_service',
    'finance_mananger',
    'finance_teller',
]
