#!/usr/bin/env python3
'''
Doc
'''
import numpy as np


def specificity(confusion):
    '''
    My function document
    '''
    total = np.sum(confusion)
    tp = np.diag(confusion)
    positives = np.sum(confusion, axis=1)
    predicted_positives = np.sum(confusion, axis=0)
    fp = predicted_positives - tp
    fn = positives - tp
    tn = total - (tp + fp + fn)

    return tn / (tn + fp)
