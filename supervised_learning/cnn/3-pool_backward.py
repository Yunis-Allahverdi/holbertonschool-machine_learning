#!/usr/bin/env python3
'''
pooling back propogation
'''

import numpy as np


def pool_backward(dA, A_prev, kernel_shape, stride=(1, 1), mode="max"):
    '''
    func
    '''
    m, h_prev, w_prev, c_prev = A_prev.shape
    kh, kw = kernel_shape
    sh, sw = stride
    _, h_new, w_new, _ = dA.shape
    dA_prev = np.zeros_like(A_prev)
    for i in range(m):
        a_prev = A_prev[i]
        da = dA[i]
        for h in range(h_new):
            for w in range(w_new):
                for c in range(c_prev):
                    patch = a_prev[h * sh: h * sh + kh, w * sw: w * sw + kw, c]
                    if mode == 'max':
                        mask = (patch == np.max(patch))
                        dA_prev[i, h * sh: h * sh + kh,
                                w * sw: w * sw + kw,
                                c] += mask * da[h, w, c]
                    elif mode == 'avg':
                        average = da[h, w, c] / (kh * kw)
                        dA_prev[i, h * sh: h * sh + kh,
                                w * sw: w * sw + kw,
                                c] += np.ones((kh, kw)) * average
    return dA_prev
