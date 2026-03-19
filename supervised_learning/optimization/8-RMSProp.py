#!/usr/bin/env python3

'''
Documented
'''
import tensorflow as tf


def create_RMSProp_op(alpha, beta2, epsilon):
    '''
    Doc
    '''
    optimizer = tf.keras.optimizers.RMSprop(
                                            learning_rate=alpha,
                                            rho=beta2,
                                            epsilon=epsilon
                                            )
    return optimizer
