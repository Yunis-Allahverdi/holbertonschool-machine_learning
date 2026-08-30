#!/usr/bin/env python3
"""Monte-Carlo policy gradient (REINFORCE) utilities."""
import numpy as np


def policy(matrix, weight):
    """Computes the softmax policy for a state matrix and weight.

    matrix is the state (or batch of states)
    weight is the weight matrix
    Returns: the action probabilities for each state
    """
    z = matrix @ weight
    exp = np.exp(z - np.max(z, axis=1, keepdims=True))
    return exp / np.sum(exp, axis=1, keepdims=True)
