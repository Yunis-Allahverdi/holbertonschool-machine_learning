#!/usr/bin/env python3

'''
Documented
'''
import tensorflow.keras as K


def save_model(network, filename):
    '''
    Doc
    '''
    K.models.save_model(
        network, filename,
    )
    return None


def load_model(filename):
    '''
    Doc
    '''
    return K.models.load_model(filename)
