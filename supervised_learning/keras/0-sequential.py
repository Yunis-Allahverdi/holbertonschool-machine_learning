#!/usr/bin/env python3

import tensorflow.keras as K


'''
Documented
'''


def build_model(nx, layers, activations, lambtha, keep_prob):
    '''
    Doc
    '''
    model = [K.layers.Input(shape=(nx,))]
    for n, act in zip(layers, activations):
        model.append(K.layers.Dense(n, activation=act, kernel_regularizer=K.regularizers.l2(lambtha)))
        model.append(K.layers.Dropout(rate=1-keep_prob))

    model.pop()
    return K.Sequential(model)
