#!/usr/bin/python3
"""
This module defines a class Rectangle with private instance attributes
for width and height. It includes methods to calculate area, perimeter,
print the rectangle using the '#' character, recreate an instance with repr,
and a class attribute to track the number of instances.
"""


class Rectangle:
    """
    Class that defines a rectangle with private attributes for width and height.
    Includes methods to compute the area, perimeter, a string representation,
    a destructor that prints a message when an instance is deleted, and
    tracks the number of instances created and deleted.
    """

    # Public class attribute to track number of instances
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        Initializes the rectangle with optional width and height (default is 0).
        Increments the number_of_instances class attribute.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Getter for the width attribute.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the width attribute.
        Ensures width is an integer and >= 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter for the height attribute.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for the height attribute.
        Ensures height is an integer and >= 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculates and returns the area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates and returns the perimeter of the rectangle.
        If width or height is 0, the perimeter is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns a string representation of the rectangle using the '#' character.
        If width or height is 0, returns an empty string.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return '\n'.join(['#' * self.__width for _ in range(self.__height)])

    def __repr__(self):
        """
        Returns a string that represents the rectangle in a format
        that allows a new instance to be created using eval().
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        Prints a message when an instance of Rectangle is deleted.
        Decrements the number_of_instances class attribute.
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")