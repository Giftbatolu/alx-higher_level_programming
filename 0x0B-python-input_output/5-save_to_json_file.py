#!/usr/bin/python33

import json

""" Defines a function "5-save_to_json_file" """


def save_to_json_file(my_obj, filename):
    """
        Function that write to a text file using json representation

        Args:
            my_obj - The file that cintain an object.
            filename - The file to write to.

        Return:
            json representation.
    """
    with open(filename, "w", encoding="utf-8") as a_file:
        a_file.write(json.dumps(my_obj))
