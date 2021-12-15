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

    number_of_instances = 0
    print_symbol = "#"

    @classmethod
    def square(cls, size=0):
        """
        method: square
        :param size: length of the sides
        :return: side length
        """
        if not isinstance(size, int):
            raise TypeError("width must be an integer")
        if size < 0:
            raise ValueError("width must be >= 0")
        return cls(size, size)

    def __init__(self, width=0, height=0):
        """
        method: __init__
        :param width:
        :param height:
        """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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
                    string += str(self.print_symbol)
                if i != max(range(self.__height)):
                    string += "\n"
        return string

    def __repr__(self):
        """
        method: __repr__
        :return: official string representation of an object
        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() > rect_2.area():
            return rect_1
        elif rect_1.area() < rect_2.area():
            return rect_2
        else:
            return rect_1

    def __del__(self):
        """
        method: __del__
        :return: delete instance of Rectangle
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
