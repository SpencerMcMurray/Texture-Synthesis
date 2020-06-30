from scipy.signal.windows import gaussian
import numpy as np
import data


def gauss_window(shape, sigma):
    """
    Create a 2D Gaussian window
    Edited from https://stackoverflow.com/questions/17190649/how-to-obtain-a-gaussian-filter-in-python
    """
    k = shape // 2
    y, x = np.ogrid[-k:k+1, -k:k+1]
    h = np.exp(-(x*x + y*y) / (2.*sigma*sigma))
    h[h < np.finfo(h.dtype).eps*h.max()] = 0
    sumh = h.sum()
    if sumh != 0:
        h /= sumh
    return h
