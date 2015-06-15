#!/usr/bin/env python2
# coding=utf8

from __future__ import absolute_import, division, print_function

from easydict import EasyDict

from walis.utils.http import jsonpickle_loads, jsonpickle_dumps


def any_to_raw(any):
    return jsonpickle_loads(jsonpickle_dumps(any))


def any_to_dic(any):
    return any_to_raw(any)

def dic_fields_process(dic,includes=None,excludes=None):
    fields = dic.keys()
    # 先白后黑
    if includes is not None:
        excludes = set(fields) - set(includes)
    if excludes is not None:
        [dic.pop(field,None) for field in excludes]
    return dic


from thriftpy.thrift import TPayloadMeta
def dic_to_tobj(dic,tobj_or_ttype,follow_spec=False):
    #todo 支持ttype
    if isinstance(tobj_or_ttype,TPayloadMeta):
        tobj = tobj_or_ttype()
    else:
        tobj = tobj_or_ttype
    for k,v in dic.iteritems():
        if k in tobj.__dict__.keys():
            setattr(tobj,k,v)
    if follow_spec:
        tobj_follow_spec(tobj)
    return tobj


def getresult_to_raw(getresult):
    if isinstance(getresult, (tuple,list)):
        return [EasyDict(any_to_raw(item)) for item in getresult]
    else:
        return EasyDict(any_to_raw(getresult))


def tobj_follow_spec(tobj):
    spec = tobj.thrift_spec
    fields = []
    for index,field in spec.iteritems():
        if len(field)==3:
            field_type,field_name,other = field #return 3 para ,like (6, 'is_map', True)
        else:
            field_type,field_name=field
        fields.append(field_name)
    for k in tobj.__dict__.keys():
        if k not in fields:
            tobj.__dict__.pop(k,None)
    return tobj

def always_list(pk_or_pks):
    if isinstance(pk_or_pks, (tuple,list)):
        result = pk_or_pks
    else:
        result = [pk_or_pks, ]
    return result


def object2dict(_object, exclude=None):

    if type(_object) in (list, tuple, set):
        result = []
        for _o in _object:
            tmp = {}
            for name, value in _o.__dict__.items():
                if exclude and name not in set(exclude):
                    continue
                tmp[name] = value

            result.append(tmp)
    else:
        result = {}
        for name, value in _object.__dict__.items():
            if exclude and name not in set(exclude):
                continue
            result[name] = value

    return result


def dict2object(value_d, _object, exclude=None):

    for name, value in value_d.items():
        if exclude and name in exclude:
            continue

        setattr(_object, name, value)

    return _object


def ttype2dict(ttype, keys=None):
    keys_set = []
    maps = {}
    if keys:
        keys_set = set(keys)

    for key, value in ttype.__dict__.items():
        if keys_set and key not in keys_set:
            continue
        maps[key] = value
    return maps
