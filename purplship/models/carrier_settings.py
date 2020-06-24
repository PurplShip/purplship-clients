# coding: utf-8

"""
    PurplShip Multi-carrier API

    PurplShip is a Multi-carrier Shipping API that simplifies the integration of logistic carrier services  # noqa: E501

    OpenAPI spec version: v1
    Contact: hello@purplship.com
    Generated by: https://github.com/PurplShip/purplship-python-client.git
"""


import pprint
import re  # noqa: F401

import six


class CarrierSettings(object):
    """NOTE: This class is auto generated by the purplship code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      purplship_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    purplship_types = {
        'id': 'str',
        'carrier_name': 'str',
        'carrier_id': 'str',
        'test': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'carrier_name': 'carrierName',
        'carrier_id': 'carrierId',
        'test': 'test'
    }

    def __init__(self, id=None, carrier_name=None, carrier_id=None, test=None):  # noqa: E501
        """CarrierSettings - a model defined in PurplShip"""  # noqa: E501

        self._id = None
        self._carrier_name = None
        self._carrier_id = None
        self._test = None
        self.discriminator = None

        self.id = id
        self.carrier_name = carrier_name
        self.carrier_id = carrier_id
        self.test = test

    @property
    def id(self):
        """Gets the id of this CarrierSettings.  # noqa: E501

        A unique address identifier  # noqa: E501

        :return: The id of this CarrierSettings.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CarrierSettings.

        A unique address identifier  # noqa: E501

        :param id: The id of this CarrierSettings.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501
        if id is not None and len(id) < 1:
            raise ValueError("Invalid value for `id`, length must be greater than or equal to `1`")  # noqa: E501

        self._id = id

    @property
    def carrier_name(self):
        """Gets the carrier_name of this CarrierSettings.  # noqa: E501

        Indicates a carrier (type)  # noqa: E501

        :return: The carrier_name of this CarrierSettings.  # noqa: E501
        :rtype: str
        """
        return self._carrier_name

    @carrier_name.setter
    def carrier_name(self, carrier_name):
        """Sets the carrier_name of this CarrierSettings.

        Indicates a carrier (type)  # noqa: E501

        :param carrier_name: The carrier_name of this CarrierSettings.  # noqa: E501
        :type: str
        """
        if carrier_name is None:
            raise ValueError("Invalid value for `carrier_name`, must not be `None`")  # noqa: E501
        allowed_values = ["canadapost", "dhl", "fedex", "purolator", "ups", "eshipper", "freightcom"]  # noqa: E501
        if carrier_name not in allowed_values:
            raise ValueError(
                "Invalid value for `carrier_name` ({0}), must be one of {1}"  # noqa: E501
                .format(carrier_name, allowed_values)
            )

        self._carrier_name = carrier_name

    @property
    def carrier_id(self):
        """Gets the carrier_id of this CarrierSettings.  # noqa: E501

        Indicates a specific carrier configuration name.  # noqa: E501

        :return: The carrier_id of this CarrierSettings.  # noqa: E501
        :rtype: str
        """
        return self._carrier_id

    @carrier_id.setter
    def carrier_id(self, carrier_id):
        """Sets the carrier_id of this CarrierSettings.

        Indicates a specific carrier configuration name.  # noqa: E501

        :param carrier_id: The carrier_id of this CarrierSettings.  # noqa: E501
        :type: str
        """
        if carrier_id is None:
            raise ValueError("Invalid value for `carrier_id`, must not be `None`")  # noqa: E501
        if carrier_id is not None and len(carrier_id) < 1:
            raise ValueError("Invalid value for `carrier_id`, length must be greater than or equal to `1`")  # noqa: E501

        self._carrier_id = carrier_id

    @property
    def test(self):
        """Gets the test of this CarrierSettings.  # noqa: E501

         The test flag indicates whether to use a carrier configured for test.    # noqa: E501

        :return: The test of this CarrierSettings.  # noqa: E501
        :rtype: bool
        """
        return self._test

    @test.setter
    def test(self, test):
        """Sets the test of this CarrierSettings.

         The test flag indicates whether to use a carrier configured for test.    # noqa: E501

        :param test: The test of this CarrierSettings.  # noqa: E501
        :type: bool
        """
        if test is None:
            raise ValueError("Invalid value for `test`, must not be `None`")  # noqa: E501

        self._test = test

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.purplship_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(CarrierSettings, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CarrierSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
