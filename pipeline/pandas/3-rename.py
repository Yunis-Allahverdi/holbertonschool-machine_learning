#!/usr/bin/env python3

'''
This module converts and renames Timestamp column
'''
import pandas as pd


def rename(df):
    '''
    This function loads data with delimiter
    '''
    df['Datetime'] = pd.to_datatime(df['Timestamp'],unit='s')
    new_df = df[['Datetime', 'Close']]
    return new_df
