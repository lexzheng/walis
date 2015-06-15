#!/usr/bin/env python2
# coding=utf8

from __future__ import absolute_import, division, print_function
from contextlib import contextmanager
import functools

from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.declarative import declarative_base
from walis.core.db.mysql import make_commit_decorator
from walis import config

from walis.exception.util import raise_server_exc
from walis.exception.error_code import DATABASE_MYSQL_ERROR

engines = {}

for role, role_settings in config.MYSQL.items():
    role_url = ("mysql+pymysql://{user}:{passwd}@{host}:{port}/{database}"
                "?charset=utf8".format(**role_settings))
    engines[role] = create_engine(role_url,
                                  pool_size=10,
                                  max_overflow=-1,
                                  pool_recycle=1800)

from sqlalchemy.orm import scoped_session, sessionmaker
DBSession = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engines['master']))
# make_db_session(engines)

ModelBase = declarative_base()


class WalisModel(object):

    def to_dict(self):
        result = {}
        for key, value in self.__dict__.iteritems():
            if key.startswith('_'):
                continue
            result[key] = value
        return result


db_commit = make_commit_decorator(DBSession)


@contextmanager
def walis_session(commit=False):
    session = DBSession()
    try:
        yield session
        if commit:
            session.commit()
    except Exception as e:
        session.rollback()
        raise_server_exc(DATABASE_MYSQL_ERROR, exc=e)
    finally:
        session.close()


def walis_db_handler(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        session = DBSession()
        func.func_globals['session'] = session
        try:
            ret = func(*args, **kwargs)
        except SQLAlchemyError as se:
            session.rollback()
            raise_server_exc(DATABASE_MYSQL_ERROR, exc=se)
        except Exception as e:
            session.rollback()
            raise_server_exc(DATABASE_MYSQL_ERROR, exc=e)
        finally:
            session.close()
            func.func_globals.pop('session')
        return ret
    return wrapper
