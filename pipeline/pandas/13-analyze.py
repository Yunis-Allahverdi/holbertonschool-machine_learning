#!/usr/bin/env python3
'''
This module computes desc() except Timestamp column
'''


def analyze(df):
    '''
    Same with above
    '''
    df = df.drop(columns=['Timestamp'])
    return df.describe()
