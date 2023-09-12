#!/usr/bin/python3
"""
This module contains a class BaseGeometry with a method that raises an exception.
"""


class BaseGeometry:
    """
    A class with a method that raises an exception.
    """

    def area(self):
        """
        A method that raises an exception.

        Raises:
            Exception: Always, with the message "area() is not implemented"
        """
        raise Exception("area() is not implemented")
