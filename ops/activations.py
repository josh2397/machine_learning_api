'''
Computes activation for given function

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
        return 1/(1+np.exp(-(x))) #np.nan_to_num()
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
    if key == 0:
        sum = 0
        output = []
        for i in x:
            sum = sum + np.exp(x[i-1])
        #change for loop range to number of classes
        for i in x:
            output.append(np.exp(x[i-1]) / sum)

        return output

    elif key == 1:
        return 1
        #implement softmax derivative

def softplus(x, key):
    if key == 0:
        return np.log(1 + np.exp(x))
    elif key == 1:
        return 1 / (1 + np.exp(-(x)))

