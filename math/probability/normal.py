#!/usr/bin/env python3


'''
Doc
'''


class Normal:
    '''
    Doc
    '''

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
