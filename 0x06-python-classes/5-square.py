#!/usr/bin/python3
"""Defines a class Square"""

class Square:
    """Square class with private instance attribute size, validation, area
        method, getter/setter, and print method
    """

    def __init__(self, size=0):
        """Initialize a new Square object with size validation

        Args:
            size (int): The size of the new square, must be an integer >= 0.
        """
        self.set_size(size)

    def get_size(self):
        """Get the size of the square"""
        return self.__size

    def set_size(self, value):
        """Set the size of the square with validation

        Args:
            value (int): The new size of the square, must be an integer >= 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    size = property(get_size, set_size)

    def area(self):
        """Return the current square area"""
        return self.get_size() ** 2

    def my_print(self):
        """Print the square using the # character"""
        if self.get_size() == 0:
            print()
        else:
            for i in range(self.get_size()):
                print("#" * self.get_size())

