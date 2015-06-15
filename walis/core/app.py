# coding=utf8

from flask import Flask
import sys

from .log import logger_init
from .monitor import statsd_init
from .signal import reg_signals
from walis.api import api_init
from walis.core.auth import auth_init
from walis.service.login import login_init


reload(sys)
sys.setdefaultencoding('utf-8')


class WalisApp(Flask):

    def init(self, settings):
        # update flask app config
        self.config.update(**settings.FLASK)

        reg_signals()

        logger_init()

        statsd_init()

        api_init(self)

        auth_init(self)

        login_init(self)



