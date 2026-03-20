#!/usr/bin/env python3

'''
Doc
'''
import numpy as np


def l2_reg_cost(cost, lambtha, weights, L, m):
    '''
    Doc
    '''
    l2_cost = 0

    for i in range(1, L + 1):
        W = weights[f'W{i}']
        l2_cost += np.sum(np.square(W))

    regularization_penalty = (lambtha / (2 * m)) * l2_cost

    return cost + regularization_penalty
