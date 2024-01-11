#!/usr/bin/python3
# models/square.py
"""Module that defines the Square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class, inherits from Rectangle class."""

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor for Square class."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for size."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size with validation."""
        self.integer_validator("width", value)
        self.greater_than_zero_validator("width", value)
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update attributes of the Square."""
        attributes = ["id", "size", "x", "y"]
        for index, value in enumerate(args):
            setattr(self, attributes[index], value)
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of the Square."""
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }

    def __str__(self):
        """String representation of Square."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.size)

    def integer_validator(self, name, value):
        """Validate that the value is an integer."""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))

    def greater_than_zero_validator(self, name, value):
        """Validate that the value is greater than zero."""
        if value <= 0:
            raise ValueError("{} must be > 0".format(name))


if __name__ == "__main__":
    # Test the Square class
    s1 = Square(5)
    print(s1.id)
    print(s1.size)
    print(s1.x)
    print(s1.y)

    s2 = Square(7, 9, 1)
    print(s2.id)
    print(s2.size)
    print(s2.x)
    print(s2.y)

