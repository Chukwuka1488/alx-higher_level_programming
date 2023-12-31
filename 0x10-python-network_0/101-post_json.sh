#!/bin/bash
# This script takes a URL and a filename as arguments, sends a JSON POST request to the URL with the contents of the file in the body of the request, and displays the body of the response.
curl -s "$1" -d "@$2" -X POST -H "Content-Type: application/json"