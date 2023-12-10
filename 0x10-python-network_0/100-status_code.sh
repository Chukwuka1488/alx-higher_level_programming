#!/bin/bash
# This script takes a URL as an argument, sends a request to that URL, and displays only the status code of the response.
curl -so /dev/null -w "%{http_code}" "$1"