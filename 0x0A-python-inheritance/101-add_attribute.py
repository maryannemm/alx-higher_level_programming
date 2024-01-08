#!/usr/bin/python3

def add_attribute(obj, name, value):
    """
    Adds a new attribute to an object if it's possible.
    Raises a TypeError exception if the object can't have a new attribute.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)

# Example usage
if __name__ == "__main__":
    class MyClass():
        pass

    mc = MyClass()
    add_attribute(mc, "name", "John")
    print(mc.name)

    try:
        a = "My String"
        add_attribute(a, "name", "Bob")
        print(a.name)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

