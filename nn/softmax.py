'''
Requirements:
    Select between softmax and softmaxDerivative using boolean value
    Support vector/tensor and single variables

'''

import numpy as np

class softmax:

    def softmax(self, x):
        return 1

    def softmaxDerivative(self, x):
        return 0
    
    def __init__(self, x):

        self.x = x