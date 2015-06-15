#!/usr/bin/env python2
# coding=utf8

from __future__ import absolute_import, division, print_function

from datetime import datetime


JOB_SETTINGS = {
    #################
    # Voicecall job_deco
    #################
    'voiceorder_job': {
        'func': 'voicecall.voiceorder_job',
        'trigger': 'interval',
        'seconds': 15,
    },
    'voicecall_job': {
        'func': 'voicecall.voicecall_job',
        'trigger': 'interval',
        'seconds': 3,
    },
    'voicecall_ban_daily_clean_job': {
        'func': 'voicecall.voicecall_ban_daily_clean_job',
        'trigger': 'interval',
        'days': 1,
        'start_date': datetime.now().replace(hour=23, minute=59, second=0)
    },
    #############
    # order job_deco
    #############
    'process_order': {
        'func': 'process_order.process_order',
        'trigger': 'interval',
        'seconds': 1,
    },
    ##################
    # pay notice job_deco
    ##################
    'notice_activity_pay': {
        'func': 'notice_activity_pay.notice_activity_pay',
        'trigger': 'interval',
        'seconds': 30,
    },

    ##################
    # restaurant job_deco
    ##################
    'clean_rst_director': {
        'func': 'clean_rst_director.clean_rst_director',
        'trigger': 'cron',
        'hour': '22',
        'minute': '30',
    },
    'notice_unwatched_rst': {
        'func': 'notice_unwatched_rst.notice_unwatched_rst',
        'trigger': 'cron',
        'hour': '23',
        'minute': '00'
    }
}

