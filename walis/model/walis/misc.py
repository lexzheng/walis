#!/usr/bin/env python2
# -*- coding: utf8 -*-

from __future__ import print_function, division, absolute_import

from sqlalchemy import Column, Integer, Numeric, String, SmallInteger\
    ,DateTime, Float,Text, Date, Binary

from walis.model.zeus import ZeusMySession
from walis.model.zeus import ModelBase


class Restaurant(ModelBase):
    __tablename__ = 'restaurant'

    ATTRIBUTE_HALF_PRICE = "half_price"
    ATTRIBUTE_HALF_PRICE_BACKUP = "half_price_backup"
    ATTRIBUTE_FREE_ORDER = "free_order"
    ATTRIBUTE_HUANBAO = "huanbao"
    ATTRIBUTE_HUANBAO_DOUBLE_POINT = "huanbao_double_point"
    ATTRIBUTE_COCA = "coca"
    ATTRIBUTE_DOUBLE_POINT = "double_point"
    ATTRIBUTE_FAPIAO = "fapiao"
    ATTRIBUTE_QUAN = "quan"
    ATTRIBUTE_DISCOUNT8 = "discount8"
    ATTRIBUTE_ZHUKAO_HALF_PRICE = "zhukao_half_price"
    ATTRIBUTE_NEW_USER_DISCOUNT = "new_user_discount"
    # TODO may remove new_user_discount_amount
    ATTRIBUTE_NEW_USER_DISCOUNT_AMOUNT = "new_user_discount_amount"
    ATTRIBUTE_NEW_USER_DISCOUNT_RESTAURANT_PAY = \
        "new_user_discount_restaurant_pay"
    ATTRIBUTE_DISCOUNT_88 = "discount_88"
    ATTRIBUTE_GUANGZHOU_COCA = "guangzhou_coca"
    ATTRIBUTE_EXTRA_DISCOUNT = "extra_discount"

    ATTRIBUTE_SETUP_STEP = 'setup_step'
    ATTRIBUTE_DP_NEW_USER_DISCOUNT = 'dp_new_user_discount'

    SETUP_STEP_NEW_RST = 0
    SETUP_STEP_START_INFO = 1
    SETUP_STEP_BIND_PHONE = 2
    SETUP_STEP_MENU = 3
    SETUP_STEP_ORDER_MODE = 4
    SETUP_STEP_FINISHED = 5

    DOCK_CORP_ELEME_DELIVERY = 7

    CERTIFICATION_TYPE_NONE = 0
    CERTIFICATION_TYPE_PERSONAL = 1
    CERTIFICATION_TYPE_CORP = 2

    # column definitions
    id = Column(Integer, primary_key=True)
    is_valid = Column(SmallInteger, default=1)
    agent_fee = Column(Integer, default=0)
    busy_level = Column(Integer, default=0)
    name = Column(String(255))
    is_premium = Column(SmallInteger, default=0)
    latitude = Column(Numeric(16, 13))
    longitude = Column(Numeric(16, 13))
    description = Column(String(255), default="")
    address_text = Column(String(255))
    deliver_description = Column(String(255), default="")
    num_rating_1 = Column(Integer, default=0)
    num_rating_2 = Column(Integer, default=0)
    num_rating_3 = Column(Integer, default=0)
    num_rating_4 = Column(Integer, default=0)
    num_rating_5 = Column(Integer, default=0)
    service_rating = Column(Float(7), default=0.0)
    created_at = Column(DateTime)
    image_url = Column(String(255), default="")
    image_hash = Column(String(255), default="")
    phone = Column(String(255))
    mobile = Column(String(32), default="")
    order_mode = Column(Integer, default=1)
    promotion_info = Column(String(255), default="")
    one_delivery = Column(Integer, default=0)
    pinyin_name = Column(String(255), default="")
    name_for_url = Column(String(255))
    min_deliver_amount = Column(Integer, default=0)
    close_description = Column(String(255), default="")
    is_saas = Column(Integer, default=0)
    header_image_url = Column(String(255), default="")
    waimai_num_print_copies = Column(Integer, default=1)
    tangchi_num_print_copies = Column(Integer, default=1)
    printer_version = Column(String(20), default="")
    napos_client_settings = Column(Text, default="")
    sn = Column(Integer, default=0)
    deliver_radius = Column(Integer, default=2500)
    min_lng = Column(Numeric(16, 13), default=0.0)
    max_lng = Column(Numeric(16, 13), default=0.0)
    min_lat = Column(Numeric(16, 13), default=0.0)
    max_lat = Column(Numeric(16, 13), default=0.0)
    is_bookable = Column(Integer, default=0)
    flavors = Column(String(255), default="")
    dine_enabled = Column(Integer, default=1)
    deliver_spent = Column(Integer, default=0)
    is_time_ensure = Column(Integer, default=0)
    time_ensure_description = Column(String(255), default="")
    # deprecated, will not use this field in the future
    time_ensure_at = Column(DateTime)
    time_ensure_spent = Column(Integer, default=0)
    time_ensure_discount = Column(String(10), default="")
    city_id = Column(Integer, default=1)
    is_phone_hidden = Column(Integer, default=1)
    coupon_enabled = Column(Integer, default=0)
    coupon_start_at = Column(DateTime)
    coupon_end_at = Column(DateTime)
    coupon_number = Column(Integer, default=0)
    coupon_discount = Column(Integer, default=0)
    paper_width = Column(String(50), default="58")
    auto_print_tangchi = Column(SmallInteger, default=1)
    speed_coef1 = Column(Float(7), default=0.0)
    speed_coef2 = Column(Float(7), default=0.0)
    speed_coef3 = Column(Float(7), default=0.0)
    avg_comment_time = Column(Float(7), default=0.0)
    activities = Column(String(255), default="")
    has_food_img = Column(Integer, default=0)
    online_payment = Column(Integer)
    invoice = Column(Integer, default=0)
    invoice_min_amount = Column(Numeric(10, 2), default=0)
    attribute = Column(Text, default="")
    deliver_area = Column(Text, default="")
    deliver_geojson = Column(Text, default="")
    open_date = Column(Date)
    original_order_quantity = Column(Float, default=0.0)
    keeper_name = Column(String, default="")
    keeper_phone = Column(String, default="")
    keeper_identity_card = Column(String, default="")
    remark = Column(Text, default="")
    corporation = Column(String, default="")
    geohash_ranking_weight = Column(Integer, default=0)
    wireless_printer_esn = Column(String, default="")
    open_time = Column(Binary, default=0)
    recent_food_popularity = Column(Integer, default=0)
    come_from = Column(SmallInteger, default=0)
    no_agent_fee_total = Column(SmallInteger, default=0)
    service_category = Column(SmallInteger, default=0)
    dock_corp_id = Column(Integer, default=0)
    recent_order_num = Column(Integer, default=0)
    has_activity = Column(SmallInteger, default=0)
    certification_type = Column(SmallInteger, default=0)

    @classmethod
    def get_empty_image_hash_restaurant(cls):
        return ZeusMySession().query(cls.id, cls.name).filter(
            cls.is_valid == True). \
            filter(cls.is_premium == True). \
            filter(cls.image_hash == '').all()