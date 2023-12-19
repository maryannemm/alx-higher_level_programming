#!/usr/bin/python3
"""Defines a MagicClass class that mimics provided Python bytecode."""

import math


class MagicClass:
    """Represents a MagicClass with similar functionality as the given bytecode."""

    def __init__(self, radius=0):
        """Initializes a new instance of the MagicClass."""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Calculates and returns the area of the MagicClass."""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Calculates and returns the circumference of the MagicClass."""
        return 2 * math.pi * self.__radius


if __name__ == "__main__":
    # Example usage of the MagicClass
    magic_instance = MagicClass(5)
    print("Area:", magic_instance.area())
    print("Circumference:", magic_instance.circumference())

