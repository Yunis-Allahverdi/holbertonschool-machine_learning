#!/usr/bin/env python3

'''
Documented
'''
import numpy as np


def normalize(X, m, s):
    '''
    Doc
    '''
    X = (X - m) / s
    return X
