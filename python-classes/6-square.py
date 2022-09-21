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
        if value is not int:
            raise TypeError("size must be an integer")
        self.__size = value

    @property
    def position(self):
        """def name: position"""
        return self.__position

    @position.setter
    def position(self, value):
        """def name: position"""
        if value < 0:
            raise ValueError("size must be >= 0")
        if value is not int:
            raise TypeError("size must be an integer")
        self.__position = value

    def area(self):
        """def name: area"""
        return self.__size * size.__size

    def my_print(self):
        """def name: my_print"""
        for x in range(self.__position[1]):
            print()
        for i in range(self.__size):
            for x in range(self.__position[0]):
                print(" ", end="")
            for j in range(self.__size):
                print("#", end="")
            print()
