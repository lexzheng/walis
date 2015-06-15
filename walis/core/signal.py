# coding=utf8
# flake8: noqa

from blinker import signal

sig_call_done = signal(2000)
sig_call_ok = signal(2001)
sig_call_user_exc = signal(2002)
sig_call_sys_exc = signal(2003)
sig_call_unexcepted_exc = signal(2004)

import log
import monitor


def reg_signals():
    # logging
    sig_call_ok.connect(log.log_info)
    sig_call_user_exc.connect(log.log_warn)
    sig_call_sys_exc.connect(log.log_error)
    sig_call_unexcepted_exc.connect(log.log_error)
    # misc stats
    sig_call_user_exc.connect(monitor.stats_count_user_exc)
    sig_call_sys_exc.connect(monitor.stats_count_sys_exc)
    sig_call_unexcepted_exc.connect(monitor.stats_count_unexcepted_exc)
    sig_call_done.connect(monitor.stats_timing)
