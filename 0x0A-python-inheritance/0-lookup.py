#!/usr/bin/python3

"""
    Defining a function that returns the list of available attributes
    and methods of an object.
"""


def lookup(obj):
    """
        lookup - Function that returnsthe list of available attribute
        and methods of an object.

        Args:
            obj - The objects to lookup.

        return:
            The list of object.
    """
    return dir(obj)
