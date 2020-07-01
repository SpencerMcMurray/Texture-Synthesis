from scipy.signal.windows import gaussian
from scipy.ndimage import binary_dilation
from random import randint
import numpy as np
import data


def find_match(sample, window, valid_window):
    """
    Returns a random match from all the best matches for the window
    """
    size, itvl = data.WIN_SIZE, data.WIN_SIZE // 2
    rows, cols = sample.shape
    ssd = np.zeros((rows - (2 * itvl) - 1, cols - (2 * itvl) - 1))
    tot_weight = np.sum(window * valid_window)

    if tot_weight == 0:
        raise Exception("Window size not large enough")

    # Go through each useable sample pixel and calculate its ssd value
    for i in range(itvl, rows - itvl - 1):
        for j in range(itvl, cols - itvl - 1):
            curr = sample[i - itvl:i + itvl + 1, j - itvl:j + itvl + 1]
            dist = (window - curr) ** 2
            x, y = i - itvl, j - itvl
            ssd[x, y] = np.sum(dist * valid_window *
                               data.GAUSS_MASK) / tot_weight
    # Get pixels under the error thold
    best = np.argwhere(ssd <= (np.min(ssd) * (1 + data.ERR_THOLD)))
    px = best[randint(0, len(best) - 1)]
    return {"pixel": px, "error": ssd[px[0], px[1]]}


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


def unfilled_neighbours(filled_img):
    """
    Gets all non-filled pixels which neighbour filled ones,
    then sort them descendingly based on the count of
    neighbouring filled pixels
    """
    unfilled = []
    rows, cols = np.nonzero(binary_dilation(filled_img) - filled_img)
    for i in range(len(rows)):
        px = (rows[i], cols[i])
        w = get_window(filled_img, px, data.WIN_SIZE)
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
