#!/usr/bin/env python3

'''
This module calc the derivative of poly
'''


def poly_derivative(poly):
    if not isinstance(poly, list):
        return None

    poly_der = []
    for i in range(1, len(poly)):    
        poly_der.append(i * poly[i])

    return poly_der
