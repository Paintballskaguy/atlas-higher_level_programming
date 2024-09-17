#!/usr/bin/python3
"""
Defines the class MyList which inherits from the built-in list class.

MyList is a public instance method `print_sorted` prints in ascending order.
"""


class MyList(list):
    """Inherits from the list and prints a sorted version of the list."""

    def __init__(self):
        """Initializes the object (optional)."""
        super().__init__()

    def print_sorted(self):
        """Prints the list, in ascending order (not changing original list)."""
        print(sorted(self))
