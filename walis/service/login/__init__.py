#!/usr/bin/env python2
# coding=utf8

from __future__ import absolute_import, division, print_function

from flask import request
from flask.ext.login import (
    LoginManager,
    login_required,
)

from .model import WalisUser
from walis import config
from walis.utils.format import to_int


login_manager = LoginManager()


def login_init(app):
    """ Init login module
    """
    login_manager.login_view = "LoginApi:get"
    login_manager.init_app(app)

    if not config.LOGIN['enabled']:
        return

    endpoint_list = filter(
        lambda endpoint: endpoint not in config.LOGIN['exclude'],
        app.view_functions.keys()
    )

    # add login deco for each view_func
    for ep in endpoint_list:
        app.view_functions[ep] = login_required(app.view_functions[ep])


@login_manager.user_loader
def load_user(uid):
    user_id = None
    # todo 计算token
    if request.cookies.get('god_token'):
        user_id = to_int(request.cookies.get('god_uid'), return_none=True)
    if user_id is None:
        return WalisUser.get_user(request.cookies.get('SSO_TOKEN'))

    return WalisUser(user_id)


@login_manager.token_loader
def load_user(sso_id):
    #todo 计算token
    if request.cookies.get('god_token'):
        uid = request.cookies.get('god_uid')
        if uid:
            try:
                user = WalisUser(int(uid))
                return user
            except:
                pass
    sso_id = request.cookies.get('SSO_TOKEN', None)
    return WalisUser.get_user(sso_id)
