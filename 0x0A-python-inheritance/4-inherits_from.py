#!/usr/bin/python3

"""
    Defining a function called inherit_from.

"""


def inherits_from(obj, a_class):
    """
        inherits_from - Function that check the object is an instance
        of a class that inherited from the specified class

        Args:
            obj - The object to be checked.
            a_class - The specified class.

        Return - return True if the object inherited from the
            specified class otherwise False.
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
