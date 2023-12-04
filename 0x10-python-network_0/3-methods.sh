#!/bin/bash
# This script takes a URL as an argument, sends a request to that URL, and displays all HTTP methods the server will accept.

curl -sI "$1" -X OPTIONS | grep "Allow:" | cut -d':' -f2 | sed 's/ //'