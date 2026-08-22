#!/usr/bin/env python3
"""Display a game of Breakout played by the trained DQN agent."""
import gymnasium as gym
from tensorflow.keras.optimizers import Adam
from rl.agents.dqn import DQNAgent
from rl.memory import SequentialMemory
from rl.policy import GreedyQPolicy

train = __import__('train')


def main():
    """Load the trained weights and run a few greedy episodes."""
    env = gym.make('ALE/Breakout-v5',
                   repeat_action_probability=0.0,
                   render_mode='human')
    env = train.CompatibilityWrapper(env)

    nb_actions = env.action_space.n
    model = train.build_model(nb_actions)

    memory = SequentialMemory(limit=1000000,
                              window_length=train.WINDOW_LENGTH)
    dqn = DQNAgent(model=model, nb_actions=nb_actions, memory=memory,
                   processor=train.AtariProcessor(),
                   policy=GreedyQPolicy())
    dqn.compile(Adam(learning_rate=0.00025), metrics=['mae'])

    dqn.load_weights('policy.h5')
    dqn.test(env, nb_episodes=5, visualize=True)
    env.close()


if __name__ == '__main__':
    main()
