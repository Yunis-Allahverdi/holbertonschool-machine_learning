#!/usr/bin/env python3

'''
Documented
'''
import tensorflow.keras as K


def test_model(network, data, labels, verbose=True):
    '''
    Doc
    '''
    loss, accuracy = network.evaluate(data, labels, verbose=verbose)
    return [loss, accuracy]
