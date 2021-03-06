# coding: utf-8

"""
    Purplship Open Source Multi-carrier Shipping API

     Purplship is an open source multi-carrier shipping API that simplifies the integration of logistic carrier services  The **proxy** endpoints are stateless and forwards calls to carriers web services.   # noqa: E501

    OpenAPI spec version: v1-2021.2
    Contact: hello@purplship.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class LabelPrintingRequest(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'label': 'str'
    }

    attribute_map = {
        'name': 'name',
        'label': 'label'
    }

    def __init__(self, name=None, label=None):  # noqa: E501
        """LabelPrintingRequest - a model defined in Purplship"""  # noqa: E501
        self._name = None
        self._label = None
        self.discriminator = None
        self.name = name
        self.label = label

    @property
    def name(self):
        """Gets the name of this LabelPrintingRequest.  # noqa: E501

         PDF file name.  eg: shipment-[trackingNumber]   # noqa: E501

        :return: The name of this LabelPrintingRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this LabelPrintingRequest.

         PDF file name.  eg: shipment-[trackingNumber]   # noqa: E501

        :param name: The name of this LabelPrintingRequest.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def label(self):
        """Gets the label of this LabelPrintingRequest.  # noqa: E501

        Shipment base64 label  # noqa: E501

        :return: The label of this LabelPrintingRequest.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this LabelPrintingRequest.

        Shipment base64 label  # noqa: E501

        :param label: The label of this LabelPrintingRequest.  # noqa: E501
        :type: str
        """
        if label is None:
            raise ValueError("Invalid value for `label`, must not be `None`")  # noqa: E501

        self._label = label

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(LabelPrintingRequest, dict):
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
        if not isinstance(other, LabelPrintingRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
