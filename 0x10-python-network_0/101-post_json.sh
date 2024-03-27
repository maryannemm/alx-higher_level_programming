#!/bin/bash
# This script sends a JSON POST request to the specified URL with data from a file and displays the response body

# Check if the filename is provided
if [ $# -ne 2 ]; then
    echo "Usage: $0 <URL> <filename>"
    exit 1
fi

# Read the JSON data from the file
json_data=$(cat "$2")

# Send the POST request and display the response body
curl -s -X POST -H "Content-Type: application/json" -d "$json_data" "$1" | grep -q "Valid JSON" && echo "Valid JSON" || echo "Not a valid JSON"

