#!/usr/bin/python3
"""
Module for Task 12.
"""


class MyInt(int):
    """
    A class representing an integer with inverted == and != operators.
    """

    def __eq__(self, other):
        """
        Inverts the == operator.

        Args:
            other: The object to compare against.

        Returns:
            True if self is not equal to other, otherwise False.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Inverts the != operator.

        Args:
            other: The object to compare against.

        Returns:
            True if self is equal to other, otherwise False.
        """
        return super().__eq__(other)
