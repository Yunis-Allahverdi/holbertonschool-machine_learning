#!/usr/bin/env python3
'''
Doc
'''
import numpy as np


def specificity(confusion):
    '''
    My function document
    '''
    fp = confusion[0, 1:].sum()
    tn = confusion[1:, 1:].sum()
    return tn / (fp + tn)
