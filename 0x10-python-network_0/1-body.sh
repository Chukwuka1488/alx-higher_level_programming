#!/usr/bin/env bash
# This script takes a URL as an argument, sends a GET request to that URL, and displays the body of the response if the status code is 200.

url=$1
curl -sL -w "%{http_code}" "$url" -o /dev/null | grep -q "200" && curl -s "$url"
