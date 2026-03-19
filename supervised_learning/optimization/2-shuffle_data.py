#!/usr/bin/env python3

'''
Documented
'''
import numpy as np


def shuffle_data(X, Y):
    '''
    Doc
    '''
    m = X.shape[0]
    shuffle = np.random.permutation(m)
    return X[shuffle], Y[shuffle]
