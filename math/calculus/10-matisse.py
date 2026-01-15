#!/usr/bin/env python3

'''
This module calc the derivative of poly
'''


def poly_derivative(poly):
    if not isinstance(poly, list):
        return None

    poly_der = []
    for i in range(len(poly)):
        if i > 0:
            if poly[i] == 0:
                poly_der.append(0)
            else:
                poly_der.append(i * poly[i])

    return poly_der
