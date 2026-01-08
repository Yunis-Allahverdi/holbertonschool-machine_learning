#!/usr/bin/env python3

'''
This module sets index
'''


def index(df):
    '''
    This fumction does same thing like above
    '''
    new_df = df.set_index('Timestamp')
    return new_df
