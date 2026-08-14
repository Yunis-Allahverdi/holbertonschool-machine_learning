#!/usr/bin/env python3
"""Performs Q-learning on the FrozenLake environment."""
import numpy as np
epsilon_greedy = __import__('2-epsilon_greedy').epsilon_greedy


def train(env, Q, episodes=5000, max_steps=100, alpha=0.1, gamma=0.99,
          epsilon=1, min_epsilon=0.1, epsilon_decay=0.05):
    """Performs Q-learning and returns the updated Q-table and rewards."""
    max_epsilon = epsilon
    total_rewards = []

    for episode in range(episodes):
        state = env.reset()[0]
        done = False
        episode_reward = 0

        for step in range(max_steps):
            action = epsilon_greedy(Q, state, epsilon)
            new_state, reward, terminated, truncated, info = env.step(action)

            if terminated and reward == 0:
                reward = -1

            Q[state, action] = Q[state, action] + alpha * (
                reward + gamma * np.max(Q[new_state]) - Q[state, action])

            state = new_state
            episode_reward = episode_reward + reward

            if terminated or truncated:
                break

        epsilon = min_epsilon + (max_epsilon - min_epsilon) * np.exp(
            -epsilon_decay * episode)
        total_rewards.append(episode_reward)

    return Q, total_rewards
