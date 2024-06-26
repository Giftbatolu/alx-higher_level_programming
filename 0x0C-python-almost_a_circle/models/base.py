#!/usr/bin/python3

""" Defines a base class """


class Base:
    """ A base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """
            The class constructor

            Args:
                id - The id of the instance created

            Return:
                Nothing
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
