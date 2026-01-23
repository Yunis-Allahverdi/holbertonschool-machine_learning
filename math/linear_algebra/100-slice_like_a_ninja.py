#!/usr/bin/env python3
'''
Slice of matrix using np
'''


import numpy as np


def np_slice(matrix, axes={}):
    '''
    Does same thing as above
    '''
    row_val = axes.get(0, slice(None))
    col_val = axes.get(1, slice(None))
    row_idx = slice(*row_val) if isinstance(row_val, tuple) else row_val
    col_idx = slice(*col_val) if isinstance(col_val, tuple) else col_val
    return matrix[row_idx, col_idx]
