#!/usr/bin/python3
class Square:
    """Square class with private instance attribute size"""

    def __init__(self, size):
        """Initialize a new Square object

        Args:
            size (int): The size of the new square.
        """
        self.__size = size
