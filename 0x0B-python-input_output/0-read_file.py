#!/usr/bin/python
"""
Task 0 Module.
"""


def read_file(filename=""):
    """
    Prints the content of utf8 file to stdout
    """
    with open(filename, encoding='utf-8') as f:
        print(f.read())
