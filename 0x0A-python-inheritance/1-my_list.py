#!/usr/bin/python3
"""
Module for Task 1.
"""


class MyList(list):
    """
    A class that inherits from list and provides additional functionality.
    """

    def print_sorted(self):
        """
        Prints the list in ascending order.

        Returns:
            None
        """
        print(sorted(self))
