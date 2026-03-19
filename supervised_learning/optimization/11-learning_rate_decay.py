#!/usr/bin/env python3

'''
Documented
'''
import numpy as np


def learning_rate_decay(alpha, decay_rate, global_step, decay_step):
    '''
    Doc
    '''
    steps_passed = global_step // decay_step
    alpha_new = alpha / (1 + decay_rate * steps_passed)
    return alpha_new
