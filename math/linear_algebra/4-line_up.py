#!/usr/bin/env python3
'''
Addition of matrix
'''


def add_arrays(arr1, arr2):
    '''
    Does same thing as above
    '''
    new_arr = [0] * len(arr1)
    if len(arr1) == len(arr2):
        for i in range(len(arr1)):
            new_arr[i] = arr1[i] + arr2[i]

        return new_arr
    return None
