#!/usr/bin/python3
""""Define Square"""


class Square:
    """Represents a rectangle whose sides are equal

    Attributes:
        __size (int): length of side of the square
    """
    def __init__(self, size=0):
        """Square is initialized
        Args:
            size (int): length of side of the squar
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if type(size) is int:
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
