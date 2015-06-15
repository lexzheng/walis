#!/usr/bin/env python2
# -*- coding: utf8 -*-

from __future__ import absolute_import, division, print_function


class RestaurantConst(object):

    # trade record api status
    TR_ARRIVED_INCOME = 0
    TR_COMING_INCOME = 1
    # trade record zeus status
    TR_PROCESSING = 0
    TR_SUCCESS = 1

    # withdraw api status
    WD_API_UNPROCESSED = 0
    WD_API_SUMMITTED = 1
    WD_API_SUCCESS = 2
    WD_API_FAIL = 3
    # withdraw zeus status
    WD_ZEUS_UNPROCESSED = 1
    WD_ZEUS_GENERATED = 2
    WD_ZEUS_SUBMITTED = 3
    WD_ZEUS_SUCCESS = 4
    WD_ZEUS_WARNING_FAIL = 5
    WD_ZEUS_FATAL_FAIL = 6

    @classmethod
    def _withdraw_status_map(cls, map_direction, status):
        if map_direction == 'api2zeus':
            status_map = {
                cls.WD_API_UNPROCESSED: [cls.WD_ZEUS_UNPROCESSED, ],
                cls.WD_API_SUMMITTED: [cls.WD_ZEUS_GENERATED,
                                       cls.WD_ZEUS_SUBMITTED],
                cls.WD_API_SUCCESS: [cls.WD_ZEUS_SUCCESS, ],
                cls.WD_API_FAIL: [cls.WD_ZEUS_WARNING_FAIL,
                                  cls.WD_ZEUS_FATAL_FAIL]
            }
            return status_map[status]

        elif map_direction == 'zeus2api':
            status_map = {
                cls.WD_ZEUS_UNPROCESSED: cls.WD_API_UNPROCESSED,
                cls.WD_ZEUS_GENERATED: cls.WD_API_SUMMITTED,
                cls.WD_ZEUS_SUBMITTED: cls.WD_API_SUMMITTED,
                cls.WD_ZEUS_SUCCESS: cls.WD_API_SUCCESS,
                cls.WD_ZEUS_WARNING_FAIL: cls.WD_API_FAIL,
                cls.WD_ZEUS_FATAL_FAIL: cls.WD_API_FAIL
            }
            return status_map[status]

        return None

    # balance change api trade typs
    TT_API_CHARGE = 1
    TT_API_CONSUME = 2
    TT_API_WITHDRAW = 3
    TT_API_BONUS = 4
    TT_API_CONTRACT = 5
    TT_API_INVALID_INCOME = 6
    TT_API_OTHERS = 99
    # balance change zeus trade types
    TT_ZEUS_CHARGE = 0
    TT_ZEUS_CONSUME = 1
    TT_ZEUS_PRODUCE = 2
    TT_ZEUS_REFUND = 3
    TT_ZEUS_WITHDRAW_APPLY = 4
    TT_ZEUS_WITHDRAW_FAIL = 5
    TT_ZEUS_BONUS = 6
    TT_ZEUS_DRAWBACK = 7
    TT_ZEUS_PAY_AUTO_FAIL = 8
    TT_ZEUS_DIRECT_CONSUME = 9
    TT_ZEUS_CONTRACT = 10
    TT_ZEUS_INVALID_INCOME = 11
    TT_ZEUS_ANONYMOUS_DRAWBACK = 12
    TT_ZEUS_ANONYMOUS_REFUND = 13
    TT_ZEUS_BONUS_DRAWBACK = 14
    TT_ZEUS_CONTRACT_REFUND = 15

    @classmethod
    def _balance_change_status_map(cls, map_direction, status):
        """
        Zeus UserBalanceChange 状态列表：

        0 | TRADE_TYPE_CHARGE | 充值
        1 | TRADE_TYPE_CONSUME | 消费（使用余额支付）
        2 | TRADE_TYPE_PRODUCE | 订单收入*
        3 | TRADE_TYPE_REFUND | 用户退单*
        4 | TRADE_TYPE_WITHDRAW_APPLY | 餐厅提现
        5 | TRADE_TYPE_WITHDRAW_FAIL | 餐厅提现失败*
        6 | TRADE_TYPE_BONUS | 用户充值奖励
        7 | TRADE_TYPE_DRAWBACK | 用户提现*
        8 | TRADE_TYPE_PAY_AUTO_FAIL | 支付超时*
        9 | TRADE_TYPE_DIRECT_CONSUME | 消费*（使用第三方支付）
        10 | TRADE_TYPE_CONTRACT | 餐厅合同充值（SAAS）
        11 | TRADE_TYPE_INVALID_INCOME | 餐厅无效收入（用户退单）
        12 | TRADE_TYPE_ANONYMOUS_DRAWBACK | 匿名提现*
        13 | TRADE_TYPE_ANONYMOUS_REFUND | 匿名退款*
        14 | TRADE_TYPE_BONUS_DRAWBACK | 充值奖励无效退款*
        15 | TRADE_TYPE_CONTRACT_REFUND | 餐厅合同退款（SAAS）*
        """
        if map_direction == 'api2zeus':
            status_map = {
                cls.TT_API_CHARGE: [cls.TT_ZEUS_CHARGE, ],
                cls.TT_API_CONSUME: [cls.TT_ZEUS_CONSUME,
                                     cls.TT_ZEUS_DIRECT_CONSUME],
                cls.TT_API_BONUS: [cls.TT_ZEUS_BONUS, ],
                cls.TT_API_CONTRACT: [cls.TT_ZEUS_CONTRACT, ],
                cls.TT_API_INVALID_INCOME: [cls.TT_ZEUS_INVALID_INCOME, ],
                cls.TT_API_OTHERS: [cls.TT_ZEUS_REFUND,
                                    cls.TT_ZEUS_WITHDRAW_FAIL,
                                    cls.TT_ZEUS_DRAWBACK ,
                                    cls.TT_ZEUS_PAY_AUTO_FAIL,
                                    cls.TT_ZEUS_ANONYMOUS_DRAWBACK,
                                    cls.TT_ZEUS_ANONYMOUS_REFUND,
                                    cls.TT_ZEUS_BONUS_DRAWBACK,
                                    cls.TT_ZEUS_CONTRACT_REFUND],
            }
            return status_map[status]

        elif map_direction == 'zeus2api':
            status_map = {
                cls.TT_ZEUS_CHARGE: cls.TT_API_CHARGE,
                cls.TT_ZEUS_CONSUME: cls.TT_API_CONSUME,
                cls.TT_ZEUS_DIRECT_CONSUME: cls.TT_API_CONSUME,
                cls.TT_ZEUS_BONUS: cls.TT_API_BONUS,
                cls.TT_ZEUS_CONTRACT: cls.TT_API_CONTRACT,
                cls.TT_ZEUS_INVALID_INCOME: cls.TT_API_INVALID_INCOME
            }
            return status_map.get(status, cls.TT_API_OTHERS)

        return None