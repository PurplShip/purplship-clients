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

class PickupRequest(object):
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
        'pickup_date': 'str',
        'address': 'AddressData',
        'parcels': 'list[ParcelData]',
        'ready_time': 'str',
        'closing_time': 'str',
        'instruction': 'str',
        'package_location': 'str',
        'options': 'object'
    }

    attribute_map = {
        'pickup_date': 'pickup_date',
        'address': 'address',
        'parcels': 'parcels',
        'ready_time': 'ready_time',
        'closing_time': 'closing_time',
        'instruction': 'instruction',
        'package_location': 'package_location',
        'options': 'options'
    }

    def __init__(self, pickup_date=None, address=None, parcels=None, ready_time=None, closing_time=None, instruction=None, package_location=None, options=None):  # noqa: E501
        """PickupRequest - a model defined in Swagger"""  # noqa: E501
        self._pickup_date = None
        self._address = None
        self._parcels = None
        self._ready_time = None
        self._closing_time = None
        self._instruction = None
        self._package_location = None
        self._options = None
        self.discriminator = None
        self.pickup_date = pickup_date
        self.address = address
        self.parcels = parcels
        self.ready_time = ready_time
        self.closing_time = closing_time
        if instruction is not None:
            self.instruction = instruction
        if package_location is not None:
            self.package_location = package_location
        if options is not None:
            self.options = options

    @property
    def pickup_date(self):
        """Gets the pickup_date of this PickupRequest.  # noqa: E501

         The expected pickup date  Date Format: `YYYY-MM-DD`   # noqa: E501

        :return: The pickup_date of this PickupRequest.  # noqa: E501
        :rtype: str
        """
        return self._pickup_date

    @pickup_date.setter
    def pickup_date(self, pickup_date):
        """Sets the pickup_date of this PickupRequest.

         The expected pickup date  Date Format: `YYYY-MM-DD`   # noqa: E501

        :param pickup_date: The pickup_date of this PickupRequest.  # noqa: E501
        :type: str
        """
        if pickup_date is None:
            raise ValueError("Invalid value for `pickup_date`, must not be `None`")  # noqa: E501

        self._pickup_date = pickup_date

    @property
    def address(self):
        """Gets the address of this PickupRequest.  # noqa: E501


        :return: The address of this PickupRequest.  # noqa: E501
        :rtype: AddressData
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this PickupRequest.


        :param address: The address of this PickupRequest.  # noqa: E501
        :type: AddressData
        """
        if address is None:
            raise ValueError("Invalid value for `address`, must not be `None`")  # noqa: E501

        self._address = address

    @property
    def parcels(self):
        """Gets the parcels of this PickupRequest.  # noqa: E501

        The shipment parcels to pickup.  # noqa: E501

        :return: The parcels of this PickupRequest.  # noqa: E501
        :rtype: list[ParcelData]
        """
        return self._parcels

    @parcels.setter
    def parcels(self, parcels):
        """Sets the parcels of this PickupRequest.

        The shipment parcels to pickup.  # noqa: E501

        :param parcels: The parcels of this PickupRequest.  # noqa: E501
        :type: list[ParcelData]
        """
        if parcels is None:
            raise ValueError("Invalid value for `parcels`, must not be `None`")  # noqa: E501

        self._parcels = parcels

    @property
    def ready_time(self):
        """Gets the ready_time of this PickupRequest.  # noqa: E501

         The ready time for pickup.  Time Format: `HH:MM`   # noqa: E501

        :return: The ready_time of this PickupRequest.  # noqa: E501
        :rtype: str
        """
        return self._ready_time

    @ready_time.setter
    def ready_time(self, ready_time):
        """Sets the ready_time of this PickupRequest.

         The ready time for pickup.  Time Format: `HH:MM`   # noqa: E501

        :param ready_time: The ready_time of this PickupRequest.  # noqa: E501
        :type: str
        """
        if ready_time is None:
            raise ValueError("Invalid value for `ready_time`, must not be `None`")  # noqa: E501

        self._ready_time = ready_time

    @property
    def closing_time(self):
        """Gets the closing_time of this PickupRequest.  # noqa: E501

         The closing or late time of the pickup  Time Format: `HH:MM`   # noqa: E501

        :return: The closing_time of this PickupRequest.  # noqa: E501
        :rtype: str
        """
        return self._closing_time

    @closing_time.setter
    def closing_time(self, closing_time):
        """Sets the closing_time of this PickupRequest.

         The closing or late time of the pickup  Time Format: `HH:MM`   # noqa: E501

        :param closing_time: The closing_time of this PickupRequest.  # noqa: E501
        :type: str
        """
        if closing_time is None:
            raise ValueError("Invalid value for `closing_time`, must not be `None`")  # noqa: E501

        self._closing_time = closing_time

    @property
    def instruction(self):
        """Gets the instruction of this PickupRequest.  # noqa: E501

         The pickup instruction.  eg: Handle with care.   # noqa: E501

        :return: The instruction of this PickupRequest.  # noqa: E501
        :rtype: str
        """
        return self._instruction

    @instruction.setter
    def instruction(self, instruction):
        """Sets the instruction of this PickupRequest.

         The pickup instruction.  eg: Handle with care.   # noqa: E501

        :param instruction: The instruction of this PickupRequest.  # noqa: E501
        :type: str
        """

        self._instruction = instruction

    @property
    def package_location(self):
        """Gets the package_location of this PickupRequest.  # noqa: E501

         The package(s) location.  eg: Behind the entrance door.   # noqa: E501

        :return: The package_location of this PickupRequest.  # noqa: E501
        :rtype: str
        """
        return self._package_location

    @package_location.setter
    def package_location(self, package_location):
        """Sets the package_location of this PickupRequest.

         The package(s) location.  eg: Behind the entrance door.   # noqa: E501

        :param package_location: The package_location of this PickupRequest.  # noqa: E501
        :type: str
        """

        self._package_location = package_location

    @property
    def options(self):
        """Gets the options of this PickupRequest.  # noqa: E501

        Advanced carrier specific pickup options  # noqa: E501

        :return: The options of this PickupRequest.  # noqa: E501
        :rtype: object
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this PickupRequest.

        Advanced carrier specific pickup options  # noqa: E501

        :param options: The options of this PickupRequest.  # noqa: E501
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
        if issubclass(PickupRequest, dict):
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
        if not isinstance(other, PickupRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
