#!/usr/bin/env python3
'''
Finding determinant of matrix
'''


def determinant(matrix):
    '''
    This function does same thing as above
    '''
    if (
        not isinstance(matrix, list)
        or any(not isinstance(row, list) for row in matrix)
    ):
        raise TypeError("matrix must be a list of lists")

    if matrix == [[]]:
        return 1

    if matrix == []:
        raise TypeError("matrix must be a list of lists")

    n = len(matrix)
    if any(len(row) != n for row in matrix):
        raise ValueError("matrix must be a square matrix")

    if n == 1:
        return matrix[0][0]
    if n == 2:
        return (matrix[0][0] * matrix[1][1]) - (matrix[1][0] * matrix[0][1])
    if n == 3:
        return matrix[0][0] * (
            (matrix[1][1] * matrix[2][2]) -
            (matrix[2][1] * matrix[1][2])
        ) - matrix[0][1] * (
            (matrix[1][0] * matrix[2][2]) -
            (matrix[2][0] * matrix[1][2])
        ) + matrix[0][2] * (
            (matrix[1][0] * matrix[2][1]) -
            (matrix[2][0] * matrix[1][1])
        )

    det = 0
    for j in range(n):
        minor = [row[:j] + row[j+1:] for row in matrix[1:]]
        det += ((-1) ** j) * matrix[0][j] * determinant(minor)
    return det
