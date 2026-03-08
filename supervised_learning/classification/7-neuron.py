#!/usr/bin/env python3
'''
Doc
'''
import numpy as np


class Neuron:
    '''
    Doc
    '''

    def __init__(self, nx):

        if not isinstance(nx, int):
            raise TypeError('nx must be an integer')

        if nx < 1:
            raise ValueError('nx must be a positive integer')

        self.__W = np.random.randn(1, nx)
        self.__b = 0
        self.__A = 0

    def forward_prop(self, x):
        '''
        Doc
        '''

        Z = np.dot(self.__W, x) + self.__b
        self.__A = 1 / (1 + np.exp(-Z))
        return self.__A

    def cost(self, Y, A):
        '''
        Doc
        '''
        m = Y.shape[1]
        cost = (-1/m) * np.sum(Y * np.log(A) + (1 - Y) * np.log(1.0000001 - A))
        return cost

    def evaluate(self, X, Y):
        '''
        Doc
        '''
        A = self.forward_prop(X)
        predictions = np.where(A >= 0.5, 1, 0)
        cost = self.cost(Y, A)
        return predictions, cost

    def gradient_descent(self, X, Y, A, alpha=0.05):
        '''
        Doc
        '''
        m = X.shape[1]
        dZ = A - Y
        dW = (1/m) * np.dot(dZ, X.T)
        db = (1/m) * np.sum(dZ)
        self.__W -= alpha * dW
        self.__b -= alpha * db

    def train(self, X, Y, iterations=5000, alpha=0.05, verbose=True, graph=True, step=100):
        if not isinstance(iterations, int):
            raise TypeError("iterations must be an integer")
        if iterations <= 0:
            raise ValueError("iterations must be a positive integer")
        if not isinstance(alpha, float):
            raise TypeError("alpha must be a float")
        if alpha <= 0:
            raise ValueError("alpha must be positive")

        if (verbose or graph):
            if not isinstance(step, int):
                raise TypeError("step must be an integer")
            if step <= 0 or step > iterations:
                raise ValueError("step must be positive and <= iterations")

        costs = []
        steps = []

        for i in range(iterations + 1):
            if i > 0:
                A = self.forward_prop(X)
                self.gradient_descent(X, Y, A, alpha)
            else:
                A = self.__A  # before training

            if verbose and i % step == 0:
                cost = self.cost(Y, self.__A)
                print(f"Cost after {i} iterations: {cost}")

            if graph and i % step == 0:
                costs.append(self.cost(Y, self.__A))
                steps.append(i)

            if graph:
                import matplotlib.pyplot as plt
                plt.plot(steps, costs, 'b-')
                plt.xlabel('iteration')
                plt.ylabel('cost')
                plt.title('Training Cost')
                plt.show()

        return self.evaluate(X, Y)

    @property
    def W(self):
        '''Getter for W'''
        return self.__W

    @property
    def b(self):
        '''Getter for b'''
        return self.__b

    @property
    def A(self):
        '''Getter for A'''
        return self.__A
