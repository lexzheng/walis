#!/usr/bin/env python2
# coding=utf8

from __future__ import absolute_import, division, print_function
import xlwt

from walis.exception.util import raise_user_exc
from walis.exception.error_code import FORMAT_ERR

def to_int(something, silence=True, return_none=False):
    """
    transform to int silently.
    return: int if ok
            None if error.
    """
    error = False
    try:
        return int(something)
    except TypeError:
        error = True
        raise_user_exc(FORMAT_ERR, src_type='None', target_type="Int")
    except ValueError:
        error = True
        raise_user_exc(FORMAT_ERR, src_type=something, target_type="Int")
    except Exception:
        error = True
        raise_user_exc(FORMAT_ERR, src_type=something, target_type="Int")
    finally:
        if error and silence:
            if return_none:
                return None
            return something


def to_float(something, silence=True):
    """
    transform to int silently.
    return: int if ok
            None if error.
    """
    error = False
    try:
        return float(something)
    except TypeError:
        error = True
        raise_user_exc(FORMAT_ERR, src_type='None', target_type="Float")
    except ValueError:
        error = True
        raise_user_exc(FORMAT_ERR, src_type=something, target_type="Float")
    except Exception:
        error = True
        raise_user_exc(FORMAT_ERR, src_type=something, target_type="Float")
    finally:
        if error and silence:
            return None


def set_null(obj, attributes):
    """
    Set `attributes` in `obj` null if it does not exist.
    In order to make api arguments stay the same pattern.
    """
    if type(obj) in (list, tuple):
        for o in obj:
            set_null(o, attributes)
    elif type(obj) is dict:
        for attr in attributes:
            if obj.get(attr) is None:
                obj[attr] = None
    return obj


def generate_excel(data_list, sheet_name='sheet', columns=None):
    if not data_list:
        return None

    work_book = xlwt.Workbook()
    work_sheet = work_book.add_sheet(sheet_name)

    # set column name
    if columns and type(columns) in (list, tuple):
        column_keys = [col[0] for col in columns]
        for col, column in enumerate(columns):
            work_sheet.write(0, col, columns[col][1])
    else:
        column_keys = data_list[0].keys()
        for col, col_name in enumerate(data_list[0].keys()):
            work_sheet.write(0, col, col_name)

    # set content
    for row, data in enumerate(data_list):
        for col, col_key in enumerate(column_keys):
            work_sheet.write(row+1, col, data.get(col_key))

    return work_book
