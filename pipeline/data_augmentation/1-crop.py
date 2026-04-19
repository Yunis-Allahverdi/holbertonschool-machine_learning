#!/usr/bin/env python3
"""
Documented
"""
import tensorflow as tf


def crop_image(image, size):
    """
    Doc
    """
    img = tf.image.random_crop(image, size=size)
    return img
