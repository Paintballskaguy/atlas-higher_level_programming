#!/usr/bin/python3
"""
Defines a class Square that inherits from Rectangle (9-rectangle).
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class representing a square, inheriting from Rectangle."""

    def __init__(self, size):
        """
        Initialize a Square object with size.

        Args:
            size (int): The size of the square (both width and height).
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Returns the area of the square."""
        return self.__size * self.__size
