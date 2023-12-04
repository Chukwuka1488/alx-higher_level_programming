#!/bin/bash
# This script takes a URL as an argument, sends a GET request to that URL with a header variable, and displays the body of the response.

curl -s "$1" -X GET -H "X-School-User-Id: 98"