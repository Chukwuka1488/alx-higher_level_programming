#!/usr/bin/python3
"""
This module contains a function that writes an Object to a text file, 
using a JSON representation.
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Function that writes an Object to a text file, using a JSON representation.
    
    Args:
        my_obj: The Python data structure to be written to the file.
        filename (str): The name of the file.

    Returns:
        None
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
