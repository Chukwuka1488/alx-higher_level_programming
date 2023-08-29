#!/usr/bin/python3
"""Defines a class Square"""

class Square:
    """Square class with private instance attribute size

    Attributes:
        size: size of a square (1 side).
    """

    def __init__(self, size):
        """Initialize a new Square object

        Args:
            size (int): The size of the new square.
        """
        self.__size = size
