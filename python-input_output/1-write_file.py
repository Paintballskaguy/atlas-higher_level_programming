#!/usr/bin/python3
"""
Defines a function that writes a string
to a UTF8 file and returns number of
characters written
"""


def write_file(filename="", text=""):
	"""
    Writes a string to a UTF8 text file and returns the
    number of characters written.

    Args:
    filename (str): The name of the file to write to.
    text (str): The text to write to the file.

    Returns:
    int: The number of characters written to the file.
    """
	with open(filename, 'w', encoding='utf-8') as file:
		return file.write(text)