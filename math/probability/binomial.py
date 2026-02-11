#!/usr/bin/env python3


'''
Doc
'''


class Binomial:
    '''
    Doc
    '''

    def __init__(self, data=None, n=1, p=0.5):
        if data is None:
            if n <= 0:
                raise ValueError("n must be a positive value")
            if not (0 < p < 1):
                raise ValueError("p must be greater than 0 and less than 1")
            self.n = int(n)
            self.p = float(p)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")

            mean = sum(data) / len(data)
            sum_sq = sum([(x - mean) ** 2 for x in data])
            variance = sum_sq / len(data)

            p_temp = 1 - (variance / mean)
            self.n = int(round(mean / p_temp))
            self.p = float(mean / self.n)

    def pmf(self, k):
        '''
        Doc
        '''

        k = int(k)
        if k < 0 or k > self.n:
            return 0

        def factorial(num):
            f = 1
            for i in range(1, num + 1):
                f *= i
            return f

        n_fact = factorial(self.n)
        k_fact = factorial(k)
        nk_fact = factorial(self.n - k)

        combination = n_fact / (k_fact * nk_fact)
        return combination * (self.p ** k) * ((1 - self.p) ** (self.n - k))

    def cdf(self, k):
        '''
        Doc
        '''

        k = int(k)
        if k < 0:
            return 0
        if k >= self.n:
            return 1

        total = 0
        for i in range(k + 1):
            total += self.pmf(i)

        return total
