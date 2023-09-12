#!/usr/bin/python3
"""
This module contains a class BaseGeometry with two methods.
"""


class BaseGeometry:
    """
    A class with two methods: one that raises an exception and another that
    validates an integer.
    """

    def area(self):
        """
        A method that raises an exception.

        Raises:
            Exception: Always, with the message "area() is not implemented"
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        A method that validates an integer.

        Args:
            name: The name of the value, assumed to be a string.
            value: The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
