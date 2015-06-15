#!/usr/bin/env python2
# coding=utf8

from __future__ import absolute_import, division, print_function
from walis.utils.secret import md5


service_addr = 'javis.ele.me'

# voice call's sending url
voicecall_url = 'http://yyy-sh2.ti-net.com/interface/entrance/OpenInterfaceEntrance'

# voice call's async result receiver url
callback_url = ''.join(
    ['http://', service_addr, '/app/voicecall/async_result'])

# voice call's back keys receiver url
keysback_url = ''.join(
    ['http://', service_addr, '/app/voicecall/keysback'])

# voice call's end signal url
endcall_url = ''.join(
    ['http://', service_addr, '/app/voicecall/call_end'])

# voice call's parameters
call_settings = {'interfaceType': 'webCall',
               'enterpriseId': '3000006',
               'userName': 'admin',
               'pwd': md5('948492695'),  # 'ac4b80af185d1964d8bf43fe89ea9f07'
               'sync': '0',
               'ivrId': '22',
               'callbackUrl': callback_url,
}

# interval of collecting unprocessed orders
voice_order_interval = 15  # unit: seconds
# interval of sending voice calls
voice_call_interval = 3  # unit: seconds

# how long do we send voice call since ordered
send_vc_deadline = 1 * 60  # unit: seconds

# include or exclude restaurant ids
write_list = [59, 320]
black_list = []
