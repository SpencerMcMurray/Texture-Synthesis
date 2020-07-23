import numpy as np
import data
import helpers as hlp
import time
import matplotlib.pyplot as plt


def synthesis(sample, new_img_shape, window_size, gauss_mask):
    """(img, 2-tuple of int, int, 2D gaussian mask) => synthesized img
    Implementation of the Texture Synthesis by Non-parametric Sampling
    algorithm developed by Efros & Leung.
    https://people.eecs.berkeley.edu/~efros/research/NPS/alg.html
    Returns a synthesized image of size new_img_shape

    REQ: gauss_mask's size == window_size
    REQ: window_size <= min(sample.shape)
    """
    max_thold = data.MAX_ERR_THOLD
    rows, cols = new_img_shape
    pixel_count = rows * cols
    new_img = np.zeros((rows, cols))
    filled = np.zeros((rows, cols))
    sample_windows = hlp.precompute_windows(sample, window_size)

    # Seed new img and filled
    seed = hlp.seed_sample(sample, data.SEED_SIZE)
    mid_row, mid_col = rows // 2, cols // 2
    new_img[mid_row:mid_row + data.SEED_SIZE,
            mid_col:mid_col + data.SEED_SIZE] = seed
    filled[mid_row:mid_row + data.SEED_SIZE,
           mid_col:mid_col + data.SEED_SIZE] = np.ones((data.SEED_SIZE, data.SEED_SIZE))
    num_filled = data.SEED_SIZE ** 2
    start = time.perf_counter()

    # Main while loop
    while num_filled < pixel_count:
        print(f"{pixel_count - num_filled} left; {round(100 * num_filled / pixel_count, 2)}% complete; {int(time.perf_counter()-start)}s")
        progress = False
        unfilled = hlp.unfilled_neighbours(filled, window_size)
        for pixel in unfilled:
            x1, y1 = pixel["pixel"]
            window = hlp.get_window(new_img, (x1, y1), window_size)
            valid_window = hlp.get_window(filled, (x1, y1), window_size)
            best_match = hlp.find_match(
                sample, window, valid_window, sample_windows, gauss_mask)
            # If its lower than our max thold then fill in the pixel
            if best_match["error"] < max_thold:
                x2, y2 = best_match["pixel"]
                new_img[x1, y1] = sample[x2, y2]
                filled[x1, y1] = 1
                progress = True
                num_filled += 1
        if not progress:
            max_thold *= 1.1
    return new_img
