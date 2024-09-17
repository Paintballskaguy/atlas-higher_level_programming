#!/usr/bin/python3
"""
Function to return an obj with python data
that was in JSON strings.
"""


import json


def from_json_string(my_str):
    """
    Returns an object (Python data structure) represented by a JSON string.

    Args:
        my_str (str): The JSON string to convert.

    Returns:
        object: The Python object represented by the JSON string.
    """
    return json.loads*my_str)
    