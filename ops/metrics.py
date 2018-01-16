'''
Computes the metrics of the network from the given predictions and labels


'''

import matplotlib as mpl
import numpy as np


def truePositives(labels, predictions):
    #postponed 
    truePositives = 0
    for instance in labels and predictions:
        if labels == predictions:
             truePositives = truePositives + 1
def trueNegatives(labels, predictions):
    return 1
def falsePositives(labels, predictions):
    return 1
def falseNegatives(labels, predictions):
    return 1

def roc():
    return 1

def auc(labels, predictions, num_thresholds, curve):
    return 1

def precision():
    return 1

def recall():
    return 1

def sensitivityAtSpecificity():
    return 1

def accuracy(labels, predictions):
    return 1

def sensitivity():
    return 1

def specificity():
    return 1

def f1Score():
    return 1

def falseNegativeRate():
    return 1

def falseDiscoveryRate():
    return 1

def falsePostiveRate():
    return 1

def negativePredictiveValue():
    return 1

def mcc():
    return 1
    


