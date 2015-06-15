#!/usr/bin/env python2
# coding=utf8

from __future__ import absolute_import, division, print_function
from pickle import loads

import threading
import logging
import traceback
from beanstalkc import SocketError
from .beanstalkd import create_bstalk_conn
import time

"""
A simple thread pool - ref: hit9

Usage:
    pool = ThreadPool(size=10)  # size: how many threads in pool [default: 1]
    pool.start()  # start all threads to work!
    pool.stop()   # kill all threads in pool
"""


RESERVE_TIMEOUT = 0.1  # second(s)

logging.basicConfig()
log = logging.getLogger(__name__)


class ThreadWorker(threading.Thread):
    STOPPED = 0
    RUNNING = 1

    def __init__(self, pool):
        super(ThreadWorker, self).__init__()
        self.pool = pool
        # subthreads terminates once the main thread end
        self.setDaemon(True)
        self.state = ThreadWorker.STOPPED
        self.bstalk = create_bstalk_conn()

    def start(self):
        self.state = ThreadWorker.RUNNING
        super(ThreadWorker, self).start()

    def run(self):
        bstalk = self.bstalk
        while self.state == ThreadWorker.RUNNING:
            try:
                for tube in bstalk.tubes():
                    bstalk.watch(tube)
                    job = bstalk.reserve(RESERVE_TIMEOUT)
                    if job:
                        func, args, kwargs = loads(job.body)
                        try:
                            func(*args, **kwargs)
                            job.delete()
                        except Exception as e:
                            traceback.print_exc()
                            log.warn('error when doing job_deco [func:{}, params {} {}]'
                                     .format(func.__name__, args, kwargs))
                            job.delete()
                            continue

            except Exception:
                time.sleep(1)
                try:
                    bstalk.reconnect()
                    log.info('Beanstalkd reconnected.')
                    continue
                except SocketError:
                    log.error('could not connect to beanstalk.')
                    continue

    def stop(self):
        self.state = ThreadWorker.STOPPED
        self.bstalk.close()


class BstalkPool(object):

    def __init__(self, size=1):
        self.size = size
        self.threads = []

    def start(self):
        """start all threads"""
        for i in range(self.size):
            self.threads.append(ThreadWorker(self))
        for thread in self.threads:
            thread.start()

    def join(self):
        """join all threads"""
        for thread in self.threads:  # waiting completing
            if thread.isAlive():
                thread.join()

    def stop(self):
        """kill all threads"""
        for thread in self.threads:  # stop all threads
            thread.stop()
        self.join()  # waiting completing
        del self.threads[:]
