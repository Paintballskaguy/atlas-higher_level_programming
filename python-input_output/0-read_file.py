#!/usr/bin/python3
"""
Defines a function to read UTF8 text and print out contents.
"""
 
def read_file(filename=""):
    """Reads the file and prints out contents"""
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read(), end="")
