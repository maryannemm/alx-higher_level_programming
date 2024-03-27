#!/bin/bash
# This script takes a URL, sends a GET request, and displays the body of the response (if status code is 200)
curl -s -o /dev/null -w "%{http_code}" "$1" | grep -q 200 && curl -s "$1"

