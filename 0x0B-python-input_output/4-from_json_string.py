#!/usr/bin/python3

""" Defines a function that return an object represented by json. """

import json


def from_json_string(my_str):
    """
        Function that return object represented by json string.

        Args:
            my_str : The object to return.

        Return:
            An object represemted by json string.
    """
    return (json.loads(my_str))
