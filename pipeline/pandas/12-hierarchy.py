#!/usr/bin/env python3
'''
This module joins two dataset
'''
import pandas as pd
index = __import__('10-index').index


def hierarchy(df1, df2):
    '''
    Same with function
    '''
    df1 = index(df1)
    df2 = index(df2)
    df1 = df1.loc[1417411980:1417417980]
    df2 = df2.loc[1417411980:1417417980]
    df = pd.concat([df2, df1], axis=0, keys=["bitstamp", "coinbase"])
    return df
