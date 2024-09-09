#!/usr/bin/python3
"""
This module defines a class Square with a private
instance attribute called size and a method to calculate the area.
"""


class Square:
    """Represents a square with a private size attribute."""

    def __init__(self, size=0):
        """
        Initializes the square with a private size attribute.

        Args:
            size (int): The size of the square (default is 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueEr
