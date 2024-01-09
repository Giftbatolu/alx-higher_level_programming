#!/usr/bin/python3

"""
    Defining a function
"""


def is_kind_of_class(obj, a_class):
    """
        is_kind_of_class - Function that check if the object is an
        instance of a class that inherited from, the specified class

        Args:
            obj - The object to be checked.
            a_class - The specified class.

        Return - return True if the object is an instance of the
                specified class,otherwise False.
    """
    return isinstance(obj, a_class)
