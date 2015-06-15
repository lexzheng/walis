#!/usr/bin/env python2
# coding=utf8

from __future__ import absolute_import, division, print_function
import sys
import getopt
from walis.core.db.redis import redis

PAY_NOTIFY_PENDING_RECORD_IDS = 'pay_notify:pending_record_ids'
PAY_NOTIFY_PROCESS_AT_RECORD_ID = 'pay_notify:process_at_record_id'


def get_pending_record_ids():
    """
    获取'已提交'状态的打款记录

    :return:
    """
    process_ids = redis.smembers(PAY_NOTIFY_PENDING_RECORD_IDS)
    if not process_ids:
        return []
    return process_ids


def get_process_at_record_id():
    """
    获取最近一次处理的record_id

    :return:
    """
    record_id = redis.get(PAY_NOTIFY_PROCESS_AT_RECORD_ID)
    if record_id is None:
        return 0

    return int(record_id)


def set_process_at_record_id(record_id):
    """
    设置最近一次处理的record_id

    :return:
    """
    process_at = get_process_at_record_id()

    if record_id > process_at:
        redis.set(PAY_NOTIFY_PROCESS_AT_RECORD_ID, record_id)
        return True

    return False


def show_process_at():
    process_at = get_process_at_record_id()
    print('Pay Notify is processed at {} (record id)'.format(process_at))


def show_pending_record_ids():
    pending_ids = get_pending_record_ids()
    print('Pending record ids\n\tlength: {}'.format(len(pending_ids), ))


def set_process_at(record_id):
    process_at = get_process_at_record_id()
    hint = 'Will you change pay notify process at from {} to {} ?'.\
        format(process_at, record_id)

    choice = raw_input(hint + '(y/n)')
    if choice == 'y' or choice == 'yes':
        set_process_at_record_id(record_id)
        print('Done. Now process at {}'.format(get_process_at_record_id()))
        return

    print('Cancel request.')


def usage():
    print('PayNotify script.py usage:')
    print('-h,--help: print help message.')
    print('-s: print process at and pending record ids')
    print('--set=<int>: set process at record id\n')


def main(argv):
    try:
        opts, args = getopt.getopt(argv[1:], 'sh', ['set='])
    except getopt.GetoptError, err:
        print(str(err))
        usage()
        sys.exit(0)

    if not opts:
        show_process_at()
        exit(1)

    for opt, arg in opts:
        if opt == '--set':
            set_process_at(arg)
            sys.exit(1)
        elif opt == '-s':
            show_process_at()
            show_pending_record_ids()
            sys.exit(1)
        else:
            usage()
            sys.exit(0)


if __name__ == '__main__':
    main(sys.argv)
