from skimage import io
import os
import numpy as np
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


def read_texs():
    """
    Compiles a dict with the format filename:image
    for all the textures in the /textures folder
    """
    texs = {}
    d = os.path.dirname(os.path.realpath(__file__))
    tex_path = os.path.join(d, "textures")
    for filename in os.listdir(tex_path):
        name = filename.split(".")[0]
        texs[name] = io.imread(fname=os.path.join(
            tex_path, filename), as_gray=True)
    return texs
