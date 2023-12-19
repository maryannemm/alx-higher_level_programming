#!/usr/bin/python3
"""Defines a Square class."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initializes a new instance of the Square class."""
        self.size = size

    @property
    def size(self):
        """Getter method to retrieve the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method to set the size."""
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates and returns the square's area."""
        return self.__size ** 2

    def __eq__(self, other):
        """Override the equality operator."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Override the inequality operator."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Override the less-than operator."""
        return self.area() < other.area()

    def __le__(self, other):
        """Override the less-than-or-equal-to operator."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Override the greater-than operator."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Override the greater-than-or-equal-to operator."""
        return self.area() >= other.area()


if __name__ == "__main__":
    Square = __import__('102-square').Square

    s_5 = Square(5)
    s_6 = Square(6)

    if s_5 < s_6:
        print("Square 5 < Square 6")
    if s_5 <= s_6:
        print("Square 5 <= Square 6")
    if s_5 == s_6:
        print("Square 5 == Square 6")
    if s_5 != s_6:
        print("Square 5 != Square 6")
    if s_5 > s_6:
        print("Square 5 > Square 6")
    if s_5 >= s_6:
        print("Square 5 >= Square 6")

