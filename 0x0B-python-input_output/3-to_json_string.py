#!/usr/bin/python3


""" Defines a function that return json string. """

import json


def to_json_string(my_obj):
    """
        Function that return json representation of an object.

        Args:
            my_obj - The file that json string.

        Return:
            The json representation of an object.
    """

    return (json.dumps(my_obj))
