#!/usr/bin/python3
"""Function that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """def name: matrix_divided"""
    if type(matrix) is not int and type(matrix) is not float:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if type(matrix) is float:
        matrix = int(matrix)
    if type(div) is float:
        div = int(div)
    if type(div) == 0:
        raise ZeroDivisionError("division by zero")
    for i in range(matrix):
        i = matrix / div
        return new_matrix
