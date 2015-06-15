__author__ = 'superlion'


from flask.ext.login import current_user
from walis.exception.util import raise_auth_exc
from walis.exception.error_code import AUTH_UTP_FAILED_ERROR


def deco_check_is_rst_owner(func):
    def wrapper(restaurant_id):
        restaurant_id = int(restaurant_id)
        if not current_user.utp_is_restaurant_owner(restaurant_id):
            raise_auth_exc(AUTH_UTP_FAILED_ERROR)
        return func(restaurant_id)
    return wrapper


def check_is_rst_owner(restaurant_id):
    restaurant_id = int(restaurant_id)
    if not current_user.utp_is_restaurant_owner(restaurant_id):
        raise_auth_exc(AUTH_UTP_FAILED_ERROR)
