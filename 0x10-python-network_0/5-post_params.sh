#!/bin/bash
# This script takes a URL as an argument, sends a POST request to that URL with variables, and displays the body of the response.
curl -s -d "email=test@gmail.com&subject=I will always be here for PLD" "${1}"