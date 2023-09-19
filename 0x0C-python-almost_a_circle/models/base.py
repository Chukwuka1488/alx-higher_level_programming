#!/usr/bin/python3
"""
This module defines the Base class.
The Base class is intended to serve as the parent class for other classes in
the project.
It manages the id attribute for all derived classes, ensuring uniqueness and
avoiding redundancy.
"""
import json
import os
import csv
import turtle


class Base:
    """Base class to manage the id attribute in all future classes."""

    # Private class attribute
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a new Base instance.

        Parameters:
            id (int): An identifier for the instance. If None, an automatic id
            is assigned.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file."""
        # Convert list_objs into list of dictionaries
        list_dicts = [obj.to_dictionary() for obj in list_objs] if list_objs else []

        # Use the static method to_json_string to convert the list of
        # dictionaries into a JSON string
        json_str = cls.to_json_string(list_dicts)

        # Write the JSON string to a file
        with open(cls.__name__ + ".json", "w") as file:
            file.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string."""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Creates an instance with all attributes already set."""
        # For Rectangle class
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        # For Square class
        elif cls.__name__ == "Square":
            dummy = cls(1)
        # Use the update method to set the attributes from the dictionary
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances."""
        filename = "{}.json".format(cls.__name__)

        # If file doesn't exist, return an empty list
        if not os.path.exists(filename):
            return []

        # Otherwise, read the file
        with open(filename, "r") as f:
            json_str = f.read()

        # Convert the JSON string to a list of dictionaries
        list_dicts = cls.from_json_string(json_str)

        # Create instances from each dictionary and add to a list
        instances = [cls.create(**d) for d in list_dicts]

        return instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes instances to CSV file."""
        filename = "{}.csv".format(cls.__name__)

        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            if cls.__name__ == "Rectangle":
                for obj in list_objs:
                    writer.writerow([obj.id, obj.width, obj.height, obj.x, obj.y])
            elif cls.__name__ == "Square":
                for obj in list_objs:
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes instances from CSV file."""
        filename = "{}.csv".format(cls.__name__)

        if not os.path.exists(filename):
            return []

        with open(filename, 'r') as csvfile:
            reader = csv.reader(csvfile)
            instances = []
            if cls.__name__ == "Rectangle":
                for row in reader:
                    id, width, height, x, y = map(int, row)
                    instances.append(cls(width, height, x, y, id))
            elif cls.__name__ == "Square":
                for row in reader:
                    id, size, x, y = map(int, row)
                    instances.append(cls(size, x, y, id))

        return instances

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draws all the rectangles and squares using turtle module."""

        # Initialize the turtle screen
        win = turtle.Screen()
        win.title("Draw Rectangles and Squares")
        t = turtle.Turtle()
        t.speed(3)  # Moderate speed

        # Function to draw a rectangle
        def draw_rectangle(rect):
            t.penup()
            t.goto(rect.x, rect.y)
            t.pendown()
            t.forward(rect.width)
            t.left(90)
            t.forward(rect.height)
            t.left(90)
            t.forward(rect.width)
            t.left(90)
            t.forward(rect.height)
            t.left(90)

        # Function to draw a square
        def draw_square(sqr):
            t.penup()
            t.goto(sqr.x, sqr.y)
            t.pendown()
            for _ in range(4):
                t.forward(sqr.size)
                t.left(90)

        # Draw all the rectangles
        for rect in list_rectangles:
            draw_rectangle(rect)

        # Draw all the squares
        for sqr in list_squares:
            draw_square(sqr)

        # Wait for a click to close the turtle window
        win.exitonclick()
