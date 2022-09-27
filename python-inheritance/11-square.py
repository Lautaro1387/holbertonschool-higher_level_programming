#!/usr/bin/python3
"""class Square"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class Square that inherits from Rectangle"""
    def __init__(self, size):
        """def square"""
        self.integer_validator("size", size)
        self.__size = size
        print("[Square] {}/{}".format(Rectangle.__width, Rectangle.__height))

    def area(self):
        return self.__size * self.__size
