#!/usr/bin/env python3

'''
This module drop NaNs
'''


def prune(df):
    '''
    This fumction does same thing like above
    '''
    df = df.dropna(subset=['Close'])
    return df
