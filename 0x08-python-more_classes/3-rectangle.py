#!/usr/bin/python3

""" A class that defines a rectangle """


class Rectangle:
    """ A rectangle class """
    def __init__(self, width=0, height=0):
        """
            constructor of class attribute.

            Args:
                width (int): The width of the rectangle.
                height (int): The height of the rectangle.
        """
        self.height = height
        self.width = width

    @property
    def width(self):

        """ retrives the value of the width """

        return self.__width

    @width.setter
    def width(self, value):

        """
            To set the value of width.

            Args:
                value: The assign value to width.
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):

        """ retrives the value of the height """

        return self.__height

    @height.setter
    def height(self, value):

        """
            To set the value of the height.

            Args:
                value: The assign value to height.
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):

        """ return the area of rectangle """

        return (self.__height * self.__width)

    def perimeter(self):

        """ return the perimeter of the rectangle """

        if self.__height == 0 or self.__width == 0:
            return (0)

        return ((self.__height * 2) + (self.__width * 2))

    def __str__(self):

        """
            return the printable format of the rectangle with #
            character.
        """

        if self.__height == 0 or self.__width == 0:
            return ("")

        rectangle = []
        for b in range(self.__height):
            for d in range(self.__width):
                rectangle.append("#")

            if b != self.__height - 1:
                rectangle.append("\n")
        return ("".join(rectangle))
