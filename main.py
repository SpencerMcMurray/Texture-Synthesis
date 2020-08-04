import time
from pathlib import Path

import matplotlib.pyplot as plt

import data
import synthesis as s


def run(texs, show_progress):
    """(dict of name:list of imgs) => dict of name:list of synthesized imgs
    Top level of the synthesis algorithm, calls lower functions to do heavy lifting.
    Returns synthesized images at differend window sizes to be sent through plot()
    """
    new_texs = {}
    orig_start = time.perf_counter()
    for i, tex_name in enumerate(texs):
        new_imgs = []
        for j, size in enumerate(data.WIN_SIZES):
            print(f"Starting synthesis for {tex_name} w={size}")
            start = time.perf_counter()
            new_img = s.synthesis(
                texs[tex_name]["gray"], texs[tex_name]["clr"], data.NEW_IMG_SIZE, size, data.GAUSS_MASKS[j], show_progress)
            print(f"Finished synthesis in {time.perf_counter() - start}s")
            new_imgs.append(new_img)
        new_texs[tex_name] = new_imgs
    print(f"Final end time of {time.perf_counter() - orig_start}s")
    return new_texs


def plot(texs, syns, save=True):
    """(dict of name:list of imgs, dict of name:list of synthesized imgs)
    Plots the synthesized images for varying window sizes next to the originals
    """
    fig, axs = plt.subplots(len(texs), len(
        data.WIN_SIZES) + 1, constrained_layout=True)
    fig.suptitle(f"Texture synthesis results w={data.WIN_SIZES}")
    for i, name in enumerate(texs):
        if len(texs) > 1:
            orig_ax, ax = axs[i, 0], axs[i, 1:]
        else:
            orig_ax, ax = axs[0], axs[1:]

        orig_ax.set_title(f"{name} Texture Original")
        orig_ax.imshow(texs[name]["clr"])

        for j, size in enumerate(data.WIN_SIZES):
            ax[j].set_title(f"{name} Texture Synthesized W={size}")
            ax[j].imshow(syns[name][j])
            if save:
                cmap = 'viridis' if len(syns[name][j].shape) == 3 else 'gray'
                plt.imsave(fname=Path(data.OUTPUT_DIR, name + f"_W_{size}" +
                                      data.OUTPUT_EXT), arr=syns[name][j], cmap=cmap)
    if not save:
        plt.show()


if __name__ == "__main__":
    SAVE, SHOW_PROG = True, False
    # Reads all imgs in /textures folder
    print("* STARTING READ *")
    TEXS = data.read_texs()
    print("* STARTING SYNTHESIS *")
    SYNS = run(TEXS, SHOW_PROG)
    print("* STARTING PLOTTING *")
    plot(TEXS, SYNS, SAVE)
    print("* DONE *")
