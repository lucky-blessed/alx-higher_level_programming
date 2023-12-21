#!/usr/bin/python3
"""
Define a sqaure class
"""


class Square:
    """The sqaure classs
    """

    def __init__(self, size=0):
        """new square initialization

        Args:
            size (int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """
        Get/set the current sqaure size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter to set thw square size."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Returns the area of thw square"""
        return self.__self ** 2

    def my_print(self):
        """Print the square with the character # to stdout."""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
