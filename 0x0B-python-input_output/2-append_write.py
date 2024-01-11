#!/usr/bin/python3
"""
Module documentation goes here
"""


def append_write(filename="", text=""):
    """
    Function documentation goes here

    Args:
        filename (str): The name of the file to which text will be appended.
        text (str): The text to be appended to the file.

    Returns:
        int: The number of characters added.

    """
    with open(filename, mode='a', encoding='utf-8') as file:
        return file.write(text)
