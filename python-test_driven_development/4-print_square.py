#!/usr/bin/python3
"""Function that prints a square with the character #"""


def print_square(size):
    """def name: print_square"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    size = '#'
    print("{}".format(size))
