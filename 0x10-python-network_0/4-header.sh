#!/bin/bash
# This script sends a GET request to the specified URL with a custom header and displays the response body
curl -sH "X-School-User-Id: 98" "$1"

