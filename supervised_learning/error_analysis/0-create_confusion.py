#!/usr/bin/env python3
'''
Doc
'''
import numpy as np


def create_confusion_matrix(labels, logits):
	'''
	Doc
    '''

    classes = labels.shape[1]
    y_true = np.argmax(labels, axis=1)
    y_pred = np.argmax(logits, axis=1)
    confusion = np.zeros((classes, classes))
    np.add.at(confusion, (y_true, y_pred), 1)
    return confusion
