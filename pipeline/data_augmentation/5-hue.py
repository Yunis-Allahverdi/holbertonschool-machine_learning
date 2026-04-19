#!/usr/bin/env python3
"""
Documented
"""
import tensorflow as tf


def change_hue(image, delta):
    """
    Doc
    """
    img = tf.image.adjust_hue(image, delta)
    return img
