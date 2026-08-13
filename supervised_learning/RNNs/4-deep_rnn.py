#!/usr/bin/env python3
"""Forward propagation for a deep RNN."""
import numpy as np


def deep_rnn(rnn_cells, X, h_0):
    """Performs forward propagation for a deep RNN."""
    t, m, i = X.shape
    layers = len(rnn_cells)
    h = h_0.shape[2]
    o = rnn_cells[-1].by.shape[1]
    H = np.zeros((t + 1, layers, m, h))  # +1 for the initial state
    Y = np.zeros((t, m, o))
    H[0] = h_0
    for step in range(t):
        x = X[step]
        for layer in range(layers):
            cell = rnn_cells[layer]
            h_next, y = cell.forward(H[step, layer], x)
            H[step + 1, layer] = h_next
            x = h_next
        Y[step] = y
    return H, Y
