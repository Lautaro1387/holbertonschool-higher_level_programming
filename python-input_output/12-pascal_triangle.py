#!/usr/bin/python3
"""Technical interview reparation"""

def pascal_triangle(n):
    """
    returns a list of lists of integers representing the Pascal’s triangle
    """
    lis = []
    auxP = []
    aux = [1]
    if n <= 0:
        return lis
    for i in range(0, n):
        if i == 0:
            lis.append(aux)
            continue
        aux = []
        for j in range(0, i + 1):
            if j == 0 or j == i:
                aux.append(1)
                continue
            aux.append(int(auxP[j]) + int(auxP[1 - j]))
        lis.append(aux)
        auxP = aux
    return lis
