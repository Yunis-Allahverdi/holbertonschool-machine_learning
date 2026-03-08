#!/usr/bin/env python3
'''
Doc
'''
import numpy as np


class Neuron:
    '''
    Doc
    '''

    def __init__(self, nx):

        if not isinstance(nx, int):
            raise TypeError('nx must be an integer')

        if nx < 1:
            raise ValueError('nx must be a positive integer')

        self.__W = np.random.randn(1, nx)
        self.__b = 0
        self.__A = 0

    def forward_prop(self, x):
        '''
        Doc
        '''

        Z = np.dot(self.__W, x) + self.__b
        self.__A = 1 / (1 + np.exp(-Z))
        return self.__A

    @property
    def W(self):
        '''Getter for W'''
        return self.__W

    @property
    def b(self):
        '''Getter for b'''
        return self.__b

    @property
    def A(self):
        '''Getter for A'''
        return self.__A
