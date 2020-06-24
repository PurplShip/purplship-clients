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


class Customs(object):
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
        'no_eei': 'str',
        'aes': 'str',
        'description': 'str',
        'terms_of_trade': 'str',
        'commodities': 'list[Commodity]',
        'duty': 'Payment',
        'invoice': 'Invoice',
        'commercial_invoice': 'bool'
    }

    attribute_map = {
        'no_eei': 'noEei',
        'aes': 'aes',
        'description': 'description',
        'terms_of_trade': 'termsOfTrade',
        'commodities': 'commodities',
        'duty': 'duty',
        'invoice': 'invoice',
        'commercial_invoice': 'commercialInvoice'
    }

    def __init__(self, no_eei=None, aes=None, description=None, terms_of_trade=None, commodities=None, duty=None, invoice=None, commercial_invoice=None):  # noqa: E501
        """Customs - a model defined in PurplShip"""  # noqa: E501

        self._no_eei = None
        self._aes = None
        self._description = None
        self._terms_of_trade = None
        self._commodities = None
        self._duty = None
        self._invoice = None
        self._commercial_invoice = None
        self.discriminator = None

        if no_eei is not None:
            self.no_eei = no_eei
        if aes is not None:
            self.aes = aes
        if description is not None:
            self.description = description
        if terms_of_trade is not None:
            self.terms_of_trade = terms_of_trade
        if commodities is not None:
            self.commodities = commodities
        if duty is not None:
            self.duty = duty
        if invoice is not None:
            self.invoice = invoice
        if commercial_invoice is not None:
            self.commercial_invoice = commercial_invoice

    @property
    def no_eei(self):
        """Gets the no_eei of this Customs.  # noqa: E501


        :return: The no_eei of this Customs.  # noqa: E501
        :rtype: str
        """
        return self._no_eei

    @no_eei.setter
    def no_eei(self, no_eei):
        """Sets the no_eei of this Customs.


        :param no_eei: The no_eei of this Customs.  # noqa: E501
        :type: str
        """
        if no_eei is not None and len(no_eei) < 1:
            raise ValueError("Invalid value for `no_eei`, length must be greater than or equal to `1`")  # noqa: E501

        self._no_eei = no_eei

    @property
    def aes(self):
        """Gets the aes of this Customs.  # noqa: E501


        :return: The aes of this Customs.  # noqa: E501
        :rtype: str
        """
        return self._aes

    @aes.setter
    def aes(self, aes):
        """Sets the aes of this Customs.


        :param aes: The aes of this Customs.  # noqa: E501
        :type: str
        """
        if aes is not None and len(aes) < 1:
            raise ValueError("Invalid value for `aes`, length must be greater than or equal to `1`")  # noqa: E501

        self._aes = aes

    @property
    def description(self):
        """Gets the description of this Customs.  # noqa: E501


        :return: The description of this Customs.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Customs.


        :param description: The description of this Customs.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) < 1:
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `1`")  # noqa: E501

        self._description = description

    @property
    def terms_of_trade(self):
        """Gets the terms_of_trade of this Customs.  # noqa: E501

        The customs 'term of trade' also known as 'incoterm'  # noqa: E501

        :return: The terms_of_trade of this Customs.  # noqa: E501
        :rtype: str
        """
        return self._terms_of_trade

    @terms_of_trade.setter
    def terms_of_trade(self, terms_of_trade):
        """Sets the terms_of_trade of this Customs.

        The customs 'term of trade' also known as 'incoterm'  # noqa: E501

        :param terms_of_trade: The terms_of_trade of this Customs.  # noqa: E501
        :type: str
        """
        if terms_of_trade is not None and len(terms_of_trade) < 1:
            raise ValueError("Invalid value for `terms_of_trade`, length must be greater than or equal to `1`")  # noqa: E501

        self._terms_of_trade = terms_of_trade

    @property
    def commodities(self):
        """Gets the commodities of this Customs.  # noqa: E501

        The parcel content items  # noqa: E501

        :return: The commodities of this Customs.  # noqa: E501
        :rtype: list[Commodity]
        """
        return self._commodities

    @commodities.setter
    def commodities(self, commodities):
        """Sets the commodities of this Customs.

        The parcel content items  # noqa: E501

        :param commodities: The commodities of this Customs.  # noqa: E501
        :type: list[Commodity]
        """

        self._commodities = commodities

    @property
    def duty(self):
        """Gets the duty of this Customs.  # noqa: E501


        :return: The duty of this Customs.  # noqa: E501
        :rtype: Payment
        """
        return self._duty

    @duty.setter
    def duty(self, duty):
        """Sets the duty of this Customs.


        :param duty: The duty of this Customs.  # noqa: E501
        :type: Payment
        """

        self._duty = duty

    @property
    def invoice(self):
        """Gets the invoice of this Customs.  # noqa: E501


        :return: The invoice of this Customs.  # noqa: E501
        :rtype: Invoice
        """
        return self._invoice

    @invoice.setter
    def invoice(self, invoice):
        """Sets the invoice of this Customs.


        :param invoice: The invoice of this Customs.  # noqa: E501
        :type: Invoice
        """

        self._invoice = invoice

    @property
    def commercial_invoice(self):
        """Gets the commercial_invoice of this Customs.  # noqa: E501

        Indicates if the shipment is commercial  # noqa: E501

        :return: The commercial_invoice of this Customs.  # noqa: E501
        :rtype: bool
        """
        return self._commercial_invoice

    @commercial_invoice.setter
    def commercial_invoice(self, commercial_invoice):
        """Sets the commercial_invoice of this Customs.

        Indicates if the shipment is commercial  # noqa: E501

        :param commercial_invoice: The commercial_invoice of this Customs.  # noqa: E501
        :type: bool
        """

        self._commercial_invoice = commercial_invoice

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
        if issubclass(Customs, dict):
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
        if not isinstance(other, Customs):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
