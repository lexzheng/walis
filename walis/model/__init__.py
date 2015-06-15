# coding=utf8
from sqlalchemy.ext.declarative import declarative_base

ModelBase = declarative_base()


class WalisModel(object):

    def to_dict(self):
        result = {}
        for key, value in self.__dict__.iteritems():
            if key.startswith('_'):
                continue
            result[key] = value
        return result
