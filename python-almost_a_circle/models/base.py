#!/usr/bin/python3
"""
This is the base class. it will manage 'id' attributes for all other classes.
"""


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
