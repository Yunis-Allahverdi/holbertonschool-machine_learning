#!/usr/bin/env python3

'''
Doc
'''
import tensorflow as tf


def l2_reg_cost(cost, model):
    '''
    Doc
    '''
    return cost + tf.stack(model.losses)
