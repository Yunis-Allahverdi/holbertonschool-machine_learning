#!/usr/bin/env python3

'''
Doc
'''
import tensorflow as tf


def dropout_create_layer(prev, n, activation, keep_prob, training=True):
    '''
    Doc
    '''
    initializer = tf.keras.initializers.VarianceScaling(
        scale=2.0,
        mode=("fan_avg")
    )

    layer = tf.keras.layers.Dense(
        units=n,
        activation=activation,
        kernel_initializer=initializer
    )

    output = layer(prev)
    output = tf.keras.layers.Dropout(1 - keep_prob)(output, training=training)
    return output
