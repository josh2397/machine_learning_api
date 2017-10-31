'''
Requirements:
    Select between sigmoid and sigmoid derivative using boolean value
    Support vector/tensor and single variables

'''

import numpy as np

class sigmoid:
    def sigmoidNormal(self, x):
        return np.nan_to_num(1/1+np.exp(-(x)))

    def sigmoidDerivative(self, x):
        return sigmoidNormal(x) * (1 / -sigmoidNormal(x))

    def __init__(self, x, deriv):

        if deriv == False:
            sigmoidNormal(self, x)
        else if deriv == True:
            sigmoidDerivative(self, x)


