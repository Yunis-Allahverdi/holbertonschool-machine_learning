#!/usr/bin/env python3

'''
Documented
'''
import tensorflow.keras as K


def save_weights(network, filename, save_format='keras'):
    '''
    Doc
    '''
    network.save_weights(filename)
    return None


def load_weights(network, filename):
    '''
    Doc
    '''
    network.load_weights(filename)
