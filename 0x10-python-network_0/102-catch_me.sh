#!/bin/bash
# This script sends a request to 0.0.0.0:5000/catch_me and displays the response body
curl -sX PUT -L -d "user_id=98" --header "origin: HolbertonSchool" 0.0.0.0:5000/catch_me
