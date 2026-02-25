#!/usr/bin/env python3
'''
Doc
'''
import numpy as np


def create_confusion_matrix(labels, logits):
    '''
    My function document
    '''
    return np.dot(labels.T, logits)
