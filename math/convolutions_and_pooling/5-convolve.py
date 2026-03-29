#!/usr/bin/env python3
'''
Doc
'''

import numpy as np


def convolve(images, kernels, padding='same', stride=(1, 1)):
    '''
    Doc
    '''
    m, h, w, c = images.shape
    kh, kw, kc, nc = kernels.shape
    sh, sw = stride

    if padding == 'same':
        ph = int(np.ceil((((h - 1) * sh + kh - h) / 2)))
        pw = int(np.ceil((((w - 1) * sw + kw - w) / 2)))
    elif padding == 'valid':
        ph = 0
        pw = 0
    else:
        ph, pw = padding

    padded = np.pad(
        images,
        ((0, 0), (ph, ph), (pw, pw), (0, 0)),
        mode='constant'
    )

    output_h = ((h + 2 * ph - kh) // sh) + 1
    output_w = ((w + 2 * pw - kw) // sw) + 1

    output = np.zeros((m, output_h, output_w, nc))

    for i in range(output_h):
        for j in range(output_w):
            row_start = i * sh
            row_end = row_start + kh
            col_start = j * sw
            col_end = col_start + kw

            region = padded[:, row_start:row_end, col_start:col_end, :]

            for k in range(nc):
                output[:, i, j, k] = np.sum(
                    region * kernels[:, :, :, k],
                    axis=(1, 2, 3)
                )

    return output
