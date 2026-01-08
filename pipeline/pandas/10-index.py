#!/usr/bin/env python3

'''
This module sets index
'''


def fill(df):
    '''
    This fumction does same thing like above
    '''
    df = df.set_index('Timestamp')
    return df
