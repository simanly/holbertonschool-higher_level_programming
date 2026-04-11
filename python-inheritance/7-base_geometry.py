#!/usr/bin/python3
"""Module that defines a BaseGeometry class."""


class BaseGeometry:
    """Class representing BaseGeometry."""

    def area(self):
        """Method that raises an Exception (not implemented)."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method that validates value as an integer.

        Args:
            name (str): The name of the parameter.
            value (int): The parameter to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

