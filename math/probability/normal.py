#!/usr/bin/env python3


'''
Doc
'''


class Normal:
    '''
    Doc
    '''
    pi = 3.141592653589793

    def __init__(self, data=None, mean=0., stddev=1.):
        if data is not None:
            if isinstance(data, list):
                if len(data) < 2:
                    raise ValueError("data must contain multiple values")
                else:
                    total = 0
                    for i in data:
                        total += i
                    self.mean = float(total / len(data))

                    total2 = 0
                    for i in data:
                        total2 += (i - self.mean) ** 2

                    self.stddev = (total2 / len(data)) ** 0.5
            else:
                raise TypeError("data must be a list")
        else:
            if stddev <= 0:
                raise ValueError("stddev must be a positive value")
            else:
                self.stddev = float(stddev)
                self.mean = float(mean)

    def z_score(self, x):
        '''
        Doc
        '''
        return (x - self.mean) / self.stddev

    def x_value(self, z):
        '''
        Doc
        '''
        return z * self.stddev + self.mean

    def pdf(self, x):
        '''
        Doc
        '''
        pi = 3.141592653589793
        e = 2.7182818285
        exponent = -0.5 * ((x - self.mean) / self.stddev) ** 2
        coefficient = 1 / (self.stddev * (2 * pi) ** 0.5)

        return coefficient * (e ** exponent)

    def cdf(self, x):
        '''
        Doc
        '''
        v = (x - self.mean) / (self.stddev * (2 ** 0.5))
        erf = (2 / (pi ** 0.5)) * (
            v - (v**3 / 3) + (v**5 / 10) - (v**7 / 42) + (v**9 / 216)
        )

        return 0.5 * (1 + erf)
