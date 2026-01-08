#!/usr/bin/env python3

'''
This module selects last 10 rows and
converts them into numpy array
'''
import pandas as pd


def array(df):
    '''
    This fumction does same thing like above
    '''
    df = df['High', 'Close'].tail(10)
    numpy_array = df.to_numpy()
    return numpy_array
