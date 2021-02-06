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

class Customs(object):
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
        'id': 'str',
        'aes': 'str',
        'eel_pfc': 'str',
        'content_type': 'str',
        'content_description': 'str',
        'incoterm': 'str',
        'commodities': 'list[Commodity]',
        'duty': 'Payment',
        'invoice': 'str',
        'commercial_invoice': 'bool',
        'certify': 'bool',
        'signer': 'str',
        'certificate_number': 'str',
        'options': 'object'
    }

    attribute_map = {
        'id': 'id',
        'aes': 'aes',
        'eel_pfc': 'eel_pfc',
        'content_type': 'content_type',
        'content_description': 'content_description',
        'incoterm': 'incoterm',
        'commodities': 'commodities',
        'duty': 'duty',
        'invoice': 'invoice',
        'commercial_invoice': 'commercial_invoice',
        'certify': 'certify',
        'signer': 'signer',
        'certificate_number': 'certificate_number',
        'options': 'options'
    }

    def __init__(self, id=None, aes=None, eel_pfc=None, content_type=None, content_description=None, incoterm=None, commodities=None, duty=None, invoice=None, commercial_invoice=None, certify=None, signer=None, certificate_number=None, options=None):  # noqa: E501
        """Customs - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._aes = None
        self._eel_pfc = None
        self._content_type = None
        self._content_description = None
        self._incoterm = None
        self._commodities = None
        self._duty = None
        self._invoice = None
        self._commercial_invoice = None
        self._certify = None
        self._signer = None
        self._certificate_number = None
        self._options = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if aes is not None:
            self.aes = aes
        if eel_pfc is not None:
            self.eel_pfc = eel_pfc
        if content_type is not None:
            self.content_type = content_type
        if content_description is not None:
            self.content_description = content_description
        if incoterm is not None:
            self.incoterm = incoterm
        if commodities is not None:
            self.commodities = commodities
        if duty is not None:
            self.duty = duty
        if invoice is not None:
            self.invoice = invoice
        if commercial_invoice is not None:
            self.commercial_invoice = commercial_invoice
        if certify is not None:
            self.certify = certify
        if signer is not None:
            self.signer = signer
        if certificate_number is not None:
            self.certificate_number = certificate_number
        if options is not None:
            self.options = options

    @property
    def id(self):
        """Gets the id of this Customs.  # noqa: E501

        A unique identifier  # noqa: E501

        :return: The id of this Customs.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Customs.

        A unique identifier  # noqa: E501

        :param id: The id of this Customs.  # noqa: E501
        :type: str
        """

        self._id = id

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

        self._aes = aes

    @property
    def eel_pfc(self):
        """Gets the eel_pfc of this Customs.  # noqa: E501


        :return: The eel_pfc of this Customs.  # noqa: E501
        :rtype: str
        """
        return self._eel_pfc

    @eel_pfc.setter
    def eel_pfc(self, eel_pfc):
        """Sets the eel_pfc of this Customs.


        :param eel_pfc: The eel_pfc of this Customs.  # noqa: E501
        :type: str
        """

        self._eel_pfc = eel_pfc

    @property
    def content_type(self):
        """Gets the content_type of this Customs.  # noqa: E501


        :return: The content_type of this Customs.  # noqa: E501
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """Sets the content_type of this Customs.


        :param content_type: The content_type of this Customs.  # noqa: E501
        :type: str
        """
        allowed_values = ["documents", "gift", "sample", "merchandise", "return_merchandise", "other"]  # noqa: E501
        if content_type not in allowed_values:
            raise ValueError(
                "Invalid value for `content_type` ({0}), must be one of {1}"  # noqa: E501
                .format(content_type, allowed_values)
            )

        self._content_type = content_type

    @property
    def content_description(self):
        """Gets the content_description of this Customs.  # noqa: E501


        :return: The content_description of this Customs.  # noqa: E501
        :rtype: str
        """
        return self._content_description

    @content_description.setter
    def content_description(self, content_description):
        """Sets the content_description of this Customs.


        :param content_description: The content_description of this Customs.  # noqa: E501
        :type: str
        """

        self._content_description = content_description

    @property
    def incoterm(self):
        """Gets the incoterm of this Customs.  # noqa: E501

        The customs 'term of trade' also known as 'incoterm'  # noqa: E501

        :return: The incoterm of this Customs.  # noqa: E501
        :rtype: str
        """
        return self._incoterm

    @incoterm.setter
    def incoterm(self, incoterm):
        """Sets the incoterm of this Customs.

        The customs 'term of trade' also known as 'incoterm'  # noqa: E501

        :param incoterm: The incoterm of this Customs.  # noqa: E501
        :type: str
        """
        allowed_values = ["CFR", "CIF", "CIP", "CPT", "DAF", "DDP", "DDU", "DEQ", "DES", "EXW", "FAS", "FCA", "FOB"]  # noqa: E501
        if incoterm not in allowed_values:
            raise ValueError(
                "Invalid value for `incoterm` ({0}), must be one of {1}"  # noqa: E501
                .format(incoterm, allowed_values)
            )

        self._incoterm = incoterm

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

        The invoice reference number  # noqa: E501

        :return: The invoice of this Customs.  # noqa: E501
        :rtype: str
        """
        return self._invoice

    @invoice.setter
    def invoice(self, invoice):
        """Sets the invoice of this Customs.

        The invoice reference number  # noqa: E501

        :param invoice: The invoice of this Customs.  # noqa: E501
        :type: str
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

    @property
    def certify(self):
        """Gets the certify of this Customs.  # noqa: E501

        Indicate that signer certified confirmed all  # noqa: E501

        :return: The certify of this Customs.  # noqa: E501
        :rtype: bool
        """
        return self._certify

    @certify.setter
    def certify(self, certify):
        """Sets the certify of this Customs.

        Indicate that signer certified confirmed all  # noqa: E501

        :param certify: The certify of this Customs.  # noqa: E501
        :type: bool
        """

        self._certify = certify

    @property
    def signer(self):
        """Gets the signer of this Customs.  # noqa: E501


        :return: The signer of this Customs.  # noqa: E501
        :rtype: str
        """
        return self._signer

    @signer.setter
    def signer(self, signer):
        """Sets the signer of this Customs.


        :param signer: The signer of this Customs.  # noqa: E501
        :type: str
        """

        self._signer = signer

    @property
    def certificate_number(self):
        """Gets the certificate_number of this Customs.  # noqa: E501


        :return: The certificate_number of this Customs.  # noqa: E501
        :rtype: str
        """
        return self._certificate_number

    @certificate_number.setter
    def certificate_number(self, certificate_number):
        """Sets the certificate_number of this Customs.


        :param certificate_number: The certificate_number of this Customs.  # noqa: E501
        :type: str
        """

        self._certificate_number = certificate_number

    @property
    def options(self):
        """Gets the options of this Customs.  # noqa: E501


        :return: The options of this Customs.  # noqa: E501
        :rtype: object
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this Customs.


        :param options: The options of this Customs.  # noqa: E501
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
