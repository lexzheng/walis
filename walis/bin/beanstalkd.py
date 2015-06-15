#!/usr/bin/python
# -*- coding:utf-8 -*-

import logging
import logging.config

from walis import config
from walis.core.async.pool import BstalkPool

# init logging
logging.config.dictConfig(config.LOGGING)
log = logging.getLogger(__name__)


def main():
    log.info("start to run task handlers.")
    pool = BstalkPool(config.BEANSTALKD['pool_size'])
    pool.start()
    # wait
    pool.join()


if __name__ == "__main__":
    main()
