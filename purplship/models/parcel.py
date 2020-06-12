# coding: utf-8

"""
    PurplShip Multi-carrier API

    PurplShip is a Multi-carrier Shipping API that simplifies the integration of logistic carrier services  # noqa: E501

    OpenAPI spec version: v1
    Contact: hello@purplship.com
    Generated by: https://github.com/purplship-api/purplship-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Parcel(object):
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
        'weight': 'float',
        'width': 'float',
        'height': 'float',
        'length': 'float',
        'packaging_type': 'str',
        'package_preset': 'str',
        'description': 'str',
        'content': 'str',
        'is_document': 'bool',
        'weight_unit': 'str',
        'dimension_unit': 'str'
    }

    attribute_map = {
        'id': 'id',
        'weight': 'weight',
        'width': 'width',
        'height': 'height',
        'length': 'length',
        'packaging_type': 'packagingType',
        'package_preset': 'packagePreset',
        'description': 'description',
        'content': 'content',
        'is_document': 'isDocument',
        'weight_unit': 'weightUnit',
        'dimension_unit': 'dimensionUnit'
    }

    def __init__(self, id=None, weight=None, width=None, height=None, length=None, packaging_type=None, package_preset=None, description=None, content=None, is_document=None, weight_unit=None, dimension_unit=None):  # noqa: E501
        """Parcel - a model defined in PurplShip"""  # noqa: E501

        self._id = None
        self._weight = None
        self._width = None
        self._height = None
        self._length = None
        self._packaging_type = None
        self._package_preset = None
        self._description = None
        self._content = None
        self._is_document = None
        self._weight_unit = None
        self._dimension_unit = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if weight is not None:
            self.weight = weight
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if length is not None:
            self.length = length
        if packaging_type is not None:
            self.packaging_type = packaging_type
        if package_preset is not None:
            self.package_preset = package_preset
        if description is not None:
            self.description = description
        if content is not None:
            self.content = content
        if is_document is not None:
            self.is_document = is_document
        if weight_unit is not None:
            self.weight_unit = weight_unit
        if dimension_unit is not None:
            self.dimension_unit = dimension_unit

    @property
    def id(self):
        """Gets the id of this Parcel.  # noqa: E501

        A unique parcel identifier  # noqa: E501

        :return: The id of this Parcel.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Parcel.

        A unique parcel identifier  # noqa: E501

        :param id: The id of this Parcel.  # noqa: E501
        :type: str
        """
        if id is not None and len(id) < 1:
            raise ValueError("Invalid value for `id`, length must be greater than or equal to `1`")  # noqa: E501

        self._id = id

    @property
    def weight(self):
        """Gets the weight of this Parcel.  # noqa: E501

        The parcel's weight  # noqa: E501

        :return: The weight of this Parcel.  # noqa: E501
        :rtype: float
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this Parcel.

        The parcel's weight  # noqa: E501

        :param weight: The weight of this Parcel.  # noqa: E501
        :type: float
        """

        self._weight = weight

    @property
    def width(self):
        """Gets the width of this Parcel.  # noqa: E501

        The parcel's width  # noqa: E501

        :return: The width of this Parcel.  # noqa: E501
        :rtype: float
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this Parcel.

        The parcel's width  # noqa: E501

        :param width: The width of this Parcel.  # noqa: E501
        :type: float
        """

        self._width = width

    @property
    def height(self):
        """Gets the height of this Parcel.  # noqa: E501

        The parcel's height  # noqa: E501

        :return: The height of this Parcel.  # noqa: E501
        :rtype: float
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this Parcel.

        The parcel's height  # noqa: E501

        :param height: The height of this Parcel.  # noqa: E501
        :type: float
        """

        self._height = height

    @property
    def length(self):
        """Gets the length of this Parcel.  # noqa: E501

        The parcel's length  # noqa: E501

        :return: The length of this Parcel.  # noqa: E501
        :rtype: float
        """
        return self._length

    @length.setter
    def length(self, length):
        """Sets the length of this Parcel.

        The parcel's length  # noqa: E501

        :param length: The length of this Parcel.  # noqa: E501
        :type: float
        """

        self._length = length

    @property
    def packaging_type(self):
        """Gets the packaging_type of this Parcel.  # noqa: E501

         The parcel's packaging type.  Note that the packaging is optional when using a package preset  For specific carriers packaging type, please consult the reference.   # noqa: E501

        :return: The packaging_type of this Parcel.  # noqa: E501
        :rtype: str
        """
        return self._packaging_type

    @packaging_type.setter
    def packaging_type(self, packaging_type):
        """Sets the packaging_type of this Parcel.

         The parcel's packaging type.  Note that the packaging is optional when using a package preset  For specific carriers packaging type, please consult the reference.   # noqa: E501

        :param packaging_type: The packaging_type of this Parcel.  # noqa: E501
        :type: str
        """
        allowed_values = ["envelope", "pak", "tube", "pallet", "small_box", "medium_box", "your_packaging"]  # noqa: E501
        if packaging_type not in allowed_values:
            raise ValueError(
                "Invalid value for `packaging_type` ({0}), must be one of {1}"  # noqa: E501
                .format(packaging_type, allowed_values)
            )

        self._packaging_type = packaging_type

    @property
    def package_preset(self):
        """Gets the package_preset of this Parcel.  # noqa: E501

         The parcel's package preset.  For specific carriers package preset, please consult the reference.   # noqa: E501

        :return: The package_preset of this Parcel.  # noqa: E501
        :rtype: str
        """
        return self._package_preset

    @package_preset.setter
    def package_preset(self, package_preset):
        """Sets the package_preset of this Parcel.

         The parcel's package preset.  For specific carriers package preset, please consult the reference.   # noqa: E501

        :param package_preset: The package_preset of this Parcel.  # noqa: E501
        :type: str
        """
        if package_preset is not None and len(package_preset) < 1:
            raise ValueError("Invalid value for `package_preset`, length must be greater than or equal to `1`")  # noqa: E501

        self._package_preset = package_preset

    @property
    def description(self):
        """Gets the description of this Parcel.  # noqa: E501

        The parcel's description  # noqa: E501

        :return: The description of this Parcel.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Parcel.

        The parcel's description  # noqa: E501

        :param description: The description of this Parcel.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) < 1:
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `1`")  # noqa: E501

        self._description = description

    @property
    def content(self):
        """Gets the content of this Parcel.  # noqa: E501

        The parcel's content description  # noqa: E501

        :return: The content of this Parcel.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this Parcel.

        The parcel's content description  # noqa: E501

        :param content: The content of this Parcel.  # noqa: E501
        :type: str
        """
        if content is not None and len(content) < 1:
            raise ValueError("Invalid value for `content`, length must be greater than or equal to `1`")  # noqa: E501

        self._content = content

    @property
    def is_document(self):
        """Gets the is_document of this Parcel.  # noqa: E501

        Indicates if the parcel is composed of documents only  # noqa: E501

        :return: The is_document of this Parcel.  # noqa: E501
        :rtype: bool
        """
        return self._is_document

    @is_document.setter
    def is_document(self, is_document):
        """Sets the is_document of this Parcel.

        Indicates if the parcel is composed of documents only  # noqa: E501

        :param is_document: The is_document of this Parcel.  # noqa: E501
        :type: bool
        """

        self._is_document = is_document

    @property
    def weight_unit(self):
        """Gets the weight_unit of this Parcel.  # noqa: E501

        The parcel's weight unit  # noqa: E501

        :return: The weight_unit of this Parcel.  # noqa: E501
        :rtype: str
        """
        return self._weight_unit

    @weight_unit.setter
    def weight_unit(self, weight_unit):
        """Sets the weight_unit of this Parcel.

        The parcel's weight unit  # noqa: E501

        :param weight_unit: The weight_unit of this Parcel.  # noqa: E501
        :type: str
        """
        allowed_values = ["KG", "LB"]  # noqa: E501
        if weight_unit not in allowed_values:
            raise ValueError(
                "Invalid value for `weight_unit` ({0}), must be one of {1}"  # noqa: E501
                .format(weight_unit, allowed_values)
            )

        self._weight_unit = weight_unit

    @property
    def dimension_unit(self):
        """Gets the dimension_unit of this Parcel.  # noqa: E501

        The parcel's dimension unit  # noqa: E501

        :return: The dimension_unit of this Parcel.  # noqa: E501
        :rtype: str
        """
        return self._dimension_unit

    @dimension_unit.setter
    def dimension_unit(self, dimension_unit):
        """Sets the dimension_unit of this Parcel.

        The parcel's dimension unit  # noqa: E501

        :param dimension_unit: The dimension_unit of this Parcel.  # noqa: E501
        :type: str
        """
        allowed_values = ["CM", "IN"]  # noqa: E501
        if dimension_unit not in allowed_values:
            raise ValueError(
                "Invalid value for `dimension_unit` ({0}), must be one of {1}"  # noqa: E501
                .format(dimension_unit, allowed_values)
            )

        self._dimension_unit = dimension_unit

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
        if issubclass(Parcel, dict):
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
        if not isinstance(other, Parcel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other