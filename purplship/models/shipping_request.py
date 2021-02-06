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

class ShippingRequest(object):
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
        'shipper': 'AddressData',
        'recipient': 'AddressData',
        'parcels': 'list[ParcelData]',
        'options': 'object',
        'payment': 'Payment',
        'customs': 'CustomsData',
        'reference': 'str',
        'label_type': 'str',
        'selected_rate_id': 'str',
        'rates': 'list[Rate]'
    }

    attribute_map = {
        'shipper': 'shipper',
        'recipient': 'recipient',
        'parcels': 'parcels',
        'options': 'options',
        'payment': 'payment',
        'customs': 'customs',
        'reference': 'reference',
        'label_type': 'label_type',
        'selected_rate_id': 'selected_rate_id',
        'rates': 'rates'
    }

    def __init__(self, shipper=None, recipient=None, parcels=None, options=None, payment=None, customs=None, reference=None, label_type='PDF', selected_rate_id=None, rates=None):  # noqa: E501
        """ShippingRequest - a model defined in Swagger"""  # noqa: E501
        self._shipper = None
        self._recipient = None
        self._parcels = None
        self._options = None
        self._payment = None
        self._customs = None
        self._reference = None
        self._label_type = None
        self._selected_rate_id = None
        self._rates = None
        self.discriminator = None
        self.shipper = shipper
        self.recipient = recipient
        self.parcels = parcels
        if options is not None:
            self.options = options
        self.payment = payment
        if customs is not None:
            self.customs = customs
        if reference is not None:
            self.reference = reference
        if label_type is not None:
            self.label_type = label_type
        self.selected_rate_id = selected_rate_id
        self.rates = rates

    @property
    def shipper(self):
        """Gets the shipper of this ShippingRequest.  # noqa: E501


        :return: The shipper of this ShippingRequest.  # noqa: E501
        :rtype: AddressData
        """
        return self._shipper

    @shipper.setter
    def shipper(self, shipper):
        """Sets the shipper of this ShippingRequest.


        :param shipper: The shipper of this ShippingRequest.  # noqa: E501
        :type: AddressData
        """
        if shipper is None:
            raise ValueError("Invalid value for `shipper`, must not be `None`")  # noqa: E501

        self._shipper = shipper

    @property
    def recipient(self):
        """Gets the recipient of this ShippingRequest.  # noqa: E501


        :return: The recipient of this ShippingRequest.  # noqa: E501
        :rtype: AddressData
        """
        return self._recipient

    @recipient.setter
    def recipient(self, recipient):
        """Sets the recipient of this ShippingRequest.


        :param recipient: The recipient of this ShippingRequest.  # noqa: E501
        :type: AddressData
        """
        if recipient is None:
            raise ValueError("Invalid value for `recipient`, must not be `None`")  # noqa: E501

        self._recipient = recipient

    @property
    def parcels(self):
        """Gets the parcels of this ShippingRequest.  # noqa: E501

        The shipment's parcels  # noqa: E501

        :return: The parcels of this ShippingRequest.  # noqa: E501
        :rtype: list[ParcelData]
        """
        return self._parcels

    @parcels.setter
    def parcels(self, parcels):
        """Sets the parcels of this ShippingRequest.

        The shipment's parcels  # noqa: E501

        :param parcels: The parcels of this ShippingRequest.  # noqa: E501
        :type: list[ParcelData]
        """
        if parcels is None:
            raise ValueError("Invalid value for `parcels`, must not be `None`")  # noqa: E501

        self._parcels = parcels

    @property
    def options(self):
        """Gets the options of this ShippingRequest.  # noqa: E501

         The options available for the shipment.<br/> Please consult [the reference](#operation/references) for additional specific carriers options.   # noqa: E501

        :return: The options of this ShippingRequest.  # noqa: E501
        :rtype: object
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this ShippingRequest.

         The options available for the shipment.<br/> Please consult [the reference](#operation/references) for additional specific carriers options.   # noqa: E501

        :param options: The options of this ShippingRequest.  # noqa: E501
        :type: object
        """

        self._options = options

    @property
    def payment(self):
        """Gets the payment of this ShippingRequest.  # noqa: E501


        :return: The payment of this ShippingRequest.  # noqa: E501
        :rtype: Payment
        """
        return self._payment

    @payment.setter
    def payment(self, payment):
        """Sets the payment of this ShippingRequest.


        :param payment: The payment of this ShippingRequest.  # noqa: E501
        :type: Payment
        """
        if payment is None:
            raise ValueError("Invalid value for `payment`, must not be `None`")  # noqa: E501

        self._payment = payment

    @property
    def customs(self):
        """Gets the customs of this ShippingRequest.  # noqa: E501


        :return: The customs of this ShippingRequest.  # noqa: E501
        :rtype: CustomsData
        """
        return self._customs

    @customs.setter
    def customs(self, customs):
        """Sets the customs of this ShippingRequest.


        :param customs: The customs of this ShippingRequest.  # noqa: E501
        :type: CustomsData
        """

        self._customs = customs

    @property
    def reference(self):
        """Gets the reference of this ShippingRequest.  # noqa: E501

        The shipment reference  # noqa: E501

        :return: The reference of this ShippingRequest.  # noqa: E501
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this ShippingRequest.

        The shipment reference  # noqa: E501

        :param reference: The reference of this ShippingRequest.  # noqa: E501
        :type: str
        """

        self._reference = reference

    @property
    def label_type(self):
        """Gets the label_type of this ShippingRequest.  # noqa: E501

        The shipment label file type.  # noqa: E501

        :return: The label_type of this ShippingRequest.  # noqa: E501
        :rtype: str
        """
        return self._label_type

    @label_type.setter
    def label_type(self, label_type):
        """Sets the label_type of this ShippingRequest.

        The shipment label file type.  # noqa: E501

        :param label_type: The label_type of this ShippingRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["PDF", "ZPL"]  # noqa: E501
        if label_type not in allowed_values:
            raise ValueError(
                "Invalid value for `label_type` ({0}), must be one of {1}"  # noqa: E501
                .format(label_type, allowed_values)
            )

        self._label_type = label_type

    @property
    def selected_rate_id(self):
        """Gets the selected_rate_id of this ShippingRequest.  # noqa: E501

        The shipment selected rate.  # noqa: E501

        :return: The selected_rate_id of this ShippingRequest.  # noqa: E501
        :rtype: str
        """
        return self._selected_rate_id

    @selected_rate_id.setter
    def selected_rate_id(self, selected_rate_id):
        """Sets the selected_rate_id of this ShippingRequest.

        The shipment selected rate.  # noqa: E501

        :param selected_rate_id: The selected_rate_id of this ShippingRequest.  # noqa: E501
        :type: str
        """
        if selected_rate_id is None:
            raise ValueError("Invalid value for `selected_rate_id`, must not be `None`")  # noqa: E501

        self._selected_rate_id = selected_rate_id

    @property
    def rates(self):
        """Gets the rates of this ShippingRequest.  # noqa: E501

        The list for shipment rates fetched previously  # noqa: E501

        :return: The rates of this ShippingRequest.  # noqa: E501
        :rtype: list[Rate]
        """
        return self._rates

    @rates.setter
    def rates(self, rates):
        """Sets the rates of this ShippingRequest.

        The list for shipment rates fetched previously  # noqa: E501

        :param rates: The rates of this ShippingRequest.  # noqa: E501
        :type: list[Rate]
        """
        if rates is None:
            raise ValueError("Invalid value for `rates`, must not be `None`")  # noqa: E501

        self._rates = rates

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
        if issubclass(ShippingRequest, dict):
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
        if not isinstance(other, ShippingRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
