#!/usr/bin/env python3

'''
Doc
'''
import tensorflow as tf


def l2_reg_create_layer(prev, n, activation, lambtha):
    '''
    Doc
    '''
    regularizer = tf.keras.regularizers.l2(lambtha)
    init = tf.keras.initializers.VarianceScaling(scale=2.0, mode="fan_avg")
    tensor = tf.keras.layers.Dense(
        units=n,
        activation=activation,
        kernel_initializer=init,
        kernel_regularizer=regularizer,
    )

    return tensor(prev)
