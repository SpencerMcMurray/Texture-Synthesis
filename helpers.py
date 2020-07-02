from scipy.signal.windows import gaussian
from scipy.ndimage import binary_dilation
from random import randint
import numpy as np
import data


def get_window(img, pixel, size):
    """
    Creates a window of size (size)x(size) around pixel.
    This window is filled with the image around pixel, or
    zero if the window goes outside the image boundaries
    """
    x_lim, y_lim = img.shape
    w = np.zeros((size, size))
    itvl = size // 2
    for k in range(size):
        for r in range(size):
            img_i, img_j = k + pixel[0] - itvl, r + pixel[1] - itvl
            if img_i < x_lim and img_i >= 0 and img_j < y_lim and img_j >= 0:
                w[k, r] = img[img_i, img_j]
    return w


def precompute_windows(img, win_size):
    rows, cols = img.shape
    windows = []
    for i in range(rows):
        curr_windows = []
        for j in range(cols):
            curr_windows.append(get_window(img, (i, j), win_size))
        windows.append(curr_windows)
    return np.array(windows)


def find_match(sample, window, valid_window, sample_windows, gauss_mask):
    """
    Returns a random match from all the best matches for the window
    """
    rows, cols = sample.shape
    ssd = np.zeros(sample.shape)
    valid_gauss = gauss_mask * valid_window
    tot_weight = np.sum(valid_gauss)

    if tot_weight == 0:
        raise Exception("Window size not large enough")

    # Go through each useable sample pixel and calculate its ssd value
    for i in range(rows):
        for j in range(cols):
            dist = (window - sample_windows[i, j]) ** 2
            ssd[i, j] = np.sum(dist * valid_gauss) / tot_weight
    # Get pixels under the error thold
    best = np.argwhere(ssd <= (np.min(ssd) * (1 + data.ERR_THOLD)))
    px = best[randint(0, len(best) - 1)]
    return {"pixel": px, "error": ssd[px[0], px[1]]}


def unfilled_neighbours(filled_img, win_size):
    """
    Gets all non-filled pixels which neighbour filled ones,
    then sort them descendingly based on the count of
    neighbouring filled pixels
    """
    unfilled = []
    rows, cols = np.nonzero(binary_dilation(filled_img) - filled_img)
    for i in range(len(rows)):
        px = (rows[i], cols[i])
        w = get_window(filled_img, px, win_size)
        unfilled.append({"pixel": px, "count": np.sum(w)})
    return sorted(unfilled, key=lambda p: p["count"], reverse=True)


def seed_sample(sample, size):
    """
    Creates the random (size)x(size) seed for the new image
    """
    rows, cols = sample.shape
    rand_x, rand_y = randint(0, rows - size), randint(0, cols - size)
    return sample[rand_x:rand_x + size, rand_y:rand_y + size]


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
