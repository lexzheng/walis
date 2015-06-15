# coding=utf8

HTTP_SYS_ERROR_CODE = 500
HTTP_AUTH_ERROR_CODE = 403
HTTP_BAD_REQUEST = 400


class WalisExc(Exception):

    def __init__(self, id=None, type=None, code=None, msg=None):
        self.id = id
        self.type = type
        self.code = code
        self.msg = msg

    def __str__(self):
        return self.msg


class BadRequestExc(WalisExc):

    def __init__(self, msg):
        super(BadRequestExc, self).__init__(
            type='user_exc', id=id, code=HTTP_BAD_REQUEST, msg=msg)


class UserExc(WalisExc):

    def __init__(self, id, msg, code=HTTP_BAD_REQUEST):
        super(UserExc, self).__init__(
            type='user_exc', id=id, code=code, msg=msg)


class AuthExc(WalisExc):

    def __init__(self):
        super(AuthExc, self).__init__(
            type='auth_exc', code=HTTP_AUTH_ERROR_CODE,
            msg='Do not have auth to access this api')


class SysExc(WalisExc):

    def __init__(self, id, msg, source='Walis', code=HTTP_SYS_ERROR_CODE):
        super(SysExc, self).__init__(
            type='sys_exc', id=id, code=code, msg=msg)
        self.source = source

    def __str__(self):
        return '{} from {} {} {}'.format(type, self.source, self.code, self.msg)


class ZeusExc(SysExc):

    def __init__(self, id, msg, code=HTTP_SYS_ERROR_CODE):
        super(ZeusExc, self).__init__(
            id, msg, source='zeus', code=code)


# Common Used exceptions
ERR_ON_DB_COMMIT = SysExc(100200, 'Error on database commit', code=HTTP_SYS_ERROR_CODE)


EXC_ID_MAP = {
    # 0~100 reserved

    # 101~200: restaurant

    # 201~300: activity

    # 301~400: order

    # 401~500: user

    # 1000~1050: voicecall
    1000: 'voicecall exceed limit error',
    1001: 'voice call "{}" not found error',
}