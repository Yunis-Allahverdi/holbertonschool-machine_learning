#!/usr/bin/env python3
'''
Concat two matrices along a specific axis
'''


def cat_matrices(mat1, mat2, axis=0):
    '''
    Does same thing as above
    '''
    if axis != 0:
        if len(mat1) != len(mat2):
            return None

    # Base Case: Concatenate at the target axis
    if axis == 0:
        # Check if the internal structures match (rank check)
        # We ensure that if one is a list, the other is too,inner shapes match
        m1, m2 = mat1, mat2
        while isinstance(m1, list) and isinstance(m2, list):
            if len(m1) != len(m2) and axis != 0:  # This part handled recursion
                return None
            if not m1 or not m2:
                break
            m1, m2 = m1[0], m2[0]
        if isinstance(m1, list) != isinstance(m2, list):
            return None

        return mat1 + mat2

    # Recursive Step: Dive into the next dimension
    res = []
    for i in range(len(mat1)):
        sub_res = cat_matrices(mat1[i], mat2[i], axis - 1)
        if sub_res is None:
            return None
        res.append(sub_res)

    return res
