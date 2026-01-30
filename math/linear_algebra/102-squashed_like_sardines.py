#!/usr/bin/env python3
'''
Concat two matrices along a specific axis
'''


def cat_matrices(mat1, mat2, axis=0):
    '''
    Does same thing as above
    '''
    if axis == 0:
        if not isinstance(mat1, list) or not isinstance(mat2, list):
            return None
        if len(mat1) > 0 and len(mat2) > 0:
            if isinstance(mat1[0], list) != isinstance(mat2[0], list):
                return None
        return mat1 + mat2

    if not isinstance(mat1, list) or not isinstance(mat2, list):
        return None

    if len(mat1) != len(mat2):
        return None

    res = []
    for i in range(len(mat1)):
        sub_res = cat_matrices(mat1[i], mat2[i], axis - 1)
        if sub_res is None:
            return None
        res.append(sub_res)

    return res
