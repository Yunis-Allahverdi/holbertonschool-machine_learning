#!/usr/bin/env python3

'''
Documented
'''
import tensorflow.keras as K


def build_model(nx, layers, activations, lambtha, keep_prob):
    '''
    Doc
    '''
    x_input = K.layers.Input(shape=(nx,))
    x = x_input

    for i in range(len(layers) - 1):
        x = K.layers.Dense(
            layers[i],
            activation=activations[i],
            kernel_regularizer=K.regularizers.l2(lambtha)
            )(x)

        x = K.layers.Dropout(rate=1-keep_prob)(x)

    x_output = K.layers.Dense(
        units=layers[-1],
        activation=activations[-1],
        kernel_regularizer=K.regularizers.l2(lambtha)
    )(x)
    model = K.Model(inputs=x_input, outputs=x_output)
    return model
