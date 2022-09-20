#!/usr/bin/python3
"""Square"""


class Square:
    """class name: Square"""
    def __init__(self, size=0):
        """class name: __init__"""
        if size < 0:
            raise ValueError("size must be >= 0")
        if type(size) is not int:
            raise TypeError("size must be an integer")
    def size(self):
        """def name: size"""
    def size(self, value):
        """def name: size"""
    def area(self):
        """def name: area"""
        return self.__size * self.__size
