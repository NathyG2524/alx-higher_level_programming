#!/usr/bin/python3
"""
Rectangle
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle that inherit from BaseGeometry
    """
    def __init__(self, width, height):
        """
        Instantiation of Rectangle inherited from BaseGeometry
        :param width: Private instance attribute
        :param height: Private instance attribute
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = width
