#!/usr/bin/python3
"""
Square class definition module
"""


class Square:
    """
    The module class
    """
    def __init__(self, size=0):
        """
        Initializes a new instance of the square class
        Args:
            size (int, optional): Size of the square
        Raises:
            TypeError: If size not an integer.
            ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Getter method to retrieve the size of the square.
        Args:
            None
        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method to set the size of the square.

        Args:
           int value: The new size value

        Raises:
            TypeError: If value not an integer
            ValueError: If value less than 0.

        Returns:
            None
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Computes and return the area of the square.

        Args:
            None

        Returns:
            int: Area of square.
        """
        return self.__size ** 2
