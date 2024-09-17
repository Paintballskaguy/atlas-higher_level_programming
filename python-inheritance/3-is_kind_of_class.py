#!/usr/bin/python3
"""
This module defines the function is_kind_of_class.

The function returns True if the object is an instance of, or if the object is
an instance of a class that inherited from, the class; otherwise False.
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if obj is an instance of, or if obj is an instance of a class
    that inherited from, the specified class; otherwise False.
    """
    return isinstance(obj, a_class)
