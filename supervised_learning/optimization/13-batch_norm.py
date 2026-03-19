#!/usr/bin/env python3

'''
Documented
'''
import numpy as np


def batch_norm(Z, gamma, beta, epsilon):
    '''
    Doc
    '''
    mu = np.mean(Z, axis=0)
    sigma_2 = np.var(Z, axis=0)
    z_norm = (Z - mu) / (np.sqrt(sigma_2 + epsilon))
    return z_norm * gamma + beta
