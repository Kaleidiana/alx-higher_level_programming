#!/usr/bin/python
"""Module of Rectangle size"""


class rectangle:
    """
    Representation of a Rectangle
    """
    def __init__widt((self, width=0, height=0):
            """initializatiion"""
            self.width = width
            self.height = height

    @property
    def width(self):
        """ width of the Rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Raises:
           TypeError: if the width is not an integer
           ValueError: if the width is less than 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ height of the Rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Raises:
           TypeError: if the height is not an integer
           ValueError: if the height is less than 0
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

