'''
Requirements:
    Select between relu and reluDerivative using boolean value
    Support vector/tensor and single variables

'''

import numpy as np

class relu:
    def relu(self, x):
        return 1

    def reluDerivative(self, x):
        return 0

    def __init__(self, x):

        self.x = x
        