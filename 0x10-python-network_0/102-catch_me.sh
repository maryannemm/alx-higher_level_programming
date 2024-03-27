#!/bin/bash
# This script sends a request to 0.0.0.0:5000/catch_me and displays the response body

curl -sLX PUT -d "user_id=98" -H "Origin: HolbertonSchool" "$1"

