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

class Square(Rectangle):
    """
    Square class that inherits from Rectangle.
    """

    def __init__(self, size):
        """
        Initializes a Square instance with a size.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """
        Returns a string representation of the Square.
        """
        return "[Square] {}/{}".format(self._Rectangle__width, self._Rectangle__height)

# Example usage
if __name__ == "__main__":
    s = Square(13)

    print(s)
    print(s.area())

