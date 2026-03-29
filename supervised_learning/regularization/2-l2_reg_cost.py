#!/usr/bin/env python3

'''
Doc
'''
import tensorflow as tf


def l2_reg_cost(cost, model):
    '''
    Doc
    '''
    l2_losses = tf.add_n(model.losses)
    total_cost = cost + l2_losses

    return total_cost
