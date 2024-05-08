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
        self.__size = size

    @property
    def size(self):
        """ Retrieve and Return the size of the square. """

        return self.__size

    @size.setter
    def size(self, value):
        """
            Set the value of size.

            Args:
                value (int) - The value to set.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """ Return area of square. """

        return (self.__size ** 2)
