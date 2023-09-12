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

    def to_json(self):
        """
        Retrieves a dictionary representation of a Student instance.

        Returns:
            dict: A dictionary representation of a Student instance.
        """
        return self.__dict__
