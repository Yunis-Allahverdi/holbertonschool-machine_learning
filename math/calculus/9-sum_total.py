#!/usr/bin/env python3

'''
This module calc the sigma with closed form
'''


def summation_i_squared(n):
    '''
    This function does same thing as above
    '''
    if not isinstance(n, int) or n <= 0:
        return None

    return n*(n+1)*(2*n+1)) // 6
