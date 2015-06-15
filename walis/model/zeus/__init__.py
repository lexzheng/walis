#!/usr/bin/env python2
# coding=utf8

from __future__ import absolute_import, division, print_function
from contextlib import contextmanager
import functools

from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from walis.exception.util import raise_zeus_exc
from walis.exception.error_code import ZEUS_DATABASE_ERROR

from walis import config

ModelBase = declarative_base()
engines = {}

zeus_my_url = ("mysql+pymysql://{user}:{passwd}@{host}:{port}/{database}"
               "?charset=utf8".format(**config.ZEUS_SLAVE_MYSQL_SETTINGS))
mysql_engine = create_engine(zeus_my_url,
                             pool_size=10,
                             max_overflow=-1,
                             pool_recycle=1800)

ZeusMySession = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=mysql_engine))


@contextmanager
def zeus_session():
    session = ZeusMySession()
    try:
        yield session
        session.commit()
    except Exception as e:
        session.rollback()
        raise_zeus_exc(ZEUS_DATABASE_ERROR, exc=e)
    finally:
        session.close()


def zeus_db_handler(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        session = ZeusMySession()
        func.func_globals['session'] = session
        try:
            ret = func(*args, **kwargs)
        except SQLAlchemyError as se:
            session.rollback()
            raise_zeus_exc(ZEUS_DATABASE_ERROR, exc=se)
        except Exception as e:
            session.rollback()
            raise_zeus_exc(ZEUS_DATABASE_ERROR, exc=e)
        finally:
            session.close()
            func.func_globals.pop('session')
        return ret
    return wrapper

