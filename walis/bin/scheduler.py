#!/usr/bin/env python2
# coding=utf8

from __future__ import absolute_import, division, print_function
from walis.core.log import logger_init
from walis.scheduler import jobs_register, scheduler


def main():
    logger_init()
    jobs_register()
    scheduler.start()


if __name__ == "__main__":
    main()
