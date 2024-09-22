#!/usr/bin/python3
"""
This is the base class. it will manage 'id' attributes for all other classes.
"""


import json
import os

class Base:
    """Base class manages the 'id' for all"""
    __nb_objects = 0
    
    def __init__(self, id=None):
        """Initialize a new Base instance.
        
        Args:
            id (int): If provided, the instance's public id attribute is set to this value.
                      Otherwise, __nb_objects is incremented and assigned to id.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
            
    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries.
        
        Args:
            list_dictionaries (list): A list of dictionaries.
        
        Returns:
            str: The JSON string representation of list_dictionaries or "[]".
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file.
        
        Args:
            list_objs (list): A list of instances that inherit from Base.
        """
        filename = cls.__name__ + ".json"
        list_dicts = []

        if list_objs is not None:
            list_dicts = [obj.to_dictionary() for obj in list_objs]

        json_string = cls.to_json_string(list_dicts)

        with open(filename, "w") as f:
            f.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list represented by the JSON string.
        
        Args:
            json_string (str): A string representing a list of dictionaries.
        
        Returns:
            list: The list of dictionaries represented by json_string.
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)
    
    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes set using **dictionary.
        
        Args:
            dictionary (dict): The dictionary of attributes to set.
        
        Returns:
            object: An instance of the class with the attributes set.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)  # Create a dummy Rectangle instance
        elif cls.__name__ == "Square":
            dummy = cls(1)  # Create a dummy Square instance
        
        dummy.update(**dictionary)  # Update the dummy instance with real attributes
        return dummy
    
    @classmethod
    def load_from_file(cls):
        """Returns a list of instances from <Class name>.json file.
        
        Returns:
            list: A list of instances of cls type.
        """
        filename = cls.__name__ + ".json"

        if not os.path.exists(filename):
            return []

        with open(filename, "r") as f:
            json_string = f.read()

        list_dicts = cls.from_json_string(json_string)
        return [cls.create(**dictionary) for dictionary in list_dicts]