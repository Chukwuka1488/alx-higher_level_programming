#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()
    n = len(new_matrix)
    return [[i*i for i in matrix[row]] for row in range(n)]
