#! /usr/bin/env python2
# -*- coding:utf-8 -*-

import functools

from flask import _request_ctx_stack
from sqlalchemy.orm.session import Session
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.exc import SQLAlchemyError

from walis.exception.util import raise_dev_exc, raise_server_exc
from walis.exception.error_code import DATABASE_UNKNOWN_ERROR, DEV_ARGS_ERR

try:
    from flask import _app_ctx_stack
except ImportError:
    _app_ctx_stack = None

# _app_ctx_stack is new in flask@0.9
ctx_stack = _app_ctx_stack or _request_ctx_stack


def scope_func():
    return ctx_stack.__ident_func__


#############################################################
#########################  Mysql  ###########################
#############################################################
class RoutingSession(Session):
    def __init__(self, *args, **kwargs):
        super(RoutingSession, self).__init__()
        self.engines = kwargs.pop('engines', None)
        if self.engines is None:
            raise_dev_exc(DEV_ARGS_ERR, args="engines")

    def get_bind(self, mapper=None, clause=None):
        _name = getattr(self, '_name', None)

        if _name is not None:
            return self.engines[_name]
        elif self._flushing:
            return self.engines['master']
        else:
            return self.engines.get('slave', self.engines['master'])

    def using_bind(self, name):
        self._name = name
        return self


def make_db_session(engines, scopefunc=None):
    """Make a db session::

        DBSession = make_db_session(engines)
        session = DBSession()  # master/slave
        session = DBSession().using_bind('master')  # using master
    """
    if scopefunc is None:
        scopefunc = scope_func
    return scoped_session(sessionmaker(
        class_=RoutingSession,
        expire_on_commit=False,
        engines=engines), scopefunc=scopefunc)


def make_commit_decorator(DBSession, bind=None, commit_exc=None):
    """Make a decorator to commit session::

        DBSession = make_db_session(engines)
        defer_commit = make_commit_decorator(DBSession)

        @defer_commit
        def do_things():
            pass
    """

    def decorated(func):
        @functools.wraps(func)
        def func_(*args, **kwargs):
            returned = func(*args, **kwargs)
            session = DBSession()#.using_bind(bind)
            try:
                session.commit()
            except SQLAlchemyError as e:
                session.rollback()
                raise_server_exc(DATABASE_UNKNOWN_ERROR, exc=e)
            return returned

        return func_

    return decorated


def do_commit(func):
    """ database session commit decorator """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        ret = func(*args, **kwargs)
        session = Session()
        # tmp
        session._model_changes = {}
        try:
            session.commit()
        except SQLAlchemyError as se:
            session.rollback()
            raise_server_exc(DATABASE_UNKNOWN_ERROR, exc=se)
        finally:
            session.close()
        return ret

    return wrapper
