#!/bin/bash
# This script sends a request to the specified URL and displays only the status code
curl -s -o /dev/null -w "%{http_code}" "$1"

