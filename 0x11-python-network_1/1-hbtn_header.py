#!/usr/bin/python3
"""
This module sends a request to a URL and displays the value of the X-Request-Id variable
"""


if __name__ == "__main__":
    """
    Sends a request to the URL and reads the response
    """
    import urllib.request 
    import sys
    
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.headers["X-Request-Id"])