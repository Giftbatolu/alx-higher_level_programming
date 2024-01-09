#!/usr/bin/python3

"""
    Definibg a class that inherit from list
"""


class MyList(list):
    """
        Mylist - A class that inherit from list.

        Args:
            list - The Base class.
    """
    def print_sorted(self):
        """
            print_sorted - Function that print the list in ascending sort

        """
        print(sorted(self))
