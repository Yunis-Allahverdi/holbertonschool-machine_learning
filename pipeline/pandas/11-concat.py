#!/usr/bin/env python3

'''
This module sets index
'''
import pandas as pd
index = __import__('10-index').index


def concat(df1, df2):
    '''
    This fumction does same thing like above
    '''
    df1 = index(df1)
    df2 = index(df2)
    res = pd.concat([df1, df2], keys=["coinbase", "bitstamp"], ignore_index=True)
    return res
