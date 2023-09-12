#!/usr/bin/python3
"""
This module contains a function that checks if an object is exactly an instance
of the specified class.
"""


def is_same_class(obj, a_class):
    """
    Function to check if an object is exactly an instance of the specified
    class.

    Args:
        obj: The object to check.
        a_class: The class to check against.

    Returns:
        True if the object is exactly an instance of the specified class,
        False otherwise.
    """
    return type(obj) is a_class

