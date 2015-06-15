#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import os

from fabric.api import (
    env,
    execute,
    local,
    task,
    hosts,
)


env.use_ssh_config = True
env.keepalive = 60


DEPLOYMENT_PARAMS = {
    "repo": "walis",
    "remote_user": "www-data",
    "local_dir": os.path.dirname(os.path.realpath(__file__)),
    "remote_dir": "/srv/walis",
    "remote_exclude": "rsync_exclude.txt",
    "requirements": "requirements.txt",
    "require_install": True,
    "virtualenv": "/srv/virtualenvs/walisenv",
    "services": [
        "walis:",
        "walis_thrift:",
        # "beanstalk:",
        # "scheduler:",
    ],
}


@task
def dev(*args):
    """ Deploy dev env.

    :param args: host names
    :return:
    """
    if not args:
        print('Tips: \n1. `fab dev:hostname1,hostname2,hostname3`'
              '\n2. `fab dev:all`')
        return
    if args[0] == 'all':
        env.hosts = ['t-walis-1',
                     't-walis-2',
                     't-walis-3',
                     't-walis-4',
                     't-walis-test', ]
    else:
        env.hosts = args

    execute(_walis_deploy)


@task
@hosts(['xg-ppe-walle',])
def ppe_deploy():
    execute(_walis_deploy)


@task
@hosts(['d048-app-11', 'd048-app-12'])
def d_deploy():
    execute(_walis_deploy)


@task
@hosts(['p-web-6'])
def p_deploy():
    execute(_walis_deploy)


@task
def tag():
    local("git checkout master")
    local("git reset --hard origin/master")
    local("git merge develop")
    local("git push")

    tag = "v{0}".format(datetime.datetime.now().strftime("%Y%m%d%H%M"))
    local("git tag -f {0}".format(tag))
    local("git push --tags")
    local("git checkout develop")


@task
def _walis_deploy():
    import deployele
    # local("git fetch origin --prune --tags")
    execute(deployele.python_deploy, **DEPLOYMENT_PARAMS)
