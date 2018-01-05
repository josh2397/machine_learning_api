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

class sigmoid:
    
    def sigmoidNormal(self):
        return np.nan_to_num(1/1+np.exp(-(self.x)))

    def sigmoidDerivative(self):
        return sigmoidNormal(self.x) * (1 / sigmoidNormal(self.x))

    def __init__(self, x, deriv):

        self.x = x
        self.deriv = deriv

        if (self.deriv == False):
            self.sigmoidNormal()

        elif(self.deriv == True):
            self.sigmoidDerivative()




