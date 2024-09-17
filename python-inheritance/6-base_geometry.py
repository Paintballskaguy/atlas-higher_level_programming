#!/usr/bin/python3
"""
This defines a class BaseGeometry with a public instance method area.
"""


class BaseGeometry:
    """A class with a public method area that raises an exception."""

    def area(self):
        """
        Raises an exception indicating that the area method is not implemented.
        """
        raise Exception("area() is not implemented")
