#!/usr/bin/env python2
# -*- coding: utf8 -*-

from __future__ import absolute_import, division, print_function

from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
from apscheduler.schedulers.blocking import BlockingScheduler

from walis import config
from walis.utils.module import load_obj
from walis.scheduler.setting import JOB_SETTINGS


executors = {
    'default': ThreadPoolExecutor(10),
    'processpool': ProcessPoolExecutor(5)
}
job_defaults = {
    'coalesce': False,
    'max_instances': 1
}

scheduler = BlockingScheduler(executors=executors,
                              job_defaults=job_defaults)


def jobs_register():
    job_enabled_map = config.SCHEDULER['enabled']

    for job_name, job_args in JOB_SETTINGS.items():
        if job_enabled_map.get(job_name):
            job_args.update({
                'func': load_obj('walis.scheduler.jobs.' + job_args['func'])
            })
            scheduler.add_job(**job_args)
