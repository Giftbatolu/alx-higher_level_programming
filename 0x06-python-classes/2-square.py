#!/usr/bin/python3

""" Defines a class Square """


class Square:
    """ A Square class """

    def __init__(self, size=0):
        """
            class construtor

            Args:
                size (int) - The size of the square.

        """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
