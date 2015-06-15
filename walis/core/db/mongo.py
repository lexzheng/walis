#! /usr/bin/env python2
# -*- coding:utf-8 -*-

import pymongo
from walis import config


mongo = None


def mongo_init():
    global mongo
    url = config.MONGO['url']
    client = pymongo.MongoClient(url, tz_aware=False)
    mongo = client[config.MONGO['database']]

mongo_init()
