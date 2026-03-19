#!/usr/bin/env python3

'''
Documented
'''
import numpy as np


def update_variables_momentum(alpha, beta1, var, grad, v):
    '''
    Doc
    '''
    v_t = beta1 * v + (1 - beta1) * grad
    var = var - alpha * v_t
    return var, v_t
