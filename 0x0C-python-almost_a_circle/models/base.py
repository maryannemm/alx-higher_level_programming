#!/usr/bin/python3
# models/base.py
"""Module that defines the Base class."""
import turtle


class Base:
    """Base class for managing id attribute in all future classes."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor for Base class."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries."""
        import json
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file."""
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_dict = [obj.to_dictionary() for obj in list_objs]
                file.write(cls.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """Return the list of the JSON string representation json_string."""
        import json
        if json_string is None or not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def load_from_file(cls):
        """Return a list of instances from a JSON file."""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as file:
                content = file.read()
                list_dicts = cls.from_json_string(content)
                return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            return []

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes already set."""
        instance = cls(1, 1)
        instance.update(**dictionary)
        return instance

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serialize and save to a CSV file."""
        filename = cls.__name__ + ".csv"
        with open(filename, 'w') as file:
            if list_objs is None:
                file.write("")
            else:
                list_dict = [obj.to_dictionary() for obj in list_objs]
                for obj in list_dict:
                    if cls.__name__ == 'Rectangle':
                        file.write("{},{},{},{},{}\n".format(
                            obj['id'], obj['width'], obj['height'], obj['x'], obj['y']))
                    elif cls.__name__ == 'Square':
                        file.write("{},{},{},{}\n".format(
                            obj['id'], obj['size'], obj['x'], obj['y']))

    @classmethod
    def load_from_file_csv(cls):
        """Deserialize and load from a CSV file."""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, 'r') as file:
                content = file.read()
                if cls.__name__ == 'Rectangle':
                    attributes = ['id', 'width', 'height', 'x', 'y']
                    items = content.strip().split('\n')
                    return [cls.create(**dict(zip(attributes, map(int, item.split(',')))))
                            for item in items]
                elif cls.__name__ == 'Square':
                    attributes = ['id', 'size', 'x', 'y']
                    items = content.strip().split('\n')
                    return [cls.create(**dict(zip(attributes, map(int, item.split(',')))))
                            for item in items]
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Open a window and draw all the Rectangles and Squares using Turtle graphics."""
        turtle.Screen().clear()
        turtle.bgcolor("white")
        turtle.speed(0)
        turtle.hideturtle()

        for rect in list_rectangles:
            turtle.penup()
            turtle.goto(rect.x, rect.y)
            turtle.pendown()
            turtle.color("black")
            for _ in range(2):
                turtle.forward(rect.width)
                turtle.left(90)
                turtle.forward(rect.height)
                turtle.left(90)

        for square in list_squares:
            turtle.penup()
            turtle.goto(square.x, square.y)
            turtle.pendown()
            turtle.color("red")
            for _ in range(4):
                turtle.forward(square.size)
                turtle.left(90)

        turtle.exitonclick()


if __name__ == "__main__":
    # Test the Base class
    b1 = Base()
    print(b1.id)

    b2 = Base()
    print(b2.id)

    b3 = Base()
    print(b3.id)

    b4 = Base(12)
    print(b4.id)

    b5 = Base()
    print(b5.id)

