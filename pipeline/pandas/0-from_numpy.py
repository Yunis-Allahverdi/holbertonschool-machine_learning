#!/usr/bin/env python3

'''
This module creates np array and assign it to df
Before that we need to upload pandas library
'''
import pandas as pd


def from_numpy(array):
    '''
    This function creates orders then assign them to dataframe as columns
    '''
    orders = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
    df = pd.DataFrame(array, columns=orders[:array.shape[1]])
    return df
