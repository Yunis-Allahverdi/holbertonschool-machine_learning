#!/usr/bin/env python3

'''
This module calc the integral of poly
'''


def poly_integral(poly, C=0):
    '''
    Does same thing as above
    '''
    if not isinstance(poly, list):
        return None
    if not all(isinstance(c, (int, float)) for c in poly):
        return None
    if len(poly) == 0:
        return None
    if not isinstance(C, (int, float)):
        return None
    if poly == [0]:
        return [0]

    poly_int = [C]

    for i in range(len(poly)):
        coeff = poly[i] / (i + 1)
        if coeff.is_integer():
            coeff = int(coeff)
        poly_int.append(coeff)

    if len(poly_int) == 0:
        return None
    return poly_int
