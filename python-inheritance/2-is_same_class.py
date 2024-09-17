#!/usr/bin/python3
"""
This module defines the function is_same_class.

The function returns True if the object is exactly an instance of
the specified class; otherwise False.
"""


def is_same_class(obj, a_class):
    """Returns True if obj is exact instance of a_class; otherwise False."""
    return type(obj) is a_class
