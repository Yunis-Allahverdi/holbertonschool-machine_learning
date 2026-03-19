#!/usr/bin/env python3

'''
Documented
'''
import numpy as np


def moving_average(data, beta):
    '''
    Doc
    '''
    v = 0
    moving_average = []
    for i in range(len(data)):
        v = beta * v + (1 - beta) * data[i]
        v_corrected = v / (1 - beta ** (i + 1))
        moving_average.append(v_corrected)
    return moving_average
