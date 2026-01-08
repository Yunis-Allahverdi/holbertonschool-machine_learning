#!/usr/bin/env python3

'''
This module selects every 60th row of these columns
'''
import pandas as pd


def slice(df):
    '''
    This fumction does same thing like above
    '''
    df = df[['High', 'Low', 'Close', 'Volume_(BTC)']]
    new_df = [df[i] for i in range(0, len(df), 60)]
    return new_df
