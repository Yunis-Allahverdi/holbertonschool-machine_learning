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
    return 2 * (precision * sensitivity) / (precision + sensitivity)
