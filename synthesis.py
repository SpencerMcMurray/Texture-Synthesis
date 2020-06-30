from random import randint
import data
import helpers as hlp
import numpy as np


def seed_sample(sample, size):
    """
    Creates the random (size)x(size) seed for the new image
    """
    rows, cols = sample.new_img_shape
    rand_x, rand_y = randint(0, rows - size), randint(0, cols - size)
    return sample[rand_x:rand_x + size, rand_y:rand_y + size]


def synthesis(sample, new_img_shape, window_size):
    rows, cols = new_img_shape
    new_img = np.zeros((rows, cols))
    filled = np.zeros((rows, cols))

    # Seed new img and filled
    seed = seed_sample(sample, data.SEED_SIZE)
    mid_row, mid_col = rows // 2, cols // 2
    new_img[mid_row:mid_row + data.SEED_SIZE,
            mid_col:mid_col + data.SEED_SIZE] = seed
    filled[mid_row:mid_row + data.SEED_SIZE,
           mid_col:mid_col + data.SEED_SIZE] = np.ones((data.SEED_SIZE, data.SEED_SIZE))
    num_filled = data.SEED_SIZE ** 2

    gaus_win = hlp.gauss_window(window_size, data.SIGMA)

    return sample
