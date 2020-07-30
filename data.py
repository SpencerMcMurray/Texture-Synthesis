import os
from pathlib import Path

import numpy as np
from skimage import io

import helpers as hlp

NEW_IMG_SIZE = (128, 128)
WIN_SIZES = np.array([17, 19, 21])
# Values described here: https://people.eecs.berkeley.edu/~efros/research/NPS/alg.html
SEED_SIZE = 3
SIGMAS = WIN_SIZES / 6.4
ERR_THOLD = 1e-1
MAX_ERR_THOLD = 3e-1

GAUSS_MASKS = [hlp.gauss_window(WIN_SIZES[i], SIGMAS[i])
               for i in range(len(WIN_SIZES))]

FILES_DIR = Path("./textures")
OUTPUT_EXT = ".png"
OUTPUT_DIR = Path("./output")


def read_texs():
    """() => dict of name:list of imgs
    Compiles a dict with the format filename:image
    for all the textures in the /textures folder
    """
    texs = {}
    for filename in os.listdir(FILES_DIR):
        name = str(filename).split(".")[0]
        texs[name] = io.imread(
            fname=Path(str(FILES_DIR), filename), as_gray=True)
    return texs
