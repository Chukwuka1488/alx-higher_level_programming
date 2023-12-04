#!/usr/bin/env python3
"""
This module sends a POST request to a URL with an email as a parameter
"""

import urllib.request
import urllib.parse
import sys

data = urllib.parse.urlencode({'email': sys.argv[2]})
data = data.encode('ascii')
req = urllib.request.Request(sys.argv[1], data)

with urllib.request.urlopen(req) as response:
    """
    Sends a POST request to the URL and reads the response
    """
    print(response.read().decode('utf-8'))