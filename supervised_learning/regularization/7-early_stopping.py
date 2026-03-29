#!/usr/bin/env python3

'''
Doc
'''


def early_stopping(cost, opt_cost, threshold, patience, count):
    '''
    Doc
    '''
    if opt_cost - cost < threshold:
        count += 1
    else:
        count = 0

    return count >= patience, count
