# coding=utf8

import time
import logging.config
from walis import config

from werkzeug.exceptions import BadRequest

""" Logging for walis API framework
"""


class ModuleFilter(logging.Filter):
    def filter(self, record):
        exclude = ('werkzeug',)
        if record.name in exclude:
            return False
        else:
            return True


class RPCFilter(logging.Filter):
    def filter(self, record):
        include = ('requests', 'bluelake')
        for filed in include:
            if record.name.startswith(filed):
                return True
        else:
            return False


def logger_init():
    logging.config.dictConfig(config.LOGGING)


def get_request_args(ctx, include=None, exclude=None):
    default_include = ('args', 'json', 'form', 'data')
    if include is None:
        include = default_include
    if exclude is not None:
        include = include - exclude

    args_dict = {}
    if 'args' in include:
        if ctx.req.args:
            args_dict['args'] = ctx.req.args.to_dict()
    if 'json' in include:
        try:
            if ctx.req.json:
                args_dict['json'] = ctx.req.json
        except BadRequest:
            pass
    if 'form' in include:
        if ctx.req.form:
            args_dict['form'] = ctx.req.form
    if 'data' in include:
        if ctx.req.data:
            args_dict['data'] = ctx.req.data
    return args_dict


def log_info(ctx):
    log = logging.getLogger(name=ctx.module)
    timed = (time.time() - ctx.started_at) * 1000  # ms
    url = ctx.req.url[len(ctx.req.url_root) - 1:]

    req_data = get_request_args(ctx)

    fmt = ('API {ctx.response.status_code} {ctx.req.method} {ctx.module}.{call}'
           ' => {url} => {req_data} => '
           '{timed:.3f}ms')
    return log.info(fmt.format(ctx=ctx, call=ctx.func.__name__, url=url,
                               timed=timed, req_data=req_data))


def log_warn(ctx):
    log = logging.getLogger(name=ctx.module)
    url = ctx.req.url[len(ctx.req.url_root) - 1:]
    req_data = get_request_args(ctx)

    fmt = ('API {ctx.response.status_code} {ctx.req.method} {ctx.module}.{call}'
           ' => {url} => {req_data}')
    return log.warn(fmt.format(ctx=ctx, call=ctx.func.__name__, url=url,
                               req_data=req_data), exc_info=True)


def log_error(ctx):
    log = logging.getLogger(name=ctx.module)
    url = ctx.req.url[len(ctx.req.url_root) - 1:]
    req_data = get_request_args(ctx)

    fmt = ('API {ctx.response.status_code} {ctx.req.method} {ctx.module}.{call}'
           ' => {url} => {req_data}')
    return log.error(fmt.format(ctx=ctx, call=ctx.func.__name__, url=url,
                                req_data=req_data), exc_info=True)
