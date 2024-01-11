#!/usr/bin/python3
# models/rectangle.py
"""Module that defines the Rectangle class."""
from models.base import Base


class Rectangle(Base):
    """Rectangle class, inherits from Base class."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor for Rectangle class."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width with validation."""
        self.integer_validator("width", value)
        self.greater_than_zero_validator("width", value)
        self.__width = value

    @property
    def height(self):
        """Getter for height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height with validation."""
        self.integer_validator("height", value)
        self.greater_than_zero_validator("height", value)
        self.__height = value

    @property
    def x(self):
        """Getter for x."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x with validation."""
        self.integer_validator("x", value)
        self.greater_than_or_equal_to_zero_validator("x", value)
        self.__x = value

    @property
    def y(self):
        """Getter for y."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y with validation."""
        self.integer_validator("y", value)
        self.greater_than_or_equal_to_zero_validator("y", value)
        self.__y = value

    def area(self):
        """Return the area of the Rectangle."""
        return self.width * self.height

    def display(self):
        """Display the Rectangle using the # character."""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """String representation of Rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Update attributes of the Rectangle."""
        attributes = ["id", "width", "height", "x", "y"]
        for index, value in enumerate(args):
            setattr(self, attributes[index], value)
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of the Rectangle."""
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }

    def integer_validator(self, name, value):
        """Validate that the value is an integer."""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))

    def greater_than_zero_validator(self, name, value):
        """Validate that the value is greater than zero."""
        if value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def greater_than_or_equal_to_zero_validator(self, name, value):
        """Validate that the value is greater than or equal to zero."""
        if value < 0:
            raise ValueError("{} must be >= 0".format(name))


if __name__ == "__main__":
    # Test the Rectangle class
    r1 = Rectangle(10, 7, 2, 8)
    print(r1.id)
    print(r1.width)
    print(r1.height)
    print(r1.x)
    print(r1.y)

    r2 = Rectangle(2, 4)
    print(r2.id)
    print(r2.width)
    print(r2.height)
    print(r2.x)
    print(r2.y)

