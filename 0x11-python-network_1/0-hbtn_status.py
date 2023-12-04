#!/usr/bin/env python3
"""
This module fetches https://alx-intranet.hbtn.io/status using urllib
"""

import urllib.request

with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    """
    Fetches the URL and reads the response
    """
    html = response.read()
    print("Body response:")
    print("\t- type: {}".format(type(html)))
    print("\t- content: {}".format(html))
    print("\t- utf8 content: {}".format(html.decode('utf-8')))