#!/usr/bin/python3
"""
Function to write obj to a text file
using JSON.
"""


import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using
    its JSON representation.

    Args:
        my_obj: The object to serialize and write to the file.
        filename (str): The name of the file where the
        object will be written.

    Returns:
        None
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
