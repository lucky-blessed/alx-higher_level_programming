#!/usr/bin/python3
"""Module for Task 3."""

def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance of, or is an instance of a class thats inherited from the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.


    Returns:
        True if obj is an instance of a_class or its subclasses, otherwise False
    """
    return isinstance(obj, a_class)
