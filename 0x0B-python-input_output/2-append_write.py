#!/usr/bin/python3

""" Defines a function that append to a file. """


def append_write(filename="", text=""):
    """
        Function that append to a file.

        Args:
            filename - The file ti apppend the text.
            text - The tezt to be appended.

        Return - The number of character appended.
    """
    with open(filename, "a", encoding="utf-8") as a_file:
        return(a_file.write(text))
