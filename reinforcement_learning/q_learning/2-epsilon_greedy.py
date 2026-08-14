#!/usr/bin/env python3
"""Uses epsilon-greedy to determine the next action."""
import numpy as np


def epsilon_greedy(Q, state, epsilon):
    """Determines the next action using epsilon-greedy."""
    p = np.random.uniform(0, 1)
    if p < epsilon:
        action = np.random.randint(0, Q.shape[1])
    else:
        action = np.argmax(Q[state])
    return action
