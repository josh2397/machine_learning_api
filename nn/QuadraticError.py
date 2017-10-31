'''
Requirements

'''

class quadraticCost:

    @staticmethod
    def quadratic(summation, expected):
        return 0.5*(summation - expected)**2

    @staticmethod
    def quadraticDerivative(summation, expected):
        return summation - expected

    @staticmethod
    def delta(inputs, summation, expected):
        return (summation - expected)*sigmoidDerivative(inputs)