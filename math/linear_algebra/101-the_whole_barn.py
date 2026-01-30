#!/usr/bin/env python3
'''
Addition of two matrices
'''


def add_matrices(mat1, mat2):
    '''
    Does same thing as above
    '''
    if len(mat1) != len(mat2):
        return None

    if not isinstance(mat1[0], list):
        if isinstance(mat2[0], list):
            return None
        return [mat1[i] + mat2[i] for i in range(len(mat1))]

    res = []
    for i in range(len(mat1)):
        sub_res = add_matrices(mat1[i], mat2[i])
        if sub_res is None:
            return None
        res.append(sub_res)

    return res
