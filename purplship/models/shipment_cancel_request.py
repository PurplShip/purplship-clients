# coding: utf-8

"""
    Purplship Open Source Multi-carrier Shipping API

     Purplship is an open source multi-carrier shipping API that simplifies the integration of logistic carrier services  The **proxy** endpoints are stateless and forwards calls to carriers web services.   # noqa: E501

    OpenAPI spec version: v1-2021.0
    Contact: hello@purplship.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ShipmentCancelRequest(object):
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
        'shipment_identifier': 'str',
        'service': 'str',
        'options': 'object'
    }

    attribute_map = {
        'shipment_identifier': 'shipment_identifier',
        'service': 'service',
        'options': 'options'
    }

    def __init__(self, shipment_identifier=None, service=None, options=None):  # noqa: E501
        """ShipmentCancelRequest - a model defined in Swagger"""  # noqa: E501
        self._shipment_identifier = None
        self._service = None
        self._options = None
        self.discriminator = None
        self.shipment_identifier = shipment_identifier
        if service is not None:
            self.service = service
        if options is not None:
            self.options = options

    @property
    def shipment_identifier(self):
        """Gets the shipment_identifier of this ShipmentCancelRequest.  # noqa: E501

        The shipment identifier returned during creation  # noqa: E501

        :return: The shipment_identifier of this ShipmentCancelRequest.  # noqa: E501
        :rtype: str
        """
        return self._shipment_identifier

    @shipment_identifier.setter
    def shipment_identifier(self, shipment_identifier):
        """Sets the shipment_identifier of this ShipmentCancelRequest.

        The shipment identifier returned during creation  # noqa: E501

        :param shipment_identifier: The shipment_identifier of this ShipmentCancelRequest.  # noqa: E501
        :type: str
        """
        if shipment_identifier is None:
            raise ValueError("Invalid value for `shipment_identifier`, must not be `None`")  # noqa: E501

        self._shipment_identifier = shipment_identifier

    @property
    def service(self):
        """Gets the service of this ShipmentCancelRequest.  # noqa: E501

        The selected shipment service  # noqa: E501

        :return: The service of this ShipmentCancelRequest.  # noqa: E501
        :rtype: str
        """
        return self._service

    @service.setter
    def service(self, service):
        """Sets the service of this ShipmentCancelRequest.

        The selected shipment service  # noqa: E501

        :param service: The service of this ShipmentCancelRequest.  # noqa: E501
        :type: str
        """

        self._service = service

    @property
    def options(self):
        """Gets the options of this ShipmentCancelRequest.  # noqa: E501

        Advanced carrier specific cancellation options  # noqa: E501

        :return: The options of this ShipmentCancelRequest.  # noqa: E501
        :rtype: object
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this ShipmentCancelRequest.

        Advanced carrier specific cancellation options  # noqa: E501

        :param options: The options of this ShipmentCancelRequest.  # noqa: E501
        :type: object
        """

        self._options = options

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
        if issubclass(ShipmentCancelRequest, dict):
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
        if not isinstance(other, ShipmentCancelRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
