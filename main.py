import data
import synthesis as s
import time
import matplotlib.pyplot as plt


def run(texs, debug):
    new_texs = {}
    fig, axs = plt.subplots(len(texs), 2, constrained_layout=True)
    fig.suptitle(f"Texture synthesis results w={data.WIN_SIZE}")
    for i, tex_name in enumerate(texs):
        print(f"Starting synthesis for {tex_name}")
        ax2 = None
        if debug:
            if len(texs) > 1:
                ax1, ax2 = axs[i, 0], axs[i, 1]
            else:
                ax1, ax2 = axs[0], axs[1]

            ax1.set_title(f"{tex_name} Texture Original")
            ax2.set_title(f"{tex_name} Texture Synthesized")
            ax1.imshow(texs[tex_name], cmap="gray")

        start = time.perf_counter()
        new_img = s.synthesis(
            texs[tex_name], data.NEW_IMG_SIZE, data.WIN_SIZE, ax2, debug)
        print(f"Finished synthesis in {time.perf_counter() - start}s")
        new_texs[tex_name] = new_img
    return new_texs


def plot(texs, syns):
    fig, axs = plt.subplots(len(texs), 2, constrained_layout=True)
    fig.suptitle(f"Texture synthesis results w={data.WIN_SIZE}")
    for i, name in enumerate(texs):
        if len(texs) > 1:
            ax1, ax2 = axs[i, 0], axs[i, 1]
        else:
            ax1, ax2 = axs[0], axs[1]

        ax1.set_title(f"{name} Texture Original")
        ax2.set_title(f"{name} Texture Synthesized")

        ax1.imshow(texs[name], cmap="gray")
        ax2.imshow(syns[name], cmap="gray")
    plt.show()


if __name__ == "__main__":
    DEBUG = True
    # Reads all imgs in /textures folder
    print("* STARTING READ *")
    TEXS = data.read_texs()
    print("* STARTING SYNTHESIS *")
    SYNS = run(TEXS, DEBUG)
    if not DEBUG:
        print("* STARTING PLOTTING *")
        plot(TEXS, SYNS)
    print("* DONE *")
