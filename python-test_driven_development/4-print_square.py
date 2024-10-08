#!/usr/bin/python3
"""
This module provides a function `print_square(size)` that prints a square using the character '#'.
"""

def print_square(size):
    """
    Prints a square with the character '#'.
    
    Args:
        size (int): The size of the square to be printed.
    
    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
    
    Example:
        >>> print_square(3)
        ###
        ###
        ###
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    
    if size < 0:
        raise ValueError("size must be >= 0")
    
    for _ in range(size):
        print("#" * size)
