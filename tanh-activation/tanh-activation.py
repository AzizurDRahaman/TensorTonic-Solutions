import numpy as np

def tanh(x):
    """
    Implement Tanh activation function.
    """
    # Write code here
    num=np.exp(x)
    return (num-(1/num))/(num+(1/num))
    # pass