#!/usr/bin/python3
"""
Module for task 5
"""


import json


def from_json_string(my_str):
    """
    Function that writes an Object to a file using
    JSON representation

    Args:
        my_str (str): The JSON string to be converted to a Python object.

    Returns:
        object: The Python object represented by the JSON string.

    """
    return json.loads(my_str)
