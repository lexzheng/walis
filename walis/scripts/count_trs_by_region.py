# coding=utf8

from __future__ import absolute_import, division, print_function

from walis.service.analytics.transaction import count_all_daily_trs_by_city


def main():
    result = count_all_daily_trs_by_city(1)
    print(result)


if __name__ == '__main__':
    main()