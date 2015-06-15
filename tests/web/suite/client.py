# coding=utf8

from __future__ import absolute_import, division, print_function
import pytest
from walis.server import app


# TODO 在每个模块conftest中使用权限检查
# web_client.set_cookie('eleme.test', 'god_token', 'true')
# web_client.set_cookie('eleme.test', 'god_uid', '485388')
# web_client.set_cookie('eleme.test', 'user_id', '485388')

@pytest.fixture(scope="session", autouse=True)
def web_client():
    with app.test_client() as client:
        client.set_cookie(
            '',
            'SID',
            value='GOmrIgCkWQx8Y4FJPxAxFUP75RKSB1XYUa4A'
        )
        response = client.get('/api/ping', buffered=True)
        assert response.status_code == 200

        response = client.get('/api/login', buffered=True)
        assert response.status_code == 200

        return client
