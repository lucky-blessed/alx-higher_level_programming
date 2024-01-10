#!/usr/bin/python3
"""
Module for Task 13.
"""


def add_attribute(obj, attribute, value):
    """
    Adds a new attribute to an object if it's possible.

    Args:
        obj: The object to which the attribute should be added.
        attribute: The name of the new attribute.
        value: The value of the new attribute.

    Raises:
        TypeError: If the object can't have a new attribute.
    """
    if hasattr(obj, '__dict__') or (hasattr(obj, '__slots__') and attribute in obj.__slots__):
        setattr(obj, attribute, value)
    else:
        raise TypeError("can't add new attribute")
