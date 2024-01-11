#!/usr/bin/python3
"""
Module documentation for Task 6.
"""

import json


def load_from_json_file(filename):
    """
    Function that creates an Object file from a JSON file.

    Args:
        filename (str): The name of the JSON file to load the object from.

    Returns:
        object: The Python object loaded from the JSON file.

    """
    with open(filename, encoding='utf-8') as file:
        return json.load(file)
