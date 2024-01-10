#!/usr/bin/python3
import sys
from os import path
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

filename = "add_item.json"

# Load existing data from the file or create an empty list
try:
    data = load_from_json_file(filename)
except FileNotFoundError:
    data = []

# Add command-line arguments to the list
data.extend(sys.argv[1:])

# Save the updated list to the file
save_to_json_file(data, filename)

