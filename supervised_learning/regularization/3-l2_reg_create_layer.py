#!/usr/bin/env python3

'''
Doc
'''
import tensorflow as tf


def l2_reg_create_layer(prev, n, activation, lambtha):
    '''
    Doc
    '''
    layer = tf.keras.layers.Dense(
        units=n,
        activation=activation,
        kernel_regularizer=tf.keras.regularizers.l2(lambtha)
    )

    return layer(prev)
