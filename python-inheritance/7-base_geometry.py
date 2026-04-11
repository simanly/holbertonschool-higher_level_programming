#!/usr/bin/python3
"""
This module contains a class called BaseGeometry.
It provides basic geometry functions including area and integer validation.
"""


class BaseGeometry:
    """A class used to represent base geometry objects."""

    def area(self):
        """
        Public instance method that raises an Exception.
        Message: 'area() is not implemented'.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that 'value' is a positive integer.
        Args:
            name (str): The name of the value, always a string.
            value (int): The value to be validated as an integer.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
