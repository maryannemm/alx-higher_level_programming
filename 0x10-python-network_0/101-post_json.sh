#!/bin/bash
# This script sends a JSON POST request to the specified URL with data from a file and displays the response body
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
