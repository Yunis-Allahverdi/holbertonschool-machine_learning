#!/usr/bin/env python3
'''
Calc the shape of matrix
'''


def matrix_shape(matrix):
    '''
    Does same thing as above
    '''
    shape = []

    while isinstance(matrix, list):
        shape.append(len(matrix))
        if len(matrix) == 0:
            break
        matrix = matrix[0]

    return shape
