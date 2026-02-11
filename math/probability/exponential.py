#!/usr/bin/env python3

'''
Documented
'''


class Exponential:
    def __init__(self, data=None, lambtha=1.):
        if data is not None:
            if isinstance(data, list):
                if len(data) < 2:
                    raise ValueError("data must contain multiple values")
                else:
                    total = 0
                    for i in data:
                        total += i
                    self.lambtha = 1 / float(total / len(data))
            else:
                raise TypeError("data must be a list")
        else:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            else:
                self.lambtha = float(lambtha)
