# -*- coding:utf-8 -*-

from __future__ import division, print_function, absolute_import

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from walis.core.db.mysql import make_commit_decorator

from walis import config


engines = {}

walle_my_url = ("mysql+pymysql://{user}:{passwd}@{host}:{port}/{database}"
               "?charset=utf8".format(**config.WALLE_ANALYTICS))

transaction_pg_url = ("postgresql+psycopg2://{user}:{passwd}@{host}:{port}"
                      "/{database}".format(**config.TRANSACTION_PG))


mysql_engine = create_engine(walle_my_url,
                             pool_size=10,
                             max_overflow=-1,
                             pool_recycle=1800)

pg_engine = create_engine(transaction_pg_url,
                          pool_size=10,
                          max_overflow=-1,
                          pool_recycle=1800)

WDBSession = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=mysql_engine))

PGSession = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=pg_engine))

walle_db_commit = make_commit_decorator(WDBSession)
