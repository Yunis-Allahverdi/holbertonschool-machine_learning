#!/usr/bin/env python3

'''
This module selects last 10 rows and
converts them into array
'''
import pandas as pd


def array(df):
    '''
    This fumction does same thing like above
    '''
    dt = df['High', 'Close'].tail(10)
    numpy_array = dt.to_numpy()
    return numpy_array
