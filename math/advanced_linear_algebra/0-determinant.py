#!/usr/bin/env python3
'''
Finding determinant of matrix
'''


def determinant(matrix):
    # check list of lists
    if (
        not isinstance(matrix, list)
        or any(not isinstance(row, list) for row in matrix)
    ):
        raise TypeError("matrix must be a list of lists")

    # 0x0 matrix
    if matrix == [[]]:
        return 1

    # reject [] explicitly (common in Holberton tests)
    if matrix == []:
        raise TypeError("matrix must be a list of lists")

    # check square (also catches ragged matrices)
    n = len(matrix)
    if any(len(row) != n for row in matrix):
        raise ValueError("matrix must be a square matrix")

    # base cases (your logic)
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

    # NEW: recursive determinant for n >= 4
    det = 0
    for j in range(n):
        minor = [row[:j] + row[j+1:] for row in matrix[1:]]
        det += ((-1) ** j) * matrix[0][j] * determinant(minor)
    return det
