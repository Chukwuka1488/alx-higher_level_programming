#!/usr/bin/env bash
# This script takes a URL as an argument, sends a request to that URL, and displays all HTTP methods the server will accept.

url=$1
curl -sI "$url" | grep Allow | cut -d' ' -f2-