#!/usr/bin/env python3
'''
Doc
'''

import numpy as np


def convolve_grayscale_padding(images, kernel, padding):
    '''
    Doc
    '''
    m, h, w = images.shape
    kh, kw = kernel.shape
    ph, pw = padding

    # pad images with zeros
    padded = np.pad(images,
                    ((0, 0), (ph, ph), (pw, pw)),
                    mode='constant')

    h_out = h + 2 * ph - kh + 1
    w_out = w + 2 * pw - kw + 1

    output = np.zeros((m, h_out, w_out))

    for i in range(h_out):
        for j in range(w_out):
            region = padded[:, i:i + kh, j:j + kw]
            output[:, i, j] = np.sum(region * kernel, axis=(1, 2))

    return output
