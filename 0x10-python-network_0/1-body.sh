#!/bin/bash
# This script takes a URL, sends a GET request, and displays the body of the response (if status code is 200)
curl -sL "$1"
