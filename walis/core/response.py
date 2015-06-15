# coding=utf8
from functools import wraps
import tempfile

from flask import (
    make_response,
    Response,
    send_file)
import jsonpickle
from werkzeug.wrappers import Response as wResponse

from walis.exception import WalisExc


def make_res(obj):
    """Make a flask response on call ok, `obj` is a flask/werkzeug response or
    an object that can be jsonified."""
    if isinstance(obj, (Response, wResponse)):
        return obj
    return make_response(jdumps(obj))


def make_excel_res(content):

    temp_file = tempfile.TemporaryFile()
    temp_file.write(content)

    temp_file.seek(0)
    response = send_file(temp_file, as_attachment=True,
                         mimetype='application/vnd.ms-excel',
                         add_etags=False)
    return response


def make_exc_res(exc):
    """Make flask response on call exc (sys_exc or user_exc or unexcepted_exc),
    `exc` is the exception object."""

    if isinstance(exc, WalisExc):
        dct = dict(error_code=exc.error_code, type=exc.type, msg=exc.msg)
        return make_response(jdumps(dct), exc.http_code)
    else:
        dct = dict(msg='{exc!s}'.format(exc=exc), type='unknown_exc')
        return make_response(jdumps(dct), getattr(exc, 'code', 500))


def make_no_permission_res():
    return make_response(jdumps('No permission for this Api!'), 403)


def jdumps(obj):
    return jsonpickle.encode(obj, unpicklable=False)


def jloads(string, **kwargs):
    return jsonpickle.decode(string, **kwargs)


def headers(header_dict):
    """This decorator adds the headers passed in to the response"""
    _header_dict = header_dict.copy()

    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            resp = make_response(f(*args, **kwargs))
            h = resp.headers
            for header, value in _header_dict.items():
                h[header] = value
            return resp

        return decorated_function

    return decorator


json_header = headers({'Content-Type': 'application/json'})
