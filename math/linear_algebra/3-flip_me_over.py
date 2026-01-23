#!/usr/bin/env python3
'''
Find the transpose of matrix
'''


def matrix_transpose(matrix):
    '''
    Does same thing as above
    '''
    transposed_matrix = [[
        matrix[j][i] for j in range(len(matrix))]
            for i in range(len(matrix[0]))]
    return transposed_matrix
