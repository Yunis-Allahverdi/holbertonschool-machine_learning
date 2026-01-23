#!/usr/bin/env python3
'''
Multiplication of matrix
'''


def mat_mul(mat1, mat2):
    '''
    Does same thing as above
    '''
    if len(mat1[0]) == len(mat2):
        new_mat = [[0]*len(mat2[0]) for _ in range(len(mat1))]
        for i in range(len(mat1)):
            for j in range(len(mat2[0])):
                for k in range(len(mat2)):
                    new_mat[i][j] += mat1[i][k] * mat2[k][j]

        return new_mat
    return None
