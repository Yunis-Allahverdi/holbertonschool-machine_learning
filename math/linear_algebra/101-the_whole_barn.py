#!/usr/bin/env python3
'''
Addition of two matrices
'''


def add_matrices(mat1, mat2):
    '''
    Does same thing as above
    '''
    if len(mat1) == len(mat2) and len(mat1[0]) == len(mat2[0]):
        res = []
        res = [[mat1[i][j] + mat2[i][j]
                for j in range(len(mat1[0]))] for i in range(len(mat1))]
        return res
    else:
        return None
