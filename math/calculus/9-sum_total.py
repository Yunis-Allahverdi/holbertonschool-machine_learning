#!/usr/bin/env python3

'''
This module calc the sigma with closed form
'''


def summation_i_squared(n):
    '''
    This function does same thing as above
    '''
    if type(n) is int:
        return (n*(n+1)*(2*n+1))/6
    return None
