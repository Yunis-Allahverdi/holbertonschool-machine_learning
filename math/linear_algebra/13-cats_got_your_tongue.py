#!/usr/bin/env python3
'''
Concat of matrix using np
'''


import numpy as np


def np_cat(mat1, mat2, axis=0):
    '''
    Does same thing as above
    '''
    return np.concatenate((mat1, mat2), axis=axis)
