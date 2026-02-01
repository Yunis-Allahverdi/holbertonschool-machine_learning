#!/usr/bin/env python3
"""Matrix definiteness."""

import numpy as np


def definiteness(matrix):
    """Calculates the definiteness of a matrix."""
    if not isinstance(matrix, np.ndarray):
        raise TypeError("matrix must be a numpy.ndarray")

    if (
        matrix.ndim != 2
        or matrix.shape[0] != matrix.shape[1]
        or matrix.size == 0
    ):
        return None

    if not np.allclose(matrix, matrix.T):
        return None

    eigenvalues = np.linalg.eigvals(matrix)

    if not np.all(np.isreal(eigenvalues)):
        return None

    eigenvalues = eigenvalues.real

    if np.all(eigenvalues > 0):
        return "Positive definite"
    if np.all(eigenvalues >= 0) and np.any(eigenvalues == 0):
        return "Positive semi-definite"
    if np.all(eigenvalues < 0):
        return "Negative definite"
    if np.all(eigenvalues <= 0) and np.any(eigenvalues == 0):
        return "Negative semi-definite"
    if np.any(eigenvalues > 0) and np.any(eigenvalues < 0):
        return "Indefinite"

    return None
