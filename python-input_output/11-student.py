#!/usr/bin/python3
"""
This module defines a class Student with public attributes,
a method to retrieve a dictionary representation of a Student instance,
and a method to reload the attributes of the Student instance from a dictionary.
"""


class Student:
    """
    A class that defines a student with first name, last name, and age.

    Attributes:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.
    """


    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of the Student instance.
        If `attrs` is a list of strings, only the attributes listed in `attrs` will be retrieved.
        Otherwise, all attributes will be retrieved.

        Args:
            attrs (list): List of attribute names to retrieve.

        Returns:
            dict: A dictionary representation of the instance.
        """
        if isinstance(attrs, list) and all(isinstance(attr, str) for attr in attrs):
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance using a dictionary.
        The keys of the dictionary correspond to attribute names and the values
        correspond to the values to set those attributes to.

        Args:
            json (dict): A dictionary with keys and values to replace the instance attributes.
        """
        for key, value in json.items():
            setattr(self, key, value)
