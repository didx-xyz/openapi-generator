# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from petstore_api.configuration import Configuration


class EnumTest(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'enum_string': 'str',
        'enum_string_required': 'str',
        'enum_integer': 'int',
        'enum_number': 'float',
        'outer_enum': 'OuterEnum',
        'outer_enum_integer': 'OuterEnumInteger',
        'outer_enum_default_value': 'OuterEnumDefaultValue',
        'outer_enum_integer_default_value': 'OuterEnumIntegerDefaultValue'
    }

    attribute_map = {
        'enum_string': 'enum_string',
        'enum_string_required': 'enum_string_required',
        'enum_integer': 'enum_integer',
        'enum_number': 'enum_number',
        'outer_enum': 'outerEnum',
        'outer_enum_integer': 'outerEnumInteger',
        'outer_enum_default_value': 'outerEnumDefaultValue',
        'outer_enum_integer_default_value': 'outerEnumIntegerDefaultValue'
    }

    def __init__(self, enum_string=None, enum_string_required=None, enum_integer=None, enum_number=None, outer_enum=None, outer_enum_integer=None, outer_enum_default_value=None, outer_enum_integer_default_value=None, local_vars_configuration=None):  # noqa: E501
        """EnumTest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._enum_string = None
        self._enum_string_required = None
        self._enum_integer = None
        self._enum_number = None
        self._outer_enum = None
        self._outer_enum_integer = None
        self._outer_enum_default_value = None
        self._outer_enum_integer_default_value = None
        self.discriminator = None

        if enum_string is not None:
            self.enum_string = enum_string
        self.enum_string_required = enum_string_required
        if enum_integer is not None:
            self.enum_integer = enum_integer
        if enum_number is not None:
            self.enum_number = enum_number
        self.outer_enum = outer_enum
        if outer_enum_integer is not None:
            self.outer_enum_integer = outer_enum_integer
        if outer_enum_default_value is not None:
            self.outer_enum_default_value = outer_enum_default_value
        if outer_enum_integer_default_value is not None:
            self.outer_enum_integer_default_value = outer_enum_integer_default_value

    @property
    def enum_string(self):
        """Gets the enum_string of this EnumTest.  # noqa: E501


        :return: The enum_string of this EnumTest.  # noqa: E501
        :rtype: str
        """
        return self._enum_string

    @enum_string.setter
    def enum_string(self, enum_string):
        """Sets the enum_string of this EnumTest.


        :param enum_string: The enum_string of this EnumTest.  # noqa: E501
        :type enum_string: str
        """
        allowed_values = ["UPPER", "lower", ""]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and enum_string not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `enum_string` ({0}), must be one of {1}"  # noqa: E501
                .format(enum_string, allowed_values)
            )

        self._enum_string = enum_string

    @property
    def enum_string_required(self):
        """Gets the enum_string_required of this EnumTest.  # noqa: E501


        :return: The enum_string_required of this EnumTest.  # noqa: E501
        :rtype: str
        """
        return self._enum_string_required

    @enum_string_required.setter
    def enum_string_required(self, enum_string_required):
        """Sets the enum_string_required of this EnumTest.


        :param enum_string_required: The enum_string_required of this EnumTest.  # noqa: E501
        :type enum_string_required: str
        """
        if self.local_vars_configuration.client_side_validation and enum_string_required is None:  # noqa: E501
            raise ValueError("Invalid value for `enum_string_required`, must not be `None`")  # noqa: E501
        allowed_values = ["UPPER", "lower", ""]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and enum_string_required not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `enum_string_required` ({0}), must be one of {1}"  # noqa: E501
                .format(enum_string_required, allowed_values)
            )

        self._enum_string_required = enum_string_required

    @property
    def enum_integer(self):
        """Gets the enum_integer of this EnumTest.  # noqa: E501


        :return: The enum_integer of this EnumTest.  # noqa: E501
        :rtype: int
        """
        return self._enum_integer

    @enum_integer.setter
    def enum_integer(self, enum_integer):
        """Sets the enum_integer of this EnumTest.


        :param enum_integer: The enum_integer of this EnumTest.  # noqa: E501
        :type enum_integer: int
        """
        allowed_values = [1, -1]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and enum_integer not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `enum_integer` ({0}), must be one of {1}"  # noqa: E501
                .format(enum_integer, allowed_values)
            )

        self._enum_integer = enum_integer

    @property
    def enum_number(self):
        """Gets the enum_number of this EnumTest.  # noqa: E501


        :return: The enum_number of this EnumTest.  # noqa: E501
        :rtype: float
        """
        return self._enum_number

    @enum_number.setter
    def enum_number(self, enum_number):
        """Sets the enum_number of this EnumTest.


        :param enum_number: The enum_number of this EnumTest.  # noqa: E501
        :type enum_number: float
        """
        allowed_values = [1.1, -1.2]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and enum_number not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `enum_number` ({0}), must be one of {1}"  # noqa: E501
                .format(enum_number, allowed_values)
            )

        self._enum_number = enum_number

    @property
    def outer_enum(self):
        """Gets the outer_enum of this EnumTest.  # noqa: E501


        :return: The outer_enum of this EnumTest.  # noqa: E501
        :rtype: OuterEnum
        """
        return self._outer_enum

    @outer_enum.setter
    def outer_enum(self, outer_enum):
        """Sets the outer_enum of this EnumTest.


        :param outer_enum: The outer_enum of this EnumTest.  # noqa: E501
        :type outer_enum: OuterEnum
        """

        self._outer_enum = outer_enum

    @property
    def outer_enum_integer(self):
        """Gets the outer_enum_integer of this EnumTest.  # noqa: E501


        :return: The outer_enum_integer of this EnumTest.  # noqa: E501
        :rtype: OuterEnumInteger
        """
        return self._outer_enum_integer

    @outer_enum_integer.setter
    def outer_enum_integer(self, outer_enum_integer):
        """Sets the outer_enum_integer of this EnumTest.


        :param outer_enum_integer: The outer_enum_integer of this EnumTest.  # noqa: E501
        :type outer_enum_integer: OuterEnumInteger
        """

        self._outer_enum_integer = outer_enum_integer

    @property
    def outer_enum_default_value(self):
        """Gets the outer_enum_default_value of this EnumTest.  # noqa: E501


        :return: The outer_enum_default_value of this EnumTest.  # noqa: E501
        :rtype: OuterEnumDefaultValue
        """
        return self._outer_enum_default_value

    @outer_enum_default_value.setter
    def outer_enum_default_value(self, outer_enum_default_value):
        """Sets the outer_enum_default_value of this EnumTest.


        :param outer_enum_default_value: The outer_enum_default_value of this EnumTest.  # noqa: E501
        :type outer_enum_default_value: OuterEnumDefaultValue
        """

        self._outer_enum_default_value = outer_enum_default_value

    @property
    def outer_enum_integer_default_value(self):
        """Gets the outer_enum_integer_default_value of this EnumTest.  # noqa: E501


        :return: The outer_enum_integer_default_value of this EnumTest.  # noqa: E501
        :rtype: OuterEnumIntegerDefaultValue
        """
        return self._outer_enum_integer_default_value

    @outer_enum_integer_default_value.setter
    def outer_enum_integer_default_value(self, outer_enum_integer_default_value):
        """Sets the outer_enum_integer_default_value of this EnumTest.


        :param outer_enum_integer_default_value: The outer_enum_integer_default_value of this EnumTest.  # noqa: E501
        :type outer_enum_integer_default_value: OuterEnumIntegerDefaultValue
        """

        self._outer_enum_integer_default_value = outer_enum_integer_default_value

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, EnumTest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EnumTest):
            return True

        return self.to_dict() != other.to_dict()
