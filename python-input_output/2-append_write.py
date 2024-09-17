#!/usr/bin/python3
"""
Defines the function to add to the end of
a text file in UTF8 and return the number
of characters that were added.
"""


def append_write(filename="", text=""):
    """
    Appends a string to the end of a text file.

    Args:
        filename (str): The name of the file to append to.
        text (str): The text to append to the file.

    Returns:
        int: The number of characters added to the file.
    """
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
