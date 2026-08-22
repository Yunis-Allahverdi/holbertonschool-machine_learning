#!/usr/bin/env python3
"""Train a DQN agent to play Atari's Breakout using keras-rl2."""
import numpy as np
import gymnasium as gym
from PIL import Image
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, Flatten, Permute
from tensorflow.keras.optimizers import Adam
from rl.agents.dqn import DQNAgent
from rl.memory import SequentialMemory
from rl.policy import EpsGreedyQPolicy, LinearAnnealedPolicy
from rl.core import Processor


WINDOW_LENGTH = 4
INPUT_SHAPE = (84, 84)


class CompatibilityWrapper(gym.Wrapper):
    """Bridge the Gymnasium API to the old Gym API keras-rl expects."""

    def step(self, action):
        """Return (observation, reward, done, info) from one step."""
        obs, reward, terminated, truncated, info = self.env.step(action)
        return obs, reward, terminated or truncated, info

    def reset(self, **kwargs):
        """Return only the observation from a reset."""
        obs, info = self.env.reset(**kwargs)
        return obs

    def render(self, *args, **kwargs):
        """Render using the render_mode fixed at creation time."""
        return self.env.render()


class AtariProcessor(Processor):
    """Grayscale/resize frames, scale batches and clip rewards."""

    def process_observation(self, observation):
        """Convert a raw frame to an 84x84 grayscale uint8 image."""
        img = Image.fromarray(observation).resize(INPUT_SHAPE)
        img = img.convert('L')
        return np.array(img).astype('uint8')

    def process_state_batch(self, batch):
        """Scale a batch of stacked frames to the [0, 1] range."""
        return batch.astype('float32') / 255.0

    def process_reward(self, reward):
        """Clip rewards to the [-1, 1] range."""
        return np.clip(reward, -1.0, 1.0)


def build_model(nb_actions):
    """Build the convolutional policy network."""
    model = Sequential()
    model.add(Permute((2, 3, 1),
                      input_shape=(WINDOW_LENGTH,) + INPUT_SHAPE))
    model.add(Conv2D(32, (8, 8), strides=(4, 4), activation='relu'))
    model.add(Conv2D(64, (4, 4), strides=(2, 2), activation='relu'))
    model.add(Conv2D(64, (3, 3), strides=(1, 1), activation='relu'))
    model.add(Flatten())
    model.add(Dense(512, activation='relu'))
    model.add(Dense(nb_actions, activation='linear'))
    return model


def build_agent(model, nb_actions):
    """Create and compile the DQN agent."""
    memory = SequentialMemory(limit=1000000, window_length=WINDOW_LENGTH)
    policy = LinearAnnealedPolicy(EpsGreedyQPolicy(), attr='eps',
                                  value_max=1.0, value_min=0.1,
                                  value_test=0.05, nb_steps=1000000)
    dqn = DQNAgent(model=model, nb_actions=nb_actions, memory=memory,
                   processor=AtariProcessor(), policy=policy,
                   nb_steps_warmup=50000, gamma=0.99,
                   target_model_update=10000, train_interval=4,
                   delta_clip=1.0)
    dqn.compile(Adam(learning_rate=0.00025), metrics=['mae'])
    return dqn


def main():
    """Build the environment, train the agent and save the weights."""
    env = gym.make('ALE/Breakout-v5',
                   repeat_action_probability=0.0)
    env = CompatibilityWrapper(env)

    nb_actions = env.action_space.n
    model = build_model(nb_actions)
    dqn = build_agent(model, nb_actions)

    dqn.fit(env, nb_steps=1750000, log_interval=10000, visualize=False)
    dqn.save_weights('policy.h5', overwrite=True)
    env.close()


if __name__ == '__main__':
    main()
