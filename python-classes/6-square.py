#!/usr/bin/python3
"""Square"""


class Square:
    """class name: Square"""
    def __init__(self, size=0, position=(0, 0)):
        """def name: __init__"""
        if size < 0:
            raise ValueError("size must be >= 0")
        if type(size) is not int:
            raise TypeError("size must be an integer")
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """def name: size"""
        return self.__size

    @size.setter
    def size(self, value):
        """def name: size"""
        if value < 0:
            raise ValueError("size must be >= 0")
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        self.__size = value

    @property
    def position(self):
        """def name: position"""
        return self.__position

    @position.setter
    def position(self, value):
        """def name: position"""
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) is not int or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """def name: area"""
        return self.__size * size.__size

    def my_print(self):
        """def name: my_print"""
        if self.__size == 0:
            print()
            return
        for x in range(self.__position[1]):
            print()
        for i in range(self.__size):
            for p in range(self.__position[0]):
                print(end=" ")
            for j in range(self.__size):
                print("#", end="")
            print()
