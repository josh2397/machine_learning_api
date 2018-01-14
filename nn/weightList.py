'''
Initialise a set number of weights for a given network layer


'''

def weightInit(u, v):
    return [np.random.normal(0, 1 / np.sqrt(shape[i+1]), (shape[i], shape[i + 1])) for i in range(self.numberOfLayers - 1)]

def biasInit(v):
    return 