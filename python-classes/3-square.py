#!/usr/bin/python3
"""Square"""


class Square:
    """class name: Square"""
    def __init__(self, size=0):
        """def name: __init__"""
        if size < 0:
            raise ValueError(size must be >= 0)
    def area(self):
