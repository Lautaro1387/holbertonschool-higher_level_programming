#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for number1 in matrix:
        for idx in number1:
            print("{:d}".format(idx), end="")
            if idx != number1[-1]:
                print(" ", end="")
        print("")
