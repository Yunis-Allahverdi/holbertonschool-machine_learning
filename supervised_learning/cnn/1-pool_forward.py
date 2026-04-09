#!/usr/bin/env python3
'''
pooling forward prop
'''

import numpy as np


def ceil(a):
    """
    ceil function
    """
    b = a // 1
    if a != b:
        return int(b + 1)
    return int(a)


def pool_forward(A_prev, kernel_shape, stride=(1, 1), mode="max"):
    '''
    Func
    '''

    m, h_prev, w_prev, c_prev = A_prev.shape
    kh, kw = kernel_shape
    sh, sw = stride

    nh = (h_prev - kh) // sh + 1
    nw = (w_prev - kw) // sw + 1

    output = np.zeros((m, nh, nw, c_prev))

    for i in range(m):
        a_prev = A_prev[i]
        for h in range(nh):
            for w in range(nw):
                for c in range(c_prev):
                    patch = a_prev[h * sh: h * sh + kh, w * sw: w * sw + kw, c]
                    if mode == 'max':
                        output[i, h, w, c] = np.max(patch)
                    elif mode == 'avg':
                        output[i, h, w, c] = np.mean(patch)

    return output
