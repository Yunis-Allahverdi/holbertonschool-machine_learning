#!/usr/bin/env python3

'''
Documented
'''
import numpy as np


def normalization_constants(X):
    '''
    Doc
    '''
    m = np.mean(X, axis=0)
    s = np.std(X, axis=0)
    return m, s
