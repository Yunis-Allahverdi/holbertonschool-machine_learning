#!/usr/bin/env python3

'''
Documented
'''
import tensorflow as tf


def create_momentum_op(alpha, beta1):
    '''
    Doc
    '''
    optimizer = tf.optimizers.SGD(learning_rate=alpha, momentum=beta1)
    return optimizer
