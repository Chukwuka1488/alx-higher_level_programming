#!/usr/bin/python3
"""
This module contains the function add_attribute which adds a new attribute to an object if it's possible.
"""

def add_attribute(obj, name, value):
    """
    Adds a new attribute to an object if it's possible.
    Raises a TypeError exception, with the message "can't add new attribute" if the object can't have new attribute.
    """
    if hasattr(obj, '__dict__'):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
