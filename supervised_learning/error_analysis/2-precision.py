#!/usr/bin/env python3
'''
Doc
'''
import numpy as np


def precision(confusion):
    '''
    My function document
    '''
    tp = np.diag(confusion)
    actual_positives = np.sum(confusion, axis=0)
    return tp / actual_positives
