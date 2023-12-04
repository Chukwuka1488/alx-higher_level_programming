#!/bin/bash
# This script takes a URL as an argument, sends a DELETE request to that URL, and displays the body of the response.

curl -s -X DELETE "$1"
