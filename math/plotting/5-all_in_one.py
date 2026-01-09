#!/usr/bin/env python3
'''
This module plots five previous charts at the same time
'''
import numpy as np
import matplotlib.pyplot as plt


def all_in_one():
    '''
    This function does same thing as above
    '''
    y0 = np.arange(0, 11) ** 3

    mean = [69, 0]
    cov = [[15, 8], [8, 15]]
    np.random.seed(5)
    x1, y1 = np.random.multivariate_normal(mean, cov, 2000).T
    y1 += 180

    x2 = np.arange(0, 28651, 5730)
    r2 = np.log(0.5)
    t2 = 5730
    y2 = np.exp((r2 / t2) * x2)

    x3 = np.arange(0, 21000, 1000)
    r3 = np.log(0.5)
    t31 = 5730
    t32 = 1600
    y31 = np.exp((r3 / t31) * x3)
    y32 = np.exp((r3 / t32) * x3)

    np.random.seed(5)
    student_grades = np.random.normal(68, 15, 50)

    a = plt.subplot2grid((3,2), (0,0), colspan=1)
    b = plt.subplot2grid((3,2), (1,0), colspan=1)
    c = plt.subplot2grid((3,2), (1,1), colspan=1)
    d = plt.subplot2grid((3,2), (0,1), colspan=1)
    e = plt.subplot2grid((3,2), (2,0), colspan=2)
    a.set_xlim(0, 10)
    a.plot(y, 'r')
    b.set_xlim([0, 28650])
    b.set_yscale('log')
    b.set_xlabel('Time (years)',fontsize=8)
    b.set_ylabel('Fraction Remaining',fontsize=8)
    b.set_title('Exponential Decay of C-14',fontsize=8)
    b.plot(x2, y2)
    c.plot(x3, y31, 'r--', x3, y32, 'g')
    c.set_title("Exponential Decay of Radioactive Elements", fontsize=8)
    c.set_xlabel("Time (years)",fontsize=8)
    c.set_ylabel("Fraction Remaining",fontsize=8)
    c.legend(['C-14', 'Ra-226'], loc="upper right",fontsize=8)
    d.set_xlabel('Height (in)',fontsize=8)
    d.set_ylabel('Weight (lbs)',fontsize=8)
    d.set_title('Men\'s Height vs Weight',fontsize=8)
    d.plot(x1, y1, 'mo')
    e.set_xlim(0, 100)
    e.set_ylim(0, 30)
    e.set_xticks(np.arange(0, 101, step=10))
    e.hist(student_grades, range=(0, 100), edgecolor='black')
    e.set_xlabel('Grades',fontsize=8)
    e.set_ylabel('Number of Students',fontsize=8)
    e.set_title('Project A',fontsize=8)
    plt.tight_layout()
    plt.suptitle("All in One", fontsize=10)
    plt.show()
