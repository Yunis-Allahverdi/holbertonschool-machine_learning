#!/usr/bin/env python3

'''
Documented
'''
import tensorflow.keras as K
import numpy as np


def one_hot(labels, classes=None):
    '''
    Doc
    '''
    m = labels.shape[0]
    one_hot_matrix = np.zeros((m, classes))
    one_hot_matrix[np.arange(m), labels] = 1
    return one_hot_matrix
