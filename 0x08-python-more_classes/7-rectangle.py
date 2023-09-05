#!/usr/bin/python3
"""Module that defines a Rectangle class"""


class Rectangle:
    """Class that defines a rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle instance

        Args:
            width (int): Width of the rectangle
            height (int): Height of the rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Get the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle

        Args:
            value (int): New width of the rectangle

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle

        Args:
            value (int): New height of the rectangle

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Calculate the perimeter of the rectangle"""
        if self.width == 0 or self.height == 0:
            return 0

        return (self.width + self.height) * 2

    def __str__(self):
        """Return a string representation of the rectangle"""
        if self.width == 0 or self.height == 0:
            return ""

        rectangle = ""
        for i in range(self.height):
            rectangle += str(self.print_symbol) * self.width + "\n"
        return rectangle.rstrip()

    def __repr__(self):
        """Return a formal representation of the rectangle"""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Print a message when an instance of Rectangle is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
