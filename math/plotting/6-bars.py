#!/usr/bin/env python3
'''
This module plots stacked bar of fruits
'''
import numpy as np
import matplotlib.pyplot as plt


def bars():
    '''
    This function does same thing as above
    '''
    np.random.seed(5)
    fruit = np.random.randint(0, 20, (4,3))
    #plt.figure(figsize=(6.4, 4.8)) 
    names = ['Farrah', 'Fred', 'Felicia']
    plt.bar(names, fruit[0, :], label='apple', width=0.5, color='red')
    plt.bar(names, fruit[1, :], label='bananas', bottom=column1, width=0.5, color='yellow')
    plt.bar(names, fruit[2, :], label='oranges', bottom=column1+column2, width=0.5, color='#ff8000')
    plt.bar(names, fruit[3, :], label='peaches', bottom=column1+column2+column3, width=0.5, color='#ffe5b4')
    plt.yticks(np.arange(0, 81, 10))
    plt.legend()
    plt.title('Number of Fruit per Person')
    plt.ylabel('Quantity of Fruit')
    plt.show()
