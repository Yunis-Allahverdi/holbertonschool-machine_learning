#!/usr/bin/env python3

'''
Documented
'''
import tensorflow.keras as K


def save_config(network, filename):
    config = network.to_json()
    with open(filename, "w") as f:
        f.write(config)


def load_config(filename):
    with open(filename, "r") as f:
        config = f.read()

    return K.models.model_from_json(config)
