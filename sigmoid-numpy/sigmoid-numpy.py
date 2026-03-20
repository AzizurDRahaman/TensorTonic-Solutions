import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    # Write code here
    result=1/(1+(1/np.exp(x)))
    return result