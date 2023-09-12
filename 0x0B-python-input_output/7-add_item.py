#!/usr/bin/python3
"""
This script adds all arguments to a Python list, and then saves them to a file.
"""


import sys
import json


def save_to_json_file(my_obj, filename):
    with open(filename, 'w') as f:
        json.dump(my_obj, f)

def load_from_json_file(filename):
    with open(filename, 'r') as f:
        return json.load(f)

filename = "add_item.json"

try:
    my_list = load_from_json_file(filename)
except FileNotFoundError:
    my_list = []

my_list.extend(sys.argv[1:])

save_to_json_file(my_list, filename)
