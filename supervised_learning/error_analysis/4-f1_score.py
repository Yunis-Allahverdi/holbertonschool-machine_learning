#!/usr/bin/env python3
'''
Doc
'''
import numpy as np

precision = __import__('2-precision').precision
sensitivity = __import__('1-sensitivity').sensitivity


def f1_score(confusion):
    '''
    My function document
    '''
    p = precision_func(confusion)
    s = sensitivity_func(confusion)
 
    return 2 * (p * s) / (p + s)
