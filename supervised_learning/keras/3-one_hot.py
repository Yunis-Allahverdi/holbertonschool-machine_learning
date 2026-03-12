#!/usr/bin/env python3

'''
Documented
'''
import tensorflow.keras as K


def one_hot(labels, classes=None):
    '''
    Doc
    '''
    return K.ops.one_hot(labels, num_classes=classes)
