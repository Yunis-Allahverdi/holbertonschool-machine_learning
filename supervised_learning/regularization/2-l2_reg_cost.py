#!/usr/bin/env python3

'''
Doc
'''
import tensorflow as tf


def l2_reg_cost(cost, model):
    '''
    Doc
    '''
    l2_terms = [layer.kernel_regularizer(layer.kernel)
                for layer in model.layers
                if hasattr(layer, 'kernel_regularizer') and layer.kernel_regularizer]
    return tf.stack([cost] + l2_terms)
