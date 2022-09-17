#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for elements in matrix:
        new_list = []
        for int1 in elements:
            a = int1 * int1
            new_list.append(a)
        new_matrix.append(new_list)
    return new_matrix
