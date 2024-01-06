#!/usr/bin/python3
"""Define a locked class."""


class LockedClass:
    """
    Prevent users from instantiating new LockedClass attributes for
    for anything but attributes called 'first_name'.
    """

    __slots__ = ["first_name"]
