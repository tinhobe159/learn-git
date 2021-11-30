import numpy as np


def getAb2(x,y):
    col1 = np.ones(len(x))
    colx = np.array(x)
    A = np.transpose(np.array([col1, colx**2]))
    b = np.array(y).reshape(len(y), 1)
    return A, b
bptoithieu(getAb2(x,y)[0], getAb2(x,y)[1])