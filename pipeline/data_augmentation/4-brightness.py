#!/usr/bin/env python3
"""
Doc
"""
import tensorflow as tf


def change_brightness(image, max_delta):
    """
    Doc
    """
    img = tf.image.random_brightness(image, max_delta)
    return img
