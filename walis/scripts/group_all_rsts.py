# coding=utf8

from __future__ import absolute_import, division, print_function
import logging
import logging.config
from walis import config
from walis.service.rst.group import group_all_restaurants

# init logging
logging.config.dictConfig(config.LOGGING)
log = logging.getLogger(__name__)


def main():
    group_all_restaurants(1, (121.449394,31.232179), 2, 9999)

if __name__ == '__main__':
    main()