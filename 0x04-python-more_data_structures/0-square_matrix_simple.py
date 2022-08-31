#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_m = matrix.copy()

    for i in range(len(matrix)):
        new_m[i] = list(map(lambda x: x**2, matrix[i]))

    return new_m
