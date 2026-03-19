#!/usr/bin/env python3

'''
Documented
'''
import numpy as np


def update_variables_RMSProp(alpha, beta2, epsilon, var, grad, s):
    '''
    Doc
    '''
    s = beta2 * s + (1 - beta2) * (grad ** 2)
    var = var - alpha * ((grad) / (sqrt(s) + epsilon))
    return var, s
