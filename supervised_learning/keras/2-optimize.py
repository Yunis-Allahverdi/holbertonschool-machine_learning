#!/usr/bin/env python3

'''
Documented
'''
import tensorflow.keras as K


def optimize_model(network, alpha, beta1, beta2):
    '''
    Doc
    '''
    optimizer = K.optimizers.Adam(
        learning_rate=alpha,
        beta_1=beta1,
        beta_2=beta2,
    )
    loss = 'categorical_crossentropy'
    network.compile(optimizer=optimizer, loss=loss, metrics=['accuracy'])
