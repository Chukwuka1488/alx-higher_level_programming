#!/usr/bin/python3
"""
This module contains a class Student that defines a student.
"""

class Student:
    """
    A class that defines a student.
    
    Attributes:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.
    """

    def __init__(self, first_name, last_name, age):
        """
        The constructor for Student class.

        Parameters:
           first_name (str): The first name of the student.
           last_name (str): The last name of the student.
           age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Parameters:
            attrs (list): A list of strings representing attribute names.

        Returns:
            dict: A dictionary representation of a Student instance.
        """
        if attrs is None:
            return self.__dict__
        
        return {
             attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)
                }

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance.

        Parameters:
            json (dict): A dictionary with attribute names as keys and new
            attribute values as values.
        
        Returns:
            None
        """
        for key, value in json.items():
            setattr(self, key, value)
