#!/usr/bin/python3

""" Defines a class that inherit from base class. """

from .base import Base


class Rectangle(Base):
    """ A class that inherit from Base class

        Args:
            Base - the parent class.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
            The class instructor

            Args:
                width (int) - The width of the rectangle.
                height (int) - The height of the rectangle.
                x (int) - The horizontal axis
                y (int) - The vertical axis
                id (int)- The id of each instance

            Return:
                Nothing
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """ Function that retrieve and  return the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """
            Function that set the value of width.

            Args:
                value (int) - The value to assign.

            Return:
                Nothing
        """
        self.check_validation("width", value)
        self.__width = value

    @property
    def height(self):
        """ Function that retrieve and  return the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """
            Function that set the value of height.

            Args:
                value (int) - The value to assign.

            Return:
                Nothing.
        """
        self.check_validation("height", value)
        self.__height = value

    @property
    def x(self):
        """ Function that retrieve and  return the x-axis of the rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """
            Function that set the value of x-axis.

            Args:
                value (int) - The value to assign.

            Return:
                Nothing
        """
        self.check_validation("x", value)
        self.__x = value

    @property
    def y(self):
        """ Function that retrieve and  return the y-axis of the rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """
            Function that set the value of y-axis.

            Args:
                value (int) - The value to assign.

            Return:
                Nothing
        """
        self.check_validation("y", value)
        self.__y = value

    @staticmethod
    def check_validation(setter_name, value):
        """
            Function that validate the setter method.

            Args:
                setter_name(str) - name of setter method to validate
                value (int) - The value of the setter method.

            Return:
                raise TypeError if the value is not an integer.
                raise ValueError if the width or height is under or equal zero
                raise ValueError if the x or y is under zero.
        """
        if type(value) is not int:
            raise TypeError(f"{setter_name:s} must be an integer")

        if setter_name == "width" or setter_name == "height":
            if value <= 0:
                raise ValueError(f"{setter_name:s} must be > 0")

        elif value < 0:
            raise ValueError("{setter_name:s} must be >= 0")
