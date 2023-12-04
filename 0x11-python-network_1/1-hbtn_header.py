#!/usr/bin/env python3
"""
This module sends a request to a URL and displays the value of the X-Request-Id variable
"""

import urllib.request
import sys

with urllib.request.urlopen(sys.argv[1]) as response:
    """
    Sends a request to the URL and reads the response
    """
    print(response.getheader('X-Request-Id'))