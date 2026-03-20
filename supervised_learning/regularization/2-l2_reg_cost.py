#!/usr/bin/env python3

'''
Doc
'''
import tensorflow as tf


def l2_reg_cost(cost, model):
    '''
    Doc
    '''
    l2_terms = []
    for layer in model.layers:
        if hasattr(layer, 'kernel_regularizer') and layer.kernel_regularizer:
            l2_terms.append(layer.kernel_regularizer(layer.kernel))
        else:
            l2_terms.append(tf.constant(0.0, dtype=tf.float32))
    return tf.stack([cost] + l2_terms)
