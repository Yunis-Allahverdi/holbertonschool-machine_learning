#!/usr/bin/env python3

'''
This module selects every 60th row of these columns
'''


def slice(df):
    '''
    This fumction does same thing like above
    '''
    df = df[['High', 'Low', 'Close', 'Volume_BTC']]
    new_df = pd.DataFrame(columns=['High', 'Low', 'Close', 'Volume_(BTC)'])
    for i in range(0, len(df), 60):
        new_df.loc[len(new_df)] = df.loc[i]

    return new_df
