#!/usr/bin/python3
"""
This module provides a function `text_indentation` that prints a text with 2 new lines
after each of the following characters: '.', '?', and ':'.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: '.', '?', and ':'.
    
    Args:
        text (str): The text to be printed.
    
    Raises:
        TypeError: If the text is not a string.
    
    The function will also ensure that there is no extra space at the beginning or
    at the end of each printed line.
    
    Example:
        >>> text_indentation("Hello. How are you? I'm fine: thank you.")
        Hello.
        
        How are you?
        
        I'm fine:
        
        thank you.
    """
    
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    special_chars = {'.', '?', ':'}
    result = ""
    i = 0

    while i < len(text):
        result += text[i]
        if text[i] in special_chars:
            result += "\n\n"
            i += 1

            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        i += 1
    
    print(result, end="")
