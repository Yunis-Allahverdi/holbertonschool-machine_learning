#!/usr/bin/env python3
'''
This module plots scatter plot with colormap
'''
import numpy as np
import matplotlib.pyplot as plt


def gradient():
    '''
    This function does same thing as above
    '''
    x = np.random.randn(2000) * 10
    y = np.random.randn(2000) * 10
    z = np.random.rand(2000) + 40 - np.sqrt(np.square(x) + np.square(y))
    plt.figure(figsize=(6.4, 4.8))

    plt.scatter(x, y, c=z)
    plt.colorbar(label='elevation (m)')
    plt.xlabel('x coordinate (m)')
    plt.ylabel('y coordinate (m)')
    plt.title('Mountain Elevation')
    plt.show()
