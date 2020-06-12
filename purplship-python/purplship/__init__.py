# coding: utf-8

# flake8: noqa

"""
    PurplShip Multi-carrier API

    PurplShip is a Multi-carrier Shipping API that simplifies the integration of logistic carrier services  # noqa: E501

    OpenAPI spec version: v1
    Contact: hello@purplship.com
"""


from __future__ import absolute_import

# import apis into sdk package
import purplship.api as resources

# import ApiClient
from purplship.client import ApiClient
from purplship.configuration import Configuration

# import models into sdk package
from purplship.models import *


api_key = None
api_key_prefix = 'Token'
host = None
api_client = None

configuration = Configuration()


def init_client():
    global api_client
    if (api_client is not None) and (host == configuration.host) and (api_key == configuration.api_key['Authorization']):
        return api_client

    configuration.host = host
    configuration.api_key['Authorization'] = f'{api_key_prefix} {api_key}'
    api_client = ApiClient(configuration)
    return api_client


class Carriers:

    @staticmethod
    def retrieve(*args, **kwargs):
        return resources.Carriers(init_client()).retrieve(*args, **kwargs)


class Rates:

    @staticmethod
    def fetch(*args, **kwargs):
        return resources.Rates(init_client()).fetch(*args, **kwargs)


class Shipments:

    @staticmethod
    def create(*args, **kwargs):
        return resources.Shipments(init_client()).create(*args, **kwargs)


class Tracking:

    @staticmethod
    def retrieve(*args, **kwargs):
        return resources.Tracking(init_client()).retrieve(*args, **kwargs)


class Utils:

    @staticmethod
    def get_reference(*args, **kwargs):
        return resources.Utils(init_client()).get_reference(*args, **kwargs)

    @staticmethod
    def print_label(*args, **kwargs):
        return resources.Utils(init_client()).print_label(*args, **kwargs)
