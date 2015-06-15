#!/usr/bin/env python2
# coding=utf8

from __future__ import absolute_import, division, print_function
import os
import shutil
import argparse


def main(force_cover=False):
    need_cp = True
    config_existed = os.path.isfile('walisconfig.py')

    if not force_cover and config_existed:
        cover = raw_input('File walisconfig.py is already exist,'
                          ' do you want to cover it?(Y/n)')
        if cover not in ('y', 'yes', 'Y', 'Yes'):
            need_cp = False

    if need_cp:
        shutil.copy('walis/config.py', 'walisconfig.py')
        print('walisconfig is successfully generated!')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate walisconfig.')
    parser.add_argument('-f', '--force_cover', action='store_true',
                        help='force cover old walisconfig.')
    args = parser.parse_args()
    main(args.force_cover)
