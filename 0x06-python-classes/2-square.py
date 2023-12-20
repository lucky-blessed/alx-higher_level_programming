#!/usr/bin/python3
"""
This module contains the definition of a square class.
"""


class Square:
    """
        This class represent a square.
    """
    def __init__(self, size=0):
        """
        Initialize a new insatance of the square class.
        Args:
            size (int, optional): The size of the square.
        Exceptions:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        Returns:
            None.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
