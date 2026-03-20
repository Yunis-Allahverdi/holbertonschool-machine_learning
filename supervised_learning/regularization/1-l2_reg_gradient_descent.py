#!/usr/bin/env python3

'''
Doc
'''
import numpy as np


def l2_reg_gradient_descent(Y, weights, cache, alpha, lambtha, L):
    '''
    Doc
    '''
    m = Y.shape[1]
    dZ = cache['A' + str(l - 1)] if l > 1 else cache['A0']

    dW = (1 / m) * np.dot(dZ, A_prev.T) + (lambtha / m) * weights['W' + str(l)]
    db = (1 / m) * np.sum(dZ, axis=1, keepdims=True)

    weights['W' + str(l)] -= alpha * dW
    weights['b' + str(l)] -= alpha * db

    if l > 1:
        W_l = weights['W' + str(l)]
        A_prev_raw = cache['A' + str(l - 1)]

        dZ = np.dot(W_l.T, dZ) * (1 - A_prev_raw ** 2)
