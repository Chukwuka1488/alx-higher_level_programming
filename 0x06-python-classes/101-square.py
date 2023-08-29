#!/usr/bin/python3
"""Defines a class Square"""

class Square:
    """Square class with private instance attributes size and position,
        validation, area method, print method, getters/setters,
        and __str__ method
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square object with size and position validation

        Args:
            size (int): The size of the new square, must be an integer >= 0.
            position (tuple): The position of the new square, must be a tuple
            of 2 positive integers.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation

        Args:
            value (int): The new size of the square, must be an integer >= 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get the position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square with validation

        Args:
            value (tuple): The new position of the square, must be a tuple of
            2 positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
           not isinstance(value[0], int) or not isinstance(value[1], int) or \
           value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current square area"""
        return self.__size ** 2

    def my_print(self):
        """Print the square using the # character"""
        print(str(self))

    def __str__(self):
        """Return a string representation of the Square"""
        if self.__size == 0:
            return ""
        result = "\n" * self.__position[1]
        for i in range(self.__size):
            result += " " * self.__position[0] + "#" * self.__size + "\n"
        return result[:-1]
