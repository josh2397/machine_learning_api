'''
Initialise a set number of weights for a given network layer


'''
import numpy as np

def weightInit(numberOfLayers, shape):
    return [np.random.normal(0, 1 / np.sqrt(shape[i+1]), (shape[i], shape[i + 1])) for i in range(numberOfLayers - 1)]

def biasInit(numberOfLayers, shape):
    return [np.random.normal(0, 1, (shape[i])) for i in range (1, numberOfLayers)]