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
    plt.figure(figsize=(6.4, 4.8)) 
    names = ['Farrah', 'Fred', 'Felicia']
    column1 = fruit[0, :]
    column2 = fruit[1, :]
    column3 = fruit[2, :]
    column4 = fruit[3, :]
    plt.bar(names, column1, label='apples', width=0.5, color='red')
    plt.bar(names, column2, label='bananas', bottom=column1, width=0.5, color='yellow')
    plt.bar(names, column3, label='oranges', bottom=column1+column2, width=0.5, color='#ff8000')
    plt.bar(names, column4, label='peaches', bottom=column1+column2+column3, width=0.5, color='#ffe5b4')
    plt.yticks(np.arange(0, 81, 10))
    plt.legend()
    plt.title('Number of Fruit per Person')
    plt.ylabel('Quantity of Fruit')
    plt.show()
