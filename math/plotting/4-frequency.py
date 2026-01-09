#!/usr/bin/env python3
'''
This module plots histogram of student scores by setting bins as 10 units
'''
import numpy as np
import matplotlib.pyplot as plt


def frequency():
    '''
    This function does same thing as above
    '''
    np.random.seed(5)
    student_grades = np.random.normal(68, 15, 50)
    plt.figure(figsize=(6.4, 4.8))
    plt.xlim(0, 100)
    plt.ylim(0, 30)
    plt.xticks(np.arange(0, 101, step=10))
    plt.hist(student_grades, range=(0, 100), edgecolor='black')
    plt.xlabel('Grades')
    plt.ylabel('Number of Students')
    plt.title('Project A')
    plt.show()
