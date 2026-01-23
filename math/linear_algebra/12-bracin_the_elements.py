#!/usr/bin/env python3
import numpy as np
'''
Calc of matrix using np
'''


def np_elementwise(mat1, mat2):
    '''
    Does same thing as above
    '''
    add = np.add(mat1, mat2)
    sub = np.subtract(mat1, mat2)
    mul = np.multiply(mat1, mat2)
    div = np.divide(mat1, mat2)
    return add, sub, mul, div
