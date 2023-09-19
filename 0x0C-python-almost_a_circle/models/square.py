#!/usr/bin/python3
""" This module defines the Square class that inherits from Rectangle. """

from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        """ Initialize a Square """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Return the string representation of a Square """
        return ("[Square] ({}) {}/{} - {}"
                .format(self.id, self.x, self.y, self.width))

    @property
    def size(self):
        """ Get the size of the Square """
        return self.width

    @size.setter
    def size(self, value):
        """ Set the size of the Square """

        # Check if the value is an integer
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        # Check if the value is greater than 0
        if value <= 0:
            raise ValueError("width must be > 0")

        # Set both width and height as they are the same for a square
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assigns attributes using *args or **kwargs."""
        attributes = ["id", "size", "x", "y"]

        if args and len(args) > 0:
            for i, value in enumerate(args):
                if i < len(attributes):
                    if attributes[i] == "size":
                        self.width = value
                        self.height = value
                    else:
                        setattr(self, attributes[i], value)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    if key == "size":
                        self.width = value
                        self.height = value
                    else:
                        setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of the Rectangle."""
        return {
            'id': self.id,
            'size': self.width,
            'x': self.x,
            'y': self.y
        }
