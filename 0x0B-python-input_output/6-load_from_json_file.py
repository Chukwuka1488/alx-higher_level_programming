#!/usr/bin/python3
"""
This module contains a function that creates an Object from a “JSON file”.
"""

import json


def load_from_json_file(filename):
    """
    Function that creates an Object from a “JSON file”.
    
    Args:
        filename (str): The name of the file.

    Returns:
        The Python data structure represented by the JSON string in the file.
    """
    with open(filename, 'r') as f:
        return json.load(f)
