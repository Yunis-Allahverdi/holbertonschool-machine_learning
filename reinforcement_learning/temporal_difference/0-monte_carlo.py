#!/usr/bin/env python3
"""Monte Carlo value-estimation algorithm."""
import numpy as np


def monte_carlo(env, V, policy, episodes=5000, max_steps=100,
                alpha=0.1, gamma=0.99):
    """Performs the Monte Carlo algorithm.

    env is the environment instance
    V is a numpy.ndarray of shape (s,) holding the value estimate
    policy takes a state and returns the action to take
    episodes is the number of episodes to train over
    max_steps is the maximum number of steps per episode
    alpha is the learning rate
    gamma is the discount rate
    Returns: V, the updated value estimate
    """
    for _ in range(episodes):
        state = env.reset()[0]

        # Roll out one episode, recording (state, reward) at each step.
        episode = []
        for _ in range(max_steps):
            action = policy(state)
            next_state, reward, terminated, truncated, _ = env.step(action)
            episode.append([state, reward])
            if terminated or truncated:
                break
            state = next_state

        episode = np.array(episode, dtype=int)

        # Walk backward, accumulate the return, first-visit update.
        G = 0
        for i in range(len(episode) - 1, -1, -1):
            state, reward = episode[i]
            G = gamma * G + reward
            if state not in episode[:i, 0]:
                V[state] = V[state] + alpha * (G - V[state])

    return V
