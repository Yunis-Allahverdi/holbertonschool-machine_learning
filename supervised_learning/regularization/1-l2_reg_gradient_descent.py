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
    dZ = cache['A' + str(L)] - Y

    for i in reversed(range(1, L + 1)):
        A_prev = cache['A' + str(i - 1)] if i > 1 else cache['A0']
        dW = (1 / m) * np.dot(dZ, A_prev.T) + (
             (lambtha / m) * weights['W' + str(i)])
        db = (1 / m) * np.sum(dZ, axis=1, keepdims=True)

        if i > 1:
            A_prev_raw = cache['A' + str(i - 1)]
            dZ = np.dot(weights['W' + str(i)].T, dZ) * (1 - A_prev_raw ** 2)

        weights['W' + str(i)] -= alpha * dW
        weights['b' + str(i)] -= alpha * db
