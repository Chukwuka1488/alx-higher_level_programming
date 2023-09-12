#!/usr/bin/python3
"""
This module reads stdin line by line and computes metrics.
"""

import sys

def print_stats(status_codes, file_size):
    """
    Function that prints the total file size and the number of lines for
    each status code.

    Args:
        status_codes (dict): A dictionary with status codes as keys and their
        counts as values.
        file_size (int): The total file size.

    Returns:
        None
    """
    print("File size: {:d}".format(file_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{:s}: {:d}".format(code, status_codes[code]))

status_codes = {"200": 0, "301": 0, "400": 0, "401": 0,
                "403": 0, "404": 0, "405": 0, "500": 0}
file_size = 0
lines = 0

try:
    for line in sys.stdin:
        split_line = line.split()
        if len(split_line) < 2:
            continue
        if split_line[-2] in status_codes:
            status_codes[split_line[-2]] += 1
        file_size += int(split_line[-1])
        lines += 1
        if lines % 10 == 0:
            print_stats(status_codes, file_size)
except KeyboardInterrupt:
    print_stats(status_codes, file_size)
    raise
print_stats(status_codes, file_size)
