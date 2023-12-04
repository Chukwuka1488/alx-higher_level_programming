#!/bin/bash
# This script takes a URL as an argument, sends a GET request to that URL with a header variable, and displays the body of the response.
url=$1
curl -s -H "X-School-User-Id: 98" "$url"