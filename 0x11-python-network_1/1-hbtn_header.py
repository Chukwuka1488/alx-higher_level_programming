#!/usr/bin/env python3
"""
This module sends a request to a URL and displays the value of the X-Request-Id variable
"""

from urllib.request import Request, urlopen
from sys import argv


if __name__ == "__main__":
    """
    Sends a request to the URL and reads the response
    """
    response = Request(argv[1])
    with urlopen(response) as res:
        headers = res.info()
        print(headers.get('X-Request-Id'))