#!/bin/bash
# This script sends an OPTIONS request to the specified URL and displays the supported HTTP methods
curl -sI "$1" | grep -i Allow | awk '{print $2}'

