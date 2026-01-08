#!/usr/bin/env python3

'''
This module fills data
'''


def fill(df):
    '''
    This fumction does same thing like above
    '''
    df.drop('Weighted_Price', axis=1, inplace=True)
    df['Close'].fillna(method='pad', inplace=True)
    df['High'] = df['High'].fillna(df['Close'])
    df['Low'] = df['Low'].fillna(df['Close'])
    df['Open'] = df['Open'].fillna(df['Close'])
    df['Volume_(BTC)'].fillna(0)
    df['Volume_(Currency)'].fillna(0)
    return df
