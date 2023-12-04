#!/bin/bash
# This script takes a URL as an argument, sends a GET request to that URL, and displays the body of the response if the status code is 200.

curl -sL "$1" -X GET -D ./header -o ./output; if grep -q "200 OK" ./header; then cat ./output; fi