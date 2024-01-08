#!/usr/bin/python3

class BaseGeometry:
    """
    BaseGeometry class with area and integer_validator methods.
    """

    def area(self):
        """
        Raises an Exception with the message 'area() is not implemented'.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value, raising exceptions for invalid cases.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """
    Rectangle class that inherits from BaseGeometry.
    """

    def __init__(self, width, height):
        """
        Initializes a Rectangle instance with width and height.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Computes and returns the area of the Rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a string representation of the Rectangle.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

# Example usage
if __name__ == "__main__":
    r = Rectangle(3, 5)

    print(r)
    print(r.area())

