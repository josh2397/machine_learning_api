'''
Computes either sigmoid or sigmoid derivative

False - sigmoid,
True  - sigmoid derivative
'''

'''
Requirements:
    Select between sigmoid and sigmoid derivative using boolean value
    Support vector/tensor and single variables

'''

import numpy as np

def sigmoid(x, key):
    if key == 0:
        return np.nan_to_num(1/1+np.exp(-(x)))
    elif key == 1:
        return sigmoidNormal(x) * (1 / sigmoidNormal(x))

def relu(x, key):
    if key == 0:
        if x > 0:
            return x
        else:
            return 0
    elif key == 1:
        if x > 0:
            return 1
        else:
            return 0

def leakyRelu(x, key):
    if key == 0:
        if x > 0:
            return x
        else:
            return 0.01*x
    elif key == 1:
        if x > 0:
            return 1
        else:
            return 0.01

def elu(x, a, key):
    if key == 0:
        if x >= 0:
            return x
        else:
            return a*(np.exp(x) - 1)
    elif key == 1:
        if x >= 0:
            return 1
        else:
            return a*(np.exp(x))

def celu(x, a, key):
    if key == 0:
        if x >= 0:
            return x
        else:
            return a*(np.exp(x/a) - 1)
    elif key == 1:
        if x >= 0:
            return 1
        else:
            return np.exp(x/a)

def softmax(x, key):
    

'''def __init__(self, x):

    self.x = x
    #self.deriv = deriv

    if (self.deriv == False):
        self.sigmoidNormal()

    elif(self.deriv == True):
        self.sigmoidDerivative()'''




