#!/usr/bin/env python3

import pandas as pd
import numpy as np


'''
This module creates np array and assign it to df
'''


def from_numpy(array):
    orders = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
    df = pd.DataFrame(array, columns=orders[:array.shape[1]])
    return df
