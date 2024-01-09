#!/usr/bin/python3

"""
    Defining a function
"""


def is_same_class(obj, a_class):
    """
        is_same_class - Function that return true if an object is
        exactly an instance of a specified class.

        Args:
            obj - object to check.
            a_class - The specified class.

        Return - return True if an object is an instance.
                otherwise False.
    """
    if type(obj) == a_class:
        return True
    return False
