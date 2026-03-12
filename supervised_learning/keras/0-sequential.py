#!/usr/bin/env python3

import tensorflow.keras as K


'''
Documented
'''


def build_model(nx, layers, activations, lambtha, keep_prob):
    '''
    Doc
    '''
    model = Sequential()
    model.add(Dense(units=layers[0], activation=activations[0], kernel_regularizer=K.regularizers.l2(lambtha), input_dim=nx))
    model.add(Dropout(1-keep_prob))
    for i in range(1, len(layers) - 1):
        model.add(Dense(units=layers[i], activation=activations[i], kernel_regularizer=K.regularizers.l2(lambtha)))
        model.add(Dropout(1-keep_prob))

    model.add(Dense(units=layers[-1], activation=activations[-1], kernel_regularizer=K.regularizers.l2(lambtha)))
    return model
