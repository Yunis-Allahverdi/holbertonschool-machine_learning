#!/usr/bin/env python3

'''
This module selects every 60th row of these columns
'''


def slice(df):
    '''
    This fumction does same thing like above
    '''
    df = df[['High', 'Low', 'Close', 'Volume_(BTC)']]
    new_df = [df[i] if i % 60 == 0]
    return new_df
