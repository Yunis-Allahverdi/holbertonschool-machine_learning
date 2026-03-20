#!/usr/bin/env python3

'''
Doc
'''
import tensorflow as tf


def l2_reg_cost(cost, model):
    '''
    Doc
    '''
    l2_term = 0.0

    for layer in model.layers:
        if (hasattr(layer, 'kernel_regularizer') and
            layer.kernel_regularizer is not None):
            l2_term += tf.reduce_sum(
                    layer.kernel_regularizer(layer.kernel))

    total_cost = cost + l2_term
    return total_cost
