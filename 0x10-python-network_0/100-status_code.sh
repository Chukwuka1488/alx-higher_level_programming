#!/usr/bin/env bash
# This script takes a URL as an argument, sends a request to that URL, and displays only the status code of the response.

url=$1
curl -s -o /dev/null -w "%{http_code}" "$url"