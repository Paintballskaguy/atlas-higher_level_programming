#!/usr/bin/python3
"""
Function to return the dictionary description
for JSON of an object.
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    for JSON serialization of an object.

    Args:
        obj: An instance of a class.

    Returns:
        dict: The dictionary description of the object's attributes.
    """

    return obj.__dict__
