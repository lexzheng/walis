#!/usr/bin/env python2
# coding=utf8

from __future__ import absolute_import, division, print_function
import argparse
from walis.service.rst.group import group_ungrouped_rsts


def main():
    print('Start running script: group_ungrouped_rsts')
    parser = argparse.ArgumentParser()
    parser.add_argument("city_id", help="city id", type=int)
    args = parser.parse_args()
    group_ungrouped_rsts(args.city_id)
    print('End of script: group_ungrouped_rsts')

if __name__ == '__main__':
    main()
