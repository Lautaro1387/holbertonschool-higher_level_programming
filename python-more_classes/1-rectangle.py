#!/usr/bin/python3
"""Rectangle"""


class Rectangle:
    """class Rectangle"""

    def __init__(self, widht=0, height=0):
        """def __init__"""
        self.__height = height
        self.__widht = widht

    @property
    def width(self):
        """To retrieve it"""
        return self.__width

    @property
    def height(self):
        """To retrieve it"""
        return self.__height

    @width.setter
    def width(self, value):
        """To set it"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("widht must be >= 0")
        self.__widht = value

    @height.setter
    def height(self, value):
        """To set it"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
