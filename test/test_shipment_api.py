# coding: utf-8

"""
    PurplShip Multi-carrier API

    PurplShip is a Multi-carrier Shipping API that simplifies the integration of logistic carrier services  # noqa: E501

    OpenAPI spec version: v1
    Contact: hello@purplship.com
    Generated by: https://github.com/PurplShip/purplship-python-client.git
"""


from __future__ import absolute_import

import unittest

import purplship
from purplship.api.shipment import Shipment  # noqa: E501
from purplship.rest import ApiException


class TestShipment(unittest.TestCase):
    """Shipment unit test stubs"""

    def setUp(self):
        self.api = purplship.api.shipment.Shipment()  # noqa: E501

    def tearDown(self):
        pass

    def test_shipment(self):
        """Test case for shipment

        Create a Shipment  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()