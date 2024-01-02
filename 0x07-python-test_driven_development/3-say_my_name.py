#!/usr/bin/env python3

def say_my_name(first_name, last_name=""):
    """
    Prints the name in the format: My name is <first_name> <last_name>.

    Args:
    first_name (str): The first name.
    last_name (str, optional): The last name. Defaults to an empty string.

    Raises:
    TypeError: If first_name or last_name is not a string.

    Example:
    >>> say_my_name("John", "Smith")
    My name is John Smith
    >>> say_my_name("Walter", "White")
    My name is Walter White
    >>> say_my_name("Bob")
    My name is Bob
    """
    if not isinstance(first_name, str) or not isinstance(last_name, str):
        raise TypeError("first_name must be a string or last_name must be a string")

    full_name = first_name + " " + last_name if last_name else first_name
    print("My name is {}".format(full_name))

# Sample usage
say_my_name("John", "Smith")
say_my_name("Walter", "White")
say_my_name("Bob")

# Exception cases
try:
    say_my_name(12, "White")
except Exception as e:
    print(e)

