# coding=utf8
from logging.handlers import RotatingFileHandler
from os2emxpath import abspath, split


WALIS_ENV = 'dev'
SOURCE_DIR = abspath(split(__file__)[0])

########
# Flask
########
FLASK = {
    'DEBUG': True,
    'SECRET_KEY': '\xdfK\xcc\x99"\x01W\xf6\xcb>\xa1\xfc@\x06\x9b\x88\xdc\xb4)t_W\xbd\xde',  # noqa
}

########
# Login
########
LOGIN = {
    'enabled': True,
    'sso_login_url': 'http://walle.eleme.test/login',
    'exclude': [
        # Flask endpoint names
        'static',
        'PingApi:get',
        'LoginApi:get',
        'LoginApi:set_sso_login_token',
        'VoiceCallApi:sync_result',
        'VoiceCallApi:call_end',
        'VoiceCallApi:keysback',
        'HermesReceiverApi:push'
    ]
}

###########
# DataBase
###########
MYSQL = {
    'master': {
        'host': 't-walis-base',
        'port': 3306,
        'user': 'root',
        'passwd': 'eleme',
        'database': 'javis'
    }
}

REDIS = {
    "host": "127.0.0.1",
    "port": 6379,
    "password": "",
}

MONGO = {
    'url': 'mongodb://t-walis-base:27017',
    'database': 'rizzrack',
}

ZEUS_SLAVE_MYSQL_SETTINGS = {
    "host": "old_testing",
    "port": 3306,
    "user": "eleme",
    "passwd": "eleMe",
    "database": "eleme"
}

WALLE_ANALYTICS = {
    "host": "t-walis-base",
    "port": 3306,
    "user": "root",
    "passwd": "eleme",
    "database": 'javis'
}

TRANSACTION_PG = {
    "host": "",
    "port": 5432,
    "user": "",
    "passwd": "",
    "database": ''
}

#############
# Beanstalkd
#############
# thread pool size for beanstalkd task handler
BEANSTALKD = {
    'host': '127.0.0.1',
    'port': 11300,
    'pool_size': 20,
}

###########
# Monitor
###########
STATSD = {
    'host': '127.0.0.1',
    'port': 8125,
    'prefix': 'walis'
}

#########
# Thrift
#########
THRIFT_SERVICE = {
    'ers': {
        'host': 'dev_zeus_walis',
        'port': 29091,
    },
    'eus': {
        'host': 'dev_zeus_walis',
        'port': 29098,
    },
    'eos': {
        'host': 'dev_zeus_walis',
        'port': 29090,
    },
    'ess': {
        'host': 'dev_zeus_walis',
        'port': 16500,
    },
    'ees': {
        'host': 'dev_zeus_walis',
        'port': 29099,
    },
    'fuss': {
        'host': 'fuss_server',
        'port': 9093,
    },
    'sms': {
        'host': 'dev_zeus_walis',
        'port': 29093,
    },
    'eyes': {
        'host': 'eyes_server',
        'port': 14365,
    },
    'keeper': {
        'host': 'keeper_server',
        'port': 16799,
    }
}

COFFEE_SERVICE = {
    'server': 'http://172.16.10.25:8888',
    'bpm_mkt_utp': 'http://172.16.10.28:5555',
}

JVS_THRIFT_SERVICE = {
    'host': '0.0.0.0',
    'port': 17009,
}

############
# Scheduler
############
SCHEDULER = {
    'enabled': {
        # Default False
        'voiceorder_job': False,
        'voicecall_job': False,
        'voicecall_ban_daily_clean_job': False,
        'process_order': False,
        'notice_activity_pay': False,
        'clean_rst_director': False,
        'notice_unwatched_rst': False,
        'test': False
    }
}

#########
# Hermes
#########
HERMES = {
    'thrift_host': 'localhost',
    'thrift_port': 16334,
    'sender_key': '82ac83555509daf1761b5bcb08774a36e42e700c2fa7d36e5bf5d2bb5d1408b7'
}

###########
# Logging
###########
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'root': {
        'handlers': ['console', 'rpc', 'all'],
        'level': 'INFO'
    },
    'filters': {
        'module': {
            '()': 'walis.core.log.ModuleFilter',
        },
        'rpc': {
            '()': 'walis.core.log.RPCFilter',
        }
    },
    'loggers': {
        'scheduler': {
            'handlers': ['scheduler'],
            'propagate': False,
            'level': 'INFO'
        },
        'requests': {
            'handlers': ['rpc'],
            'propagate': False,
            'level': 'INFO'
        }
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'uniform',
            'filters': ['module', ],
        },
        'scheduler': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'INFO',
            'formatter': 'uniform',
            'filename': '/var/log/walis/scheduler.log',
            'mode': 'a',
            'maxBytes': 262144000,  # 200M
            'backupCount': 5,
        },
        'rpc': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'WARN',
            'filters': ['rpc', ],
            'formatter': 'uniform',
            'filename': '/var/log/walis/rpc.log',
            'mode': 'a',
            'maxBytes': 262144000,  # 200M
            'backupCount': 10,
        },
        'all': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'INFO',
            'formatter': 'uniform',
            'filename': '/var/log/walis/all.log',
            'mode': 'a',
            'maxBytes': 262144000,  # 200M
            'backupCount': 10,
        },
    },
    'formatters': {
        'uniform': {
            'format': '%(asctime)s %(levelname)-6s %(name)s[%(process)d]'
                      ' %(message)s'
        }
    }
}


# Used in prod env
try:
    from walisconfig import *
except:
    pass
