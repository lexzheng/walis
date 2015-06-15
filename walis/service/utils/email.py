#! /usr/bin/env python2
# -*- coding:utf-8 -*-

from walis.thirdparty import thrift_client

def send(sender, receiver, title, content):
    with thrift_client('ees') as ees:
        ees.send(sender, receiver, title, content)

def msend(sender, receivers, title, content):
    with thrift_client('ees') as ees:
        ees.msend(sender, receivers, title, content)