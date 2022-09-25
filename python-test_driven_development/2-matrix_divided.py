#!/usr/bin/python3
"""Function that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """def name: matrix_divided"""
    num = 0
    for row in matrix:
        if num != 0 and len(row) != length:
            raise TypeError('Each row of the matrix must have the same size')
        length = len(row)
        for item in row:
            if type(item) is not int and type(item) is not float:
                raise TypeError('matrix must be a matrix (list of lists)'
                                ' of integers/floats')
    num += 1
    if type(div) is not int and type(div) is not float:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    new_matrix = []
    for row in matrix:
        new_list = []
        for item in row:
            new_list.append(round(item / div, 2))
        new_matrix.append(new_list)
    return new_matrix
