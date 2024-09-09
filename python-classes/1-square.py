#!/usr/bin/python3
"""
This module defines a class Square with a private
instance attribute called size.
"""


class Square:
    """Represents a square with a private size attribute."""

    def __init__(self, size):
        """Initializes the square with a private size attribute."""
        self.__size = size
