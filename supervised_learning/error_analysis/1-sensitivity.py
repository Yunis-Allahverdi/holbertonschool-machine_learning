#!/usr/bin/env python3
'''
Doc
'''
import numpy as np


def sensitivity(confusion):
    '''
    My function document
    '''
    tp = np.diag(confusion)
    actual_positives = np.sum(confusion, axis=1)
    return tp / actual_positives
