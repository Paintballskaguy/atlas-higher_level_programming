#!/usr/bin/python3
"""
This returns the JSON representation of
an object 
"""


def to_json_string(my_obj):
    """
    Returns the JSON of an object (str)

    Args:
        my_obj: the object to convert to JSON
        
    Returns:
        str: the JSON stuff of the object.
    """
import json
return json.dumps(my_obj)
