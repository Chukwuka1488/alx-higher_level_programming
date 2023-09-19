#!/usr/bin/python3
""" This module defines the Rectangle class that inherits from Base. """

from models.base import Base


class Rectangle(Base):
    """ Represents a rectangle, inherits from Base. """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initializes the rectangle. """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Gets the width. """
        return self.__width

    @width.setter
    def width(self, value):
        """ Sets the width. """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Gets the height. """
        return self.__height

    @height.setter
    def height(self, value):
        """ Sets the height. """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ Gets x. """
        return self.__x

    @x.setter
    def x(self, value):
        """ Sets x. """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Gets y. """
        return self.__y

    @y.setter
    def y(self, value):
        """ Sets y. """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Returns the area of the rectangle. """
        return self.width * self.height

    def display(self):
        """ Displays the rectangle using the '#' character. """
        for _ in range(self.height):
            print("#" * self.width)

    def __str__(self):
        """
        Overrides the default string representation for the Rectangle instances.
        """
        return ("[Rectangle] ({}) {}/{} - {}/{}"
                .format(self.id, self.x, self.y, self.width, self.height))

    def display(self):
        """
        Prints the Rectangle instance with the character '#' taking care of
        x and y.
        """
        # print vertical offset
        for _ in range(self.y):
            print()

        # print the rectangle
        for _ in range(self.height):
            # print horizontal offset
            print(' ' * self.x, end='')

            # print the rectangle's width
            print('#' * self.width)

    def update(self, *args):
        """
        Assigns an argument to each attribute.
        """
        attributes = ['id', 'width', 'height', 'x', 'y']

        for i, arg in enumerate(args):
            if i < len(attributes):
                setattr(self, attributes[i], arg)

    def update(self, *args, **kwargs):
        # List of attributes for clarity
        attributes = ["id", "width", "height", "x", "y"]

        # If args exist and are not empty, use args
        if args and len(args) > 0:
            for i, value in enumerate(args):
                if i < len(attributes):
                    setattr(self, attributes[i], value)
        # If args are not provided or empty, use kwargs
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):  # Make sure the attribute exists
                    setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of the Rectangle."""
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
