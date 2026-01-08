#!/usr/bin/env python3
'''
My module document
'''
import pandas as pd
index = __import__('10-index').index


def concat(df1, df2):
    '''
    My function document
    '''
    df1 = index(df1)
    df2 = index(df2)
    df = pd.concat([df1, df2], keys=["coinbase", "bitstamp"])
    return df
