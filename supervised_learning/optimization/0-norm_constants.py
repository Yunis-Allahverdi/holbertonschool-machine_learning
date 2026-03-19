#!/usr/bin/env python3

'''
Documented
'''
import tensorflow as tf


def normalization_constants(X):
    '''
    Doc
    '''
    return tf.nn.moments(
        X, axes=[0]
    )
