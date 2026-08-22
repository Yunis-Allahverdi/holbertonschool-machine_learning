# Deep Q-Learning — Atari Breakout

Train and watch a Deep Q-Network agent play Atari's Breakout, built with
`keras`, `keras-rl2` and `gymnasium`.

## Files

| File | Description |
|------|-------------|
| `train.py` | Trains a `DQNAgent` on Breakout and saves the policy network to `policy.h5`. |
| `play.py` | Loads `policy.h5` and displays the agent playing with a `GreedyQPolicy`. |

## Concepts

- **Deep Q-learning** — approximates the action-value function `Q(s, a)`
  with a neural network instead of a lookup table, so it can handle raw
  pixel states.
- **Policy network** — the online CNN that is trained every few steps and
  selects actions.
- **Replay memory** (`SequentialMemory`) — stores past transitions and
  samples random minibatches, breaking the correlation between
  consecutive frames.
- **Target network** — a periodically-synced copy of the policy network
  used to compute the TD targets. Using a *separate, slowly-updated*
  network stops the target from moving every gradient step, which
  stabilizes training (fixed Q-targets).
- **keras-rl2** — a reinforcement-learning library that wraps agents
  (`DQNAgent`), memory (`SequentialMemory`) and policies
  (`EpsGreedyQPolicy`, `GreedyQPolicy`) around a Keras model.

## Requirements

```
python3      3.9   (Ubuntu 20.04 LTS)
numpy        1.25.2
gymnasium    0.29.1
keras        2.15.0
tensorflow   2.15.0
keras-rl2    1.0.4
Pillow       10.3.0
h5py         3.11.0
```

## Installation

```bash
pip install --user keras-rl2==1.0.4
pip install --user gymnasium[atari]==0.29.1
pip install --user tensorflow==2.15.0 keras==2.15.0 numpy==1.25.2
pip install --user Pillow==10.3.0 h5py==3.11.0
pip install autorom[accept-rom-license]
```

## Usage

```bash
./train.py     # trains and writes policy.h5
./play.py      # opens a window and plays 5 greedy episodes
```

## Implementation notes

Two mismatches between the pinned libraries have to be handled:

1. **API mismatch.** `keras-rl2` was written for the old Gym API
   (`reset()` -> obs, `step()` -> `(obs, reward, done, info)`,
   `render(mode=...)`). Gymnasium 0.29 uses `reset()` -> `(obs, info)`,
   `step()` -> `(obs, reward, terminated, truncated, info)` and sets the
   render mode at construction. `CompatibilityWrapper` (a
   `gymnasium.Wrapper`) rewrites `reset`, `step` and `render` to the shape
   keras-rl expects.

2. **Preprocessing.** `gymnasium.wrappers.AtariPreprocessing` depends on
   OpenCV, which is not part of the required dependencies. Instead the
   frames are grayscaled and resized to 84x84 with **Pillow** inside a
   keras-rl `Processor`, and `SequentialMemory(window_length=4)` stacks
   the last four frames into each state.

`nb_steps` in `train.py` is set high on purpose — real Breakout learning
needs on the order of millions of steps. Lower it if you only want a
quick sanity run.
