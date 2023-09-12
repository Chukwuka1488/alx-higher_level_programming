#!/usr/bin/python3
"""
This module contains a function that returns the list of available attributes
and methods of an object.
"""


def lookup(obj):
    """
    Function to return a list of valid attributes and methods for an object.

    Args:
        obj: The object to inspect.

    Returns:
        A list of the names of the object's attributes and methods.
    """
    return dir(obj)
