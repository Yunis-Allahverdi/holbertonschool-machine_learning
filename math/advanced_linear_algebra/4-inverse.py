#!/usr/bin/env python3
"""Inverse of a matrix."""


def determinant(matrix):
    """Calculates the determinant of a square matrix."""
    if (not isinstance(matrix, list) or
            any(not isinstance(row, list) for row in matrix)):
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
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0
    for j in range(n):
        sub = [row[:j] + row[j + 1:] for row in matrix[1:]]
        det += ((-1) ** j) * matrix[0][j] * determinant(sub)
    return det


def minor(matrix):
    """Calculates the minor matrix of a non-empty square matrix."""
    if (not isinstance(matrix, list) or
            any(not isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a list of lists")

    if matrix == [] or matrix == [[]]:
        raise ValueError("matrix must be a non-empty square matrix")

    n = len(matrix)
    if any(len(row) != n for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")

    if n == 1:
        return [[1]]

    minors = []
    for i in range(n):
        row = []
        for j in range(n):
            sub = [r[:j] + r[j + 1:] for k, r in enumerate(matrix) if k != i]
            row.append(determinant(sub))
        minors.append(row)
    return minors


def cofactor(matrix):
    """Calculates the cofactor matrix of a non-empty square matrix."""
    minors = minor(matrix)
    n = len(minors)

    cof = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(((-1) ** (i + j)) * minors[i][j])
        cof.append(row)
    return cof


def adjugate(matrix):
    """Calculates the adjugate matrix of a non-empty square matrix."""
    cof = cofactor(matrix)
    n = len(cof)
    return [[cof[j][i] for j in range(n)] for i in range(n)]


def inverse(matrix):
    """Calculates the inverse of a non-empty square matrix."""
    if (not isinstance(matrix, list) or
            any(not isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a list of lists")

    if matrix == [] or matrix == [[]]:
        raise ValueError("matrix must be a non-empty square matrix")

    n = len(matrix)
    if any(len(row) != n for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")

    det = determinant(matrix)
    if det == 0:
        return None

    adj = adjugate(matrix)
    return [[adj[i][j] / det for j in range(n)] for i in range(n)]
