#!/bin/bash
# This script takes a URL as an argument, sends a request to that URL, and displays all HTTP methods the server will accept.
curl -s -I "${1}" | grep "^Allow: .*" | cut -d " " -f 2-