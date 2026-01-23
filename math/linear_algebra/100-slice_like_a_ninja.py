#!/usr/bin/env python3
'''
Slice of matrix using np
'''


def np_slice(matrix, axes={}):
    """
    Slices a numpy.ndarray along specific axes based on a dictionary.

    Args:
        matrix: A numpy.ndarray to be sliced.
        axes: A dictionary where key is the axis and value is the slice tuple.

    Returns:
        A new numpy.ndarray containing the sliced data.
    """
    # Create a list of default slices (equivalent to :) for every dimension
    # matrix.ndim gives us the total number of axes
    slices = [slice(None)] * matrix.ndim

    # Update the slice list with specific instructions from the axes dict
    for axis, slice_tuple in axes.items():
        slices[axis] = slice(*slice_tuple)

    return matrix[tuple(slices)]
