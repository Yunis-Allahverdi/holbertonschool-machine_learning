#!/usr/bin/env python3
'''
Doc
'''

import numpy as np


def convolve_grayscale_same(images, kernel):
    '''
    Doc
    '''
    m, h, w = images.shape
    kh, kw = kernel.shape

    # padding sizes
    ph = kh // 2
    pw = kw // 2
