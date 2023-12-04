#!/bin/bash
# This script takes a URL as an argument, sends a DELETE request to that URL, and displays the body of the response.

url=$1
curl -s -X DELETE "$url"
