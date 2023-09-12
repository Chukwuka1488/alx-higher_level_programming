#!/usr/bin/python3
"""
This module contains a class MyList that inherits from list.
"""


class MyList(list):
    """
    A class that inherits from list.

    This class includes a method for printing the list in sorted order.
    """

    def print_sorted(self):
        """
        Prints the list in ascending order.

        This method uses the built-in sorted function to return a new list
        that contains all elements of the original list in ascending order,
        and then prints this sorted list. The original list is not modified.
        """
        print(sorted(self))
