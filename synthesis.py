import numpy as np
import data
import helpers as hlp
import time
import matplotlib.pyplot as plt


def synthesis(sample, new_img_shape, window_size, ax, debug):
    """
    Implementation of the Texture Synthesis by Non-parametric Sampling
    algorithm developed by Efros & Leung.
    https://people.eecs.berkeley.edu/~efros/research/NPS/alg.html
    """
    max_thold = data.MAX_ERR_THOLD
    rows, cols = new_img_shape
    pixel_count = rows * cols
    new_img = np.zeros((rows, cols))
    filled = np.zeros((rows, cols))

    # Seed new img and filled
    seed = hlp.seed_sample(sample, data.SEED_SIZE)
    mid_row, mid_col = rows // 2, cols // 2
    new_img[mid_row:mid_row + data.SEED_SIZE,
            mid_col:mid_col + data.SEED_SIZE] = seed
    filled[mid_row:mid_row + data.SEED_SIZE,
           mid_col:mid_col + data.SEED_SIZE] = np.ones((data.SEED_SIZE, data.SEED_SIZE))
    num_filled = data.SEED_SIZE ** 2
    start = time.perf_counter()

    if debug:
        h = ax.imshow(new_img, cmap="gray")

    # Main while loop
    while num_filled < pixel_count:
        print(f"{pixel_count - num_filled} left; {100 * num_filled / pixel_count}% complete; {int(time.perf_counter()-start)}s")
        if debug:
            h.set_data(new_img)
            plt.draw(), plt.pause(1e-1)
        progress = False
        unfilled = hlp.unfilled_neighbours(filled)
        for pixel in unfilled:
            x1, y1 = pixel["pixel"]
            window = hlp.get_window(new_img, (x1, y1), data.WIN_SIZE)
            valid_window = hlp.get_window(filled, (x1, y1), data.WIN_SIZE)
            best_match = hlp.find_match(sample, window, valid_window)
            # If its lower than our max thold then fill in the pixel
            # print(best_match["error"], ";", max_thold)
            if best_match["error"] < max_thold:
                x2, y2 = best_match["pixel"]
                new_img[x1, y1] = sample[x2, y2]
                filled[x1, y1] = 1
                progress = True
                num_filled += 1
        if not progress:
            max_thold *= 1.1
    return new_img
