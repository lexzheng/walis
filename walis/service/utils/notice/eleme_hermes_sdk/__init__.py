#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Jack River'

import warnings
import json
import os
import thriftpy
from thrift_connector import ClientPool, ThriftPyCyClient

_thrift_file = thriftpy.load(
    os.path.join(os.path.dirname(os.path.realpath(__file__)), 'hermes.thrift')
)

HermesSystemException = _thrift_file.HermesSystemException
HermesUserException = _thrift_file.HermesUserException
HermesUnknownException = _thrift_file.HermesUnknownException

HermesErrorCode = _thrift_file.HermesErrorCode


def deprecated(func):
    """This is a decorator which can be used to mark functions
    as deprecated. It will result in a warning being emitted
    when the function is used."""
    def new_func(*args, **kwargs):
        warnings.warn("Call to deprecated function {}.".format(func.__name__),
                      category=DeprecationWarning)
        return func(*args, **kwargs)
    new_func.__name__ = func.__name__
    new_func.__doc__ = func.__doc__
    new_func.__dict__.update(func.__dict__)
    return new_func


class HermesClient(object):

    def __init__(self, thrift_host, thrift_port, sender_key):
        self.thrift_host = thrift_host
        self.thrift_port = thrift_port
        self.sender_key = sender_key
        self.connection_pool = ClientPool(
            service=_thrift_file.HermesService,
            host=self.thrift_host, port=self.thrift_port,
            max_conn=30, connction_class=ThriftPyCyClient,
            keepalive=1800
            )
        self.get_client_ctx = self.connection_pool.connection_ctx

    def send(self, receiver, message, need_reply=False, retry=None):
        """ direct message send without template

        :param receiver: phone number
        :param message: message content
        :param need_reply: should receive user reply
        :param retry: (Int) retry times when fail, if None, server will decide
        :return: id of Task
        """
        with self.get_client_ctx() as client:
            param = _thrift_file.NormalTaskCreationParameter(
                receivers=receiver,
                message=message,
                sender_key=self.sender_key,
                need_reply=need_reply,
                retry_count=retry,
            )
            return client.create_task(param)

    def template_send(self, receiver, template_slug,
                      template_params, need_reply=False, retry=None):
        """ send message via sms template

        :param receiver: phone number
        :param template_slug: slug of SMSTemplate
        :param template_params: (dict) params to format template
        :param need_reply: should receive user reply
        :param retry: (Int) retry times when fail, if None, server will decide
        :return: id of Task
        """
        with self.get_client_ctx() as client:
            template_id = client.get_template_id_by_slug(template_slug)

            param = _thrift_file.TemplateTaskCreationParameter(
                receivers=receiver,
                template_id=template_id,
                template_params=json.dumps(template_params),
                sender_key=self.sender_key,
                need_reply=need_reply,
                retry_count=retry,
            )
            return client.create_template_task(param)

    def audio_send(self, receiver, message, retry=None):
        """ send audio message
        :param receiver: receiver phone number
        :param message: message to send
        :param retry: retry count
        :return:
        """
        with self.get_client_ctx() as client:
            param = _thrift_file.AudioTaskCreationParameter(
                receivers=receiver,
                message=message,
                sender_key=self.sender_key,
                retry_count=retry,
            )
            return client.create_audio_task(param)

    def send_verify_code(self, receiver, code=None,
                         expire=None, via_audio=False, audio_call_type=None):
        """ send verify code

        :param receiver: phone number
        :param code: (String) code to send, if None 6-digit number will be used
        :param expire: (Int) expire in minutes, if None then no expire
        :param via_audio: (Bool) should send audio verify code, default False
        :param audio_call_type: audio verify code call: 0(out)/1(in)/2(both)
        :return: (hash_value, code)
        """
        with self.get_client_ctx() as client:
            param = _thrift_file.VerifyCodeCreationParameter(
                sender_key=self.sender_key,
                receiver=receiver,
                code=code,
                expire=expire,
                via_audio=via_audio,
                audio_call_type=audio_call_type,
            )
            result = client.verify_code_create(param)
            return result.hash_value, result.code

    def send_email_verify_code(self, receiver, code=None, expire=None):
        """ send verify code

        :param receiver: email address
        :param code: (String) code to send, if None 6-digit number will be used
        :param expire: (Int) expire in minutes, if None then no expire
        :return: (hash_value, code)
        """
        with self.get_client_ctx() as client:
            param = _thrift_file.EmailVerifyCodeCreationParameter(
                sender_key=self.sender_key,
                receiver=receiver,
                code=code,
                expire=expire,
            )
            result = client.email_verify_code_create(param)
            return result.hash_value, result.code

    @deprecated
    def validate_verify_code(self, hash_value, to_validate):
        """ validate verify code

        :param hash_value: hash value returned from send_verify_code
        :param to_validate: verify code from user
        :return: (Bool) Return is_valid. If expire reached, always return False
        """
        with self.get_client_ctx() as client:
            return client.verify_code_validate(hash_value, to_validate)

    def validate_verify_code_with_hash(self, hash_value, to_validate):
        """ validate verify code

        :param hash_value: hash value returned from send_verify_code
        :param to_validate: verify code from user
        :return: (Bool) Return is_valid. If expire reached, always return False
        """
        with self.get_client_ctx() as client:
            return client.validate_verify_code_with_hash(self.sender_key,
                                                         hash_value,
                                                         to_validate)

    def validate_verify_code_with_receiver(self, receiver, to_validate):
        """ validate verify code

        :param receiver: user phone number
        :param to_validate: verify code from user
        :return: (Bool) Return is_valid. If expire reached, always return False
        """
        with self.get_client_ctx() as client:
            return client.validate_verify_code_with_receiver(self.sender_key,
                                                             receiver,
                                                             to_validate)

    def validated_within_n_minutes(self, receiver, minutes):
        """ is receiver successfully validated within n minutes

        :param receiver: user phone number
        :param minutes: n minutes
        :return: True/False
        """
        with self.get_client_ctx() as client:
            return client.validated_within_n_minutes(
                self.sender_key,
                receiver,
                minutes
            )


__all__ = (
    'HermesClient',
)
