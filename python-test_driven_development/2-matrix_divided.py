#!/usr/bin/python3
"""Function that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """def name: matrix_divided"""
    new_matrix = []
    aux = []
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if isinstance(div, int) or not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if matrix[0]:
        size = len(matrix[0])
    for i in matrix:
        if not isinstance(i, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(matrix[i]) != size:
            raise TypeError("Each row of the matrix must have the same size")
        for j in i:
            if not isinstance(j, float) or not isinstance(j, int):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            aux.append(float("{:.2f}".format(j/div)))
        new_matrix.append(aux)
    return new_matrix
