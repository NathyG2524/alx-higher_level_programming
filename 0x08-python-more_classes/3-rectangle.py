#!/usr/bin/python3
"""
rectangle module
a rectangle class module
"""


class Rectangle:
    """
    class: Rectangle
    this is a class rectangle
    """

    def __init__(self, width=0, height=0):
        """
        method: __init__
        :param width:
        :param height:
        """
        self.height = height
        self.width = width

    @property
    def height(self):
        """
        method: get height
        :return: Private height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        method: set height
        :param value: get value to be set on the height
        :return: Private height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        """
        method: get width
        :return: Private width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        method: set width
        :param value: value to be set on width
        :return: Private width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    def area(self):
        """
        method: calculate the area of the rectangle
        :return: area
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        method: calculate the perimeter of a rectangle
        :return: perimeter
        """
        per = 2 * (self.__width + self.__height)
        if self.__width == 0 or self.__height == 0:
            per = 0
        return per

    def __str__(self):
        """
        method: __str__
        :return: readable string to the user
        """
        string = ""
        if self.__width != 0 and self.__height != 0:
            for i in range(self.__height):
                for j in range(self.__width):
                    string += "#"
                string += "\n"
        return string
