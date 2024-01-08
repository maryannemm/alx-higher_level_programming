#!/usr/bin/python3

class MyInt(int):
    """
    MyInt class that inherits from int with inverted == and != operators.
    """

    def __eq__(self, other):
        """
        Overrides the == operator.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Overrides the != operator.
        """
        return super().__eq__(other)

# Example usage
if __name__ == "__main__":
    my_i = MyInt(3)
    print(my_i)
    print(my_i == 3)
    print(my_i != 3)

