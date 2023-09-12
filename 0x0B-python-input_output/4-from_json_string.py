#!/usr/bin/python3
"""
This module contains a function that returns an object (Python data structure) 
represented by a JSON string.
"""

import json


def from_json_string(my_str):
    """
    Function that returns an object (Python data structure) represented by a
    JSON string.

    Args:
        my_str (str): The JSON string representation of the Python data
        structure.

    Returns:
        The Python data structure represented by my_str.
    """
    return json.loads(my_str)

