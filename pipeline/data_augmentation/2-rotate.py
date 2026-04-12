#!/usr/bin/env python3
"""
Doc
"""
import tensorflow as tf


def rotate_image(image):
    """
    Doc
    """
    img = tf.image.rot90(image, k=1)
    return img
