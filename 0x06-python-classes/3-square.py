#!/bin/python3
"""
Module containing the definition of a square class.
"""


class Square:
    """
    The square class.
    """
    def __init__(self, size=0):
        """
        Method: Initiaze a new instance of the square class.
        Args:
            size (int, optional): The size of the square with 0 default value.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.

        Returns:
            None
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Method: Computes and return the area of a square.
        Args:
            None
        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
