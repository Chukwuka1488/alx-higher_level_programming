#!/usr/bin/python3
"""Defines a class Square"""

class Square:
    """Square class with private instance attribute size and validation

    Attributes:
        size: size of a square (1 side).
    """

    def __init__(self, size=0):
        """Initialize a new Square object with size validation

        Args:
            size (int): The size of the new square, must be an integer >= 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
