#!/usr/bin/python3
"""
Module documentation for Task 9.
"""


class Student:
    """
    Class defines a student by:
    first name, last name, age
    """

    def __init__(self, first_name, last_name, age):
        """
        Method documentation goes here

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.

        Returns:
            None

        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Method documentation goes here

        Returns:
            dict: A dictionary representation of a Student instance.

        """
        return self.__dict__
