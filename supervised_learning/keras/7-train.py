#!/usr/bin/env python3

'''
Documented
'''
import tensorflow.keras as K


def train_model(network, data, labels, batch_size, epochs,
                validation_data=None, early_stopping=False, patience=0,
                learning_rate_decay=False, alpha=0.1, decay_rate=1,
                save_best=False, filepath=None,
                verbose=True, shuffle=False):
    '''
    Doc
    '''
    callbacks = []

    if early_stopping and validation_data is not None:
        early_stop = K.callbacks.EarlyStopping(
            monitor='val_loss',
            patience=patience,
            restore_best_weights=True
        )
        callbacks.append(early_stop)

    if learning_rate_decay and validation_data is not None:
        def lr_scheduler(epoch, lr):
            return alpha / (1 + decay_rate * epoch)

        callbacks.append(
                K.callbacks.LearningRateScheduler(lr_scheduler, verbose=1)
                )

    history = network.fit(
        x=data,
        y=labels,
        batch_size=batch_size,
        epochs=epochs,
        verbose=verbose,
        shuffle=shuffle,
        validation_data=validation_data,
        callbacks=callbacks
    )

    if save_best and filepath is not None:
        checkpoint = K.callbacks.ModelCheckpoint(
            filepath=filepath,
            save_best_only=True,
            monitor='val_loss'
        )
        callbacks.append(checkpoint)

    return history
