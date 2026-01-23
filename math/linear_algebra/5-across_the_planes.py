#!/usr/bin/env python3
'''
Addition of matrix
'''


def add_matrices2D(mat1, mat2):
    '''
    Does same thing as above
    '''
    rows = len(mat1)
    cols = len(mat1[0])
    new_mat = [[0 for _ in range(cols)] for _ in range(rows)]
    if len(mat1[0]) == len(mat2[0]):
        for i in range(rows):
            for j in range(cols):
                new_mat[i][j] = mat1[i][j] + mat2[i][j]
        return new_mat
    return None
