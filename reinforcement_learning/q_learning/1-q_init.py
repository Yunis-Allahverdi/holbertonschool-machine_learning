#!/usr/bin/env python3
"""Initializes the Q-table."""
import numpy as np


def q_init(env):
    """Initializes the Q-table as a numpy.ndarray of zeros."""
    states = env.observation_space.n
    actions = env.action_space.n
    return np.zeros((states, actions))
