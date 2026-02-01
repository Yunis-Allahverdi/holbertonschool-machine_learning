#!/usr/bin/env python3

'''
Finding determinant of matrix
'''


def determinant(matrix):
    try:
        rows = len(matrix[0])
        cols = len(matrix)
        if rows == 0:
            return 1
        if rows == cols:
            if rows == 1:
                return matrix[0][0]
            if rows == 2:
                return (matrix[0][0] * matrix[1][1]) -
            (matrix[1][0] * matrix[0][1])
            if rows == 3:
                return matrix[0][0] * (
                    (matrix[1][1] * matrix[2][2]) -
                    (matrix[2][1] * matrix[1][2])
                ) - matrix[0][1] * (
                    (matrix[1][0] * matrix[2][2]) -
                    (matrix[2][0] * matrix[1][2])
                ) + matrix[0][2] * (
                    (matrix[1][0] * matrix[2][1]) -
                    (matrix[2][0] * matrix[1][1]))
        else:
            raise ValueError('matrix must be a square matrix')
    except:
        raise IndexError('matrix must be a list of lists')
