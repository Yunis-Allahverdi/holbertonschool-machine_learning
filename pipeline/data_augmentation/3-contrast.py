#!/usr/bin/env python3
"""
Doc
"""


import tensorflow as tf


def change_contrast(image, lower, upper):
    """
    Doc
    """

    img = tf.image.random_contrast(image, lower, upper)
    return img
