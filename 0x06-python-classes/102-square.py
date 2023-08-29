#!/usr/bin/python3
class Square:
    """Square class with private instance attribute size, validation,
        area method, getter/setter, and comparison methods
    """

    def __init__(self, size=0):
        """Initialize a new Square object with size validation

        Args:
            size (int or float): The size of the new square, must be a
            number >= 0.
        """
        self.size = size

    @property
    def size(self):
        """Get the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation

        Args:
            value (int or float): The new size of the square, must be a
            number >= 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current square area"""
        return self.__size ** 2

    def __eq__(self, other):
        """Check if two squares are equal based on their area"""
        return isinstance(other, Square) and self.area() == other.area()

    def __ne__(self, other):
        """Check if two squares are not equal based on their area"""
        return not self == other

    def __lt__(self, other):
        """Check if this square is less than another square based on their
        area
        """
        return isinstance(other, Square) and self.area() < other.area()

    def __le__(self, other):
        """Check if this square is less than or equal to another square based on
        their area
        """
        return isinstance(other, Square) and self.area() <= other.area()

    def __gt__(self, other):
        """Check if this square is greater than another square based on
        their area
        """
        return isinstance(other, Square) and self.area() > other.area()

    def __ge__(self, other):
        """Check if this square is greater than or equal to another square
        based on their area
        """
        return isinstance(other, Square) and self.area() >= other.area()
