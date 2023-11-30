#!/usr/bin/python3
import dis
import importlib.util
import sys

def print_names(module):
    names = [name for name in dir(module) if not name.startswith('__')]
    for name in sorted(names):
        print(name)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./4-hidden_discovery.py <module_name>")
        sys.exit(1)

    module_name = sys.argv[1]

    try:
        spec = importlib.util.spec_from_file_location(module_name, module_name + ".pyc")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        print_names(module)
    except Exception as e:
        print(e)

