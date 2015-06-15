#!/usr/bin/env python2
# -*- coding: utf8 -*-

from __future__ import absolute_import, division, print_function
import json

from flask import request
from flask.ext.login import current_user
from webargs import Arg

from walis.service.rst import recruit as recruit_base
from walis.model.walis import DBSession, db_commit
from walis.model.walis.rst import RestaurantRecruitment
from walis.utils.http import args_parser


def get_by_user():
    user_id = current_user.id

    args_spec = {
        'status': Arg(int, allow_missing=True),
        'page_no': Arg(int, allow_missing=True),
        'page_size': Arg(int, allow_missing=True),
    }
    args = args_parser.parse(args_spec, request)
    status = args.get('status', None)
    # offset, limit = get_paging_params(db_style=True)

    recruits = recruit_base.get_by_uid(
        user_id,
        status,
        (args['page_no']-1) * args.get('page_size', 30),
        args.get('page_size', 30)
    )
    count = recruit_base.count_by_uid(user_id, status)

    return {
        'recruits': recruit_base.pack_recruits(recruits),
        'total_num': count,
    }


@db_commit
def put():
    recruit_ids = [int(_id) for _id in
                   json.loads(request.data).get("id_list")]
    status_to = int(json.loads(request.data).get("status"))
    session = DBSession()
    recruits = session.query(RestaurantRecruitment).filter(
        RestaurantRecruitment.id.in_(recruit_ids)).all()
    for recruit in recruits:
        recruit.status = status_to
    return ''
