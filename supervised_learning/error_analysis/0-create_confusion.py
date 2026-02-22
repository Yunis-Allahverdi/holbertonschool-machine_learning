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
    confusion = np.zeros((classes, classes))
    true_classes = np.argmax(labels, axis=1)
    pred_classes = np.argmax(logits, axis=1)
    for t, p in zip(true_classes, pred_classes):
        confusion[t, p] += 1

    return confusion
