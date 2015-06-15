# coding=utf8

import pytest
from walis.server import app


@pytest.fixture
def web_client():
    with app.test_client() as client:
        return client
