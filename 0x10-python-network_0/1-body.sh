#!/bin/bash
# This script takes a URL as an argument, sends a GET request to that URL, and displays the body of the response if the status code is 200.
curl -sL -w "%{http_code}" "$1" -o /dev/null | grep -q "200" && curl -s "$1"
