#!/usr/bin/env python3

'''
Documented
'''
import tensorflow as tf


def learning_rate_decay(alpha, decay_rate, decay_step):
    '''
    Doc
    '''
    alpha = tf.keras.optimizers.schedules.InverseTimeDecay(
        initial_learning_rate=alpha,
        decay_steps=decay_step,
        decay_rate=decay_rate,
        staircase=True
    )
    return alpha
