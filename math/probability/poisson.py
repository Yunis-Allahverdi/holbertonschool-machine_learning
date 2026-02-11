#!/usr/bin/env python3

'''
Documented
'''


class Poisson:
    '''
    Documented
    '''

    def __init__(self, data=None, lambtha=1.):
        if data is not None:
            if isinstance(data, list):
                if len(data) < 2:
                    raise ValueError("data must contain multiple values")
                else:
                    total = 0
                    for i in data:
                        total += i
                    self.lambtha = float(total / len(data))
            else:
                raise TypeError("data must be a list")

        else:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            else:
                self.lambtha = float(lambtha)

    def pmf(self, k):
        '''
        Documented
        '''
        if not isinstance(k, int):
            k = int(k)
        if k < 0:
            return 0

        fact = 1
        for i in range(1, k + 1):
            fact *= i

        return ((self.lambtha ** k) * (2.7182818285 ** -self.lambtha)) / fact

    def cdf(self, k):
        '''
        Documented
        '''
        if not isinstance(k, int):
            k = int(k)

        if k < 0:
            return 0

        fact = 1
        e_inv = 2.7182818285 ** (-self.lambtha)
        total_probability = 0
        for i in range(0, k + 1):
            if i == 0:
                total_probability += e_inv
                continue
            fact *= i
            total_probability += ((self.lambtha ** i) * e_inv) / fact

        return total_probability
