#!/usr/bin/python3
"""
This is the base class. it will manage 'id' attributes for all other classes.
"""


import json

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