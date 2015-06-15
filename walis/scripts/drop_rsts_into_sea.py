# coding=utf8

from __future__ import absolute_import, division, print_function
from walis.service.rst import group
import logging
import logging.config
from walis import config
# init logging
logging.config.dictConfig(config.LOGGING)
log = logging.getLogger(__name__)


def main():
    group.drop_bod_invalid_rsts(1, -100)


if __name__ == '__main__':
    main()
