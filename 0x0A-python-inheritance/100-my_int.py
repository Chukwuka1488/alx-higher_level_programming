#!/usr/bin/python3
"""
This module contains the class MyInt which inherits from int.
MyInt is a rebel. It has == and != operators inverted.
"""


class MyInt(int):
    """
    A class MyInt that inherits from int.
    """

    def __eq__(self, other):
        """
        Overrides the == operator with != operator.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Overrides the != operator with == operator.
        """
        return super().__eq__(other)
