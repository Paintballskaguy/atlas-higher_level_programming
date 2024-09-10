#!/usr/bin/python3
"""
This module defines a function `say_my_name` that prints a person's full name.
"""


def say_my_name(first_name, last_name=""):
    """
    Prints 'My name is <first_name> <last_name>'.

    Args:
        first_name (str): The first name to print. Required.
        last_name (str): The last name to print. Optional, defaults to an empty string.

    Raises:
        TypeError: If either first_name or last_name is not a string.

    Example:
        >>> say_my_name("John", "Smith")
        My name is John Smith

        >>> say_my_name("Alice")
        My name is Alice 
    """
    
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    
    print(f"My name is {first_name} {last_name}")