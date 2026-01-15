#!/usr/bin/env python3

'''
This module calc the derivative of poly
'''


def poly_derivative(poly):
    if not isinstance(poly, list):
        return None
    if not all(isinstance(c, (int, float)) for c in poly):
        return None
    if len(poly) == 0:
        return None

    poly_der = []
    for i in range(1, len(poly)):
        poly_der.append(i * poly[i])

    if len(poly_der) == 0:
        return [0]
    return poly_der
