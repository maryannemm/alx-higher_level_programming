#!/usr/bin/python3

class BaseGeometry:
    """
    BaseGeometry class with a placeholder for the area method.
    """

    def area(self):
        """
        Raises an Exception with the message 'area() is not implemented'.
        """
        raise Exception("area() is not implemented")

# Example usage
if __name__ == "__main__":
    bg = BaseGeometry()

    try:
        print(bg.area())
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

