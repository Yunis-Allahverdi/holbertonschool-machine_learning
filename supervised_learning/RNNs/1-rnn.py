#!/usr/bin/env python3
"""Forward propagation for a simple RNN."""
import numpy as np


def rnn(rnn_cell, X, h_0):
    """Performs forward propagation for a simple RNN."""
    t, m, i = X.shape              # t = time steps, m = batch size, i = input dim
    h = h_0.shape[1]              # h = hidden state dim
    o = rnn_cell.by.shape[1]     # o = output dim (read off the output bias)
    H = np.zeros((t + 1, m, h))  # holds initial state + one state per step
    Y = np.zeros((t, m, o))      # holds one output per step
    H[0] = h_0                    # put the initial hidden state at the front
    for step in range(t):         # walk through the sequence one step at a time
        h_next, y = rnn_cell.forward(H[step], X[step])  # feed prev state + current input
        H[step + 1] = h_next     # save the new hidden state
        Y[step] = y              # save this step's output
    return H, Y                   # H: (t+1, m, h), Y: (t, m, o)
