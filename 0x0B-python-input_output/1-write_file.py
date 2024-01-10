#!/usr/bin/python3
"""
Module for Task 1.
"""


def write_file(filename="", text=""):
    """
    Function that writes a string to a text file (UTF8) and
    returns the number of characters written.

    Args:
        filename: The filename to be written.
        text: The text to be written to the file.

    Returns:
        int: Number of characters written.
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        return file.write(txt)
