#!/usr/bin/env python2
# coding=utf8

from __future__ import absolute_import, division, print_function

import json
from flask import session
from flask.ext.login import login_user
from walis.server import app
from walis.service.login import WalisUser

cookies = {'SID': u'Y6cq6mrex5Z0lSJ3teSIwWxgEAKf0YR21jhg'}


#
# def test_create(web_client):
#     data
#     response = web_client.post('/api/cs/event',
#                                headers=headers,
#                                cookies=cookies,
#                                data=data)
#     assert response.status_code == 200
#     assert isinstance(json.loads(response.data)['id'], int)
def test_login():
    user = WalisUser(485388)
    login_user(user)


headers = [('Content-Type', 'application/json')]
def test_get_event(web_client):

    with app.test_client() as web_client:
        response = web_client.get('/api/ping', buffered=True)
        assert response.status_code == 200

        web_client.set_cookie('', 'SID',
                              value='GOmrIgCkWQx8Y4FJPxAxFUP75RKSB1XYUa4A')

        response = web_client.get('/api/login', buffered=True)
        print(response.status_code)
        assert response.status_code == 200

        # test_login()
        # web_client.set_cookie('eleme.test', 'god_token', 'true')
        # web_client.set_cookie('eleme.test', 'god_uid', '485388')
        # web_client.set_cookie('eleme.test', 'user_id', '485388')
        # session['user_id'] = 485388
        response = web_client.get('/api/banner/get_user_city_ids',
                                  headers=headers, buffered=True)
        print(response.status_code)
        assert response.status_code == 200
        print(response.data)


test_get_event(1)