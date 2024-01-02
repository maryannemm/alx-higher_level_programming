#!/usr/bin/env python3

def print_square(size):
    """
    Prints a square with the character #.

    Args:
    size (int): The size length of the square.

    Raises:
    TypeError: If size is not an integer.
    ValueError: If size is less than 0.
    TypeError: If size is a float and less than 0.

    Example:
    >>> print_square(4)
    ####
    ####
    ####
    ####
    >>> print_square(10)
    ##########
    ##########
    ##########
    ##########
    ##########
    ##########
    ##########
    ##########
    ##########
    ##########
    >>> print_square(0)
    <BLANK LINE>
    >>> print_square(1)
    #
    >>> print_square(-1)
    Traceback (most recent call last):
        ...
    ValueError: size must be >= 0
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if isinstance(size, float) and size.is_integer() and size < 0:
        raise TypeError("size must be an integer")

    for _ in range(size):
        print("#" * size)

# Sample usage
print_square(4)
print("")
print_square(10)
print("")
print_square(0)
print("")
print_square(1)
print("")

# Exception cases
try:
    print_square(-1)
except Exception as e:
    print(e)

