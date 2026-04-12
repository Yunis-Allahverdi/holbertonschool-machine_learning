#!/usr/bin/env python3
"""Doc"""
import tensorflow as tf


def flip_image(image):
    """
    Doc
    """
    flip = tf.image.flip_left_right(image)
    return flip
