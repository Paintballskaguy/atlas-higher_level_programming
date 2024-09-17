#!/usr/bin/python3
"""
This module defines the class MyList which inherits from the built-in list class.

MyList contains a public instance method `print_sorted` that prints the list in ascending order.
"""


class MyList(list):
    """Inherits from the built-in list class and provides a method to print a sorted version of the list."""

    def print_sorted(self):
        """Prints the list, sorted in ascending order (without modifying the original list)."""
        print(sorted(self))