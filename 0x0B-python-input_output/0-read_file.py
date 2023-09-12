#!/usr/bin/python3
"""
This module contains the function read_file which reads a text file (UTF8) and
prints it to stdout.
"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints it to stdout.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end="")

