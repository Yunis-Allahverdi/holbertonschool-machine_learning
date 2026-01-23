#!/usr/bin/env python3
'''
Concatenation of matrix
'''


def cat_arrays(arr1, arr2):
    '''
    Does same thing as above
    '''
    new_list = arr1.copy()
    for i in arr2:
        new_list.append(i)

    return new_list
