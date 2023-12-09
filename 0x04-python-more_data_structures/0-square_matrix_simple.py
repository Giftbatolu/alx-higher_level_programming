#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []

    for row in matrix:
        row_matrix = []
        for column in row:
            row_matrix.append(column ** 2)
        new_matrix.append(row_matrix)

    return (new_matrix)
