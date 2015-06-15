# coding=utf8
#!/usr/bin/env python

from __future__ import division, print_function

from flask.ext.login import (
    login_required,
    login_user,
    logout_user,
    login_url
)

from flask import (
    redirect,
    Response,
    request,
    url_for,
    make_response,
)

from .model import WalisUser
from walis import config
from walis.core.api import WalisView, api
from walis.thirdparty.coffee import coffee


class LoginApi(WalisView):
    route_base = 'login'

    def get(self):
        sid = request.cookies.get('SSO_TOKEN', None)
        if not sid:
            return self._sso_login()
        user = WalisUser.get_user(sid)
        if not user:
            return self._sso_login()
        login_user(user, remember=True)
        # return Response('login ok.', 200)
        # return make_response('login required.', 401)
        origin_url = self._get_origin_url()
        return redirect(origin_url)


    @api('/sso_login_resp')
    def set_sso_login_token(self):
        token = request.args.get('token')
        if coffee.sso.checkToken(access_token=token):
            response = Response('{code : "ok"}')
            response.set_cookie('SSO_TOKEN', token)
        else:
            response = Response('{code : "error"}')
        return response


    @classmethod
    def _sso_login(cls):
        return make_response('login required.', 401)
        # next_url = cls._get_origin_url()
        # sso_login_url = login_url(
        #     config.LOGIN['sso_login_url'], next_url, 'redirect')
        # return redirect(sso_login_url)

    @staticmethod
    def _get_origin_url():
        origin_url = request.args.get('next', '')
        if not origin_url.startswith('http'):
            origin_url = '{base}{next}'.format(
                base='',
                next=origin_url.lstrip('/'))
            return origin_url

    @login_required
    @api('logout')
    def logout(self):
        # TODO use walle sso logout
        logout_user()
        return redirect(url_for('/'))

    @login_required
    @api('/switch_user/<int:uid>')
    def switch_user(self, uid):
        # todo 设置一个token.当开启自动计算时,自动计算token.否则需要手动提供token
        # 开启自动计算功能通过运行时修改配置达到-.-
        # if not current_user.is_super_admin():
        #     abort(404)
        response = Response('switch user to {}'.format(uid))
        response.set_cookie('god_token', 'true')
        response.set_cookie('god_uid', str(uid))
        return response


    # @login_bp.route('/app/switch_user_off')
    @login_required
    @api('/switch_user_off')
    def switch_user_off(self):
        # todo 设置一个token.当开启自动计算时,自动计算token.否则需要手动提供token
        # 开启自动计算功能通过运行时修改配置达到-.-
        response = Response('switch user off')
        response.delete_cookie('god_token')
        response.delete_cookie('god_uid')
        return response