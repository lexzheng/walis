# coding=utf8

import time
from statsd import StatsClient


# ------------ statsd  ------------------------------------------------
from walis import config


statsd = None


def statsd_init():
    global statsd
    statsd = StatsClient(
        config.STATSD['host'],
        config.STATSD['port'],
        prefix=config.STATSD['prefix']
    )


def stats_timing(ctx):
    fmt = '{ctx.module}.{ctx.func.__name__}'
    return statsd.timing(fmt.format(ctx=ctx),
                         (time.time() - ctx.started_at) * 1000)


def stats_count_user_exc(ctx):
    fmt = '{ctx.module}.{ctx.func.__name__}.user_exc'
    return statsd.incr(fmt.format(ctx=ctx))


def stats_count_sys_exc(ctx):
    fmt = '{ctx.module}.{ctx.func.__name__}.sys_exc'
    return statsd.incr(fmt.format(ctx=ctx))


def stats_count_unexcepted_exc(ctx):
    fmt = '{ctx.module}.{ctx.func.__name__}.unexcepted_exc'
    return statsd.incr(fmt.format(ctx=ctx))
