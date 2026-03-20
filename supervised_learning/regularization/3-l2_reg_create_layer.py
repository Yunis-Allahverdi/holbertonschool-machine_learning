#!/usr/bin/env python3

'''
Doc
'''
import tensorflow as tf


def l2_reg_create_layer(prev, n, activation, lambtha):
    '''
    Doc
    '''
    return tf.keras.layers.Dense(
        n,
        activation=activation,
        kernel_initializer=tf.keras.initializers.GlorotUniform(seed=0),
        kernel_regularizer=tf.keras.regularizers.L2(l2=lambtha)
    )(prev)
